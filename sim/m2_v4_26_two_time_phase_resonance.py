#!/usr/bin/env python3
"""M2 V4.26 two-time phase-memory / resonance / crystal-gate test.

This is a conventional energy-accounted model. Rotor/segment events are represented
as explicit charge impulses into a damped parallel LC mode. A passive diode branch
may transfer only the positive phase into a storage capacitor. The model tests
timing, resonance, rectification and energy bookkeeping; it does not model an
anomalous energy source.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Parameters:
    resonator_c_f: float = 10e-9
    resonator_l_h: float = 10e-3
    resonator_q: float = 20.0
    store_c_f: float = 100e-9
    impulse_charge_c: float = 10e-9
    event_hz: float = 50.0
    diode_drop_v: float = 0.2
    diode_r_ohm: float = 1000.0
    load_r_ohm: float = 1e9
    duration_s: float = 0.2
    steps_per_electrical_cycle: int = 60
    diode_enabled: bool = True


@dataclass(frozen=True)
class Result:
    resonant_frequency_hz: float
    event_frequency_hz: float
    frequency_ratio: float
    parallel_loss_r_ohm: float
    ringdown_amplitude_tau_s: float
    event_period_s: float
    events: int
    conduction_windows: int
    max_resonator_v: float
    max_diode_current_a: float
    store_voltage_v: float
    pump_energy_j: float
    resonator_energy_j: float
    store_energy_j: float
    resonator_loss_j: float
    diode_loss_j: float
    load_energy_j: float
    energy_residual_j: float


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def resonant_frequency_hz(l_h: float, c_f: float) -> float:
    return 1.0 / (2.0 * math.pi * math.sqrt(_positive("l_h", l_h) * _positive("c_f", c_f)))


def parallel_resistance_for_q_ohm(l_h: float, c_f: float, q: float) -> float:
    return _positive("q", q) * math.sqrt(_positive("l_h", l_h) / _positive("c_f", c_f))


def ringdown_amplitude_tau_s(c_f: float, r_parallel_ohm: float) -> float:
    return 2.0 * _positive("r_parallel_ohm", r_parallel_ohm) * _positive("c_f", c_f)


def impulse_voltage_step_v(charge_c: float, c_f: float) -> float:
    return charge_c / _positive("c_f", c_f)


def _validate(p: Parameters) -> None:
    _positive("resonator_c_f", p.resonator_c_f)
    _positive("resonator_l_h", p.resonator_l_h)
    _positive("resonator_q", p.resonator_q)
    _positive("store_c_f", p.store_c_f)
    _positive("event_hz", p.event_hz)
    _positive("diode_r_ohm", p.diode_r_ohm)
    _positive("load_r_ohm", p.load_r_ohm)
    _positive("duration_s", p.duration_s)
    if p.steps_per_electrical_cycle < 20:
        raise ValueError("steps_per_electrical_cycle must be >= 20")
    if p.diode_drop_v < 0.0:
        raise ValueError("diode_drop_v must be >= 0")


def simulate(p: Parameters = Parameters()) -> Result:
    """Integrate a passive parallel-LC + one-way storage branch with exact impulse bookkeeping."""
    _validate(p)
    f0 = resonant_frequency_hz(p.resonator_l_h, p.resonator_c_f)
    rpar = parallel_resistance_for_q_ohm(p.resonator_l_h, p.resonator_c_f, p.resonator_q)
    tau = ringdown_amplitude_tau_s(p.resonator_c_f, rpar)
    dt = 1.0 / (f0 * p.steps_per_electrical_cycle)
    event_period = 1.0 / p.event_hz

    # state = v_res, i_L, v_store, E_Rloss, E_diode_loss, E_load
    y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    pump_energy = 0.0
    event_count = 0
    conduction_windows = 0
    was_conducting = False
    max_v = 0.0
    max_id = 0.0
    next_event = 0.0

    def diode_current(v_res: float, v_store: float) -> float:
        if not p.diode_enabled:
            return 0.0
        excess = v_res - v_store - p.diode_drop_v
        return max(excess / p.diode_r_ohm, 0.0)

    def deriv(state: list[float]) -> list[float]:
        v_res, i_l, v_store, _, _, _ = state
        i_d = diode_current(v_res, v_store)
        return [
            (-v_res / rpar - i_l - i_d) / p.resonator_c_f,
            v_res / p.resonator_l_h,
            (i_d - v_store / p.load_r_ohm) / p.store_c_f,
            v_res * v_res / rpar,
            i_d * (p.diode_drop_v + p.diode_r_ohm * i_d),
            v_store * v_store / p.load_r_ohm,
        ]

    def rk4(state: list[float], h: float) -> list[float]:
        k1 = deriv(state)
        s2 = [a + 0.5 * h * b for a, b in zip(state, k1)]
        k2 = deriv(s2)
        s3 = [a + 0.5 * h * b for a, b in zip(state, k2)]
        k3 = deriv(s3)
        s4 = [a + h * b for a, b in zip(state, k3)]
        k4 = deriv(s4)
        return [
            a + h * (b1 + 2.0 * b2 + 2.0 * b3 + b4) / 6.0
            for a, b1, b2, b3, b4 in zip(state, k1, k2, k3, k4)
        ]

    t = 0.0
    while t < p.duration_s - 1e-15:
        if next_event <= t + 1e-15:
            old_v = y[0]
            y[0] += impulse_voltage_step_v(p.impulse_charge_c, p.resonator_c_f)
            pump_energy += 0.5 * p.resonator_c_f * (y[0] * y[0] - old_v * old_v)
            event_count += 1
            next_event += event_period
            continue

        h = min(dt, p.duration_s - t)
        if next_event < t + h - 1e-15:
            h = next_event - t

        i_d = diode_current(y[0], y[2])
        conducting = i_d > 0.0
        if conducting and not was_conducting:
            conduction_windows += 1
        was_conducting = conducting
        max_v = max(max_v, abs(y[0]))
        max_id = max(max_id, i_d)
        y = rk4(y, h)
        t += h

    v_res, i_l, v_store, e_r, e_d, e_load = y
    e_res = 0.5 * p.resonator_c_f * v_res * v_res + 0.5 * p.resonator_l_h * i_l * i_l
    e_store = 0.5 * p.store_c_f * v_store * v_store
    residual = pump_energy - e_res - e_store - e_r - e_d - e_load

    return Result(
        resonant_frequency_hz=f0,
        event_frequency_hz=p.event_hz,
        frequency_ratio=f0 / p.event_hz,
        parallel_loss_r_ohm=rpar,
        ringdown_amplitude_tau_s=tau,
        event_period_s=event_period,
        events=event_count,
        conduction_windows=conduction_windows,
        max_resonator_v=max_v,
        max_diode_current_a=max_id,
        store_voltage_v=v_store,
        pump_energy_j=pump_energy,
        resonator_energy_j=e_res,
        store_energy_j=e_store,
        resonator_loss_j=e_r,
        diode_loss_j=e_d,
        load_energy_j=e_load,
        energy_residual_j=residual,
    )


def capacitance_threshold_sweep() -> list[tuple[float, Result]]:
    """Sweep effective resonator capacitance, analogous to a field/plate perturbation."""
    out: list[tuple[float, Result]] = []
    for scale in (0.8, 1.0, 1.1, 1.2, 1.4, 1.5, 1.6, 2.0):
        p = Parameters(
            resonator_c_f=10e-9 * scale,
            resonator_l_h=10e-3,
            impulse_charge_c=3e-9,
            duration_s=0.2,
        )
        out.append((scale, simulate(p)))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-diode", action="store_true")
    parser.add_argument("--sweep-capacitance", action="store_true")
    args = parser.parse_args()

    if args.sweep_capacitance:
        print("effective C perturbation / threshold sweep")
        print(f"{'C/C0':>6s} {'f0[Hz]':>12s} {'Vstore[V]':>12s} {'windows':>8s} {'Epump[J]':>12s} {'Estore[J]':>12s}")
        for scale, r in capacitance_threshold_sweep():
            print(f"{scale:6.2f} {r.resonant_frequency_hz:12.3f} {r.store_voltage_v:12.6g} {r.conduction_windows:8d} {r.pump_energy_j:12.6g} {r.store_energy_j:12.6g}")
        return 0

    p = Parameters(diode_enabled=not args.no_diode)
    r = simulate(p)
    print("M2 V4.26 two-time phase-memory / resonance / crystal-gate test")
    print(f"f0                 = {r.resonant_frequency_hz:.6g} Hz")
    print(f"event rate         = {r.event_frequency_hz:.6g} Hz")
    print(f"f0/event           = {r.frequency_ratio:.6g}")
    print(f"ringdown tau       = {r.ringdown_amplitude_tau_s:.6g} s")
    print(f"event period       = {r.event_period_s:.6g} s")
    print(f"events             = {r.events}")
    print(f"conduction windows = {r.conduction_windows}")
    print(f"max resonator V    = {r.max_resonator_v:.6g} V")
    print(f"store V            = {r.store_voltage_v:.6g} V")
    print(f"pump energy        = {r.pump_energy_j:.9g} J")
    print(f"store energy       = {r.store_energy_j:.9g} J")
    print(f"resonator loss     = {r.resonator_loss_j:.9g} J")
    print(f"diode loss         = {r.diode_loss_j:.9g} J")
    print(f"load energy        = {r.load_energy_j:.9g} J")
    print(f"final resonator E  = {r.resonator_energy_j:.9g} J")
    print(f"energy residual    = {r.energy_residual_j:.9g} J")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
