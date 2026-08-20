#!/usr/bin/env python3
"""M2 V4.27 reservoir-isolation and source-scale calculator.

This module does not assume an anomalous source. It separates tracked output,
storage change and losses from independently measured/upper-bounded inputs, then
computes the unresolved residual and the source scale that any missing reservoir
would have to supply.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import math


def _positive(name: str, value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return value


def _nonnegative(name: str, value: float) -> float:
    if value < 0.0:
        raise ValueError(f"{name} must be >= 0")
    return value


@dataclass(frozen=True)
class EnergyBudget:
    """Energy terms over one common measurement interval.

    All input fields are positive when they deliver energy into the apparatus.
    `delta_stored_j` is signed: positive means net storage gain, negative means
    stored energy was released during the interval.
    """

    load_j: float
    delta_stored_j: float
    losses_j: float
    mechanical_in_j: float = 0.0
    bias_in_j: float = 0.0
    rf_in_j: float = 0.0
    thermal_in_j: float = 0.0
    atmospheric_in_j: float = 0.0
    chemical_in_j: float = 0.0

    @property
    def demand_j(self) -> float:
        return self.load_j + self.delta_stored_j + self.losses_j

    @property
    def known_input_j(self) -> float:
        return (
            self.mechanical_in_j
            + self.bias_in_j
            + self.rf_in_j
            + self.thermal_in_j
            + self.atmospheric_in_j
            + self.chemical_in_j
        )

    @property
    def residual_j(self) -> float:
        return self.demand_j - self.known_input_j


def rss_uncertainty_j(*one_sigma_terms_j: float) -> float:
    """Root-sum-square independent 1-sigma absolute energy uncertainties."""
    for i, value in enumerate(one_sigma_terms_j):
        _nonnegative(f"uncertainty[{i}]", value)
    return math.sqrt(sum(value * value for value in one_sigma_terms_j))


def residual_significance_sigma(residual_j: float, sigma_j: float) -> float:
    _nonnegative("sigma_j", sigma_j)
    if sigma_j == 0.0:
        if residual_j > 0.0:
            return math.inf
        if residual_j < 0.0:
            return -math.inf
        return 0.0
    return residual_j / sigma_j


def energy_per_event_j(power_w: float, event_rate_hz: float) -> float:
    return _nonnegative("power_w", power_w) / _positive("event_rate_hz", event_rate_hz)


def source_current_for_power_a(power_w: float, source_voltage_v: float) -> float:
    return _nonnegative("power_w", power_w) / _positive("source_voltage_v", source_voltage_v)


def charge_per_event_c(power_w: float, event_rate_hz: float, transfer_voltage_v: float) -> float:
    """Minimum transferred charge/event if E_event = V * deltaQ at fixed V."""
    return energy_per_event_j(power_w, event_rate_hz) / _positive("transfer_voltage_v", transfer_voltage_v)


def capacitor_voltage_for_event_energy_v(power_w: float, event_rate_hz: float, capacitance_f: float) -> float:
    """Voltage whose 1/2 C V^2 equals the required energy per event."""
    e = energy_per_event_j(power_w, event_rate_hz)
    c = _positive("capacitance_f", capacitance_f)
    return math.sqrt(2.0 * e / c)


def capacitor_charge_for_event_energy_c(power_w: float, event_rate_hz: float, capacitance_f: float) -> float:
    c = _positive("capacitance_f", capacitance_f)
    return c * capacitor_voltage_for_event_energy_v(power_w, event_rate_hz, c)


def impulse_energy_j(impulse_charge_c: float, capacitance_f: float) -> float:
    q = _nonnegative("impulse_charge_c", impulse_charge_c)
    c = _positive("capacitance_f", capacitance_f)
    return q * q / (2.0 * c)


def scale_gap(required_event_energy_j: float, reference_event_energy_j: float) -> float:
    return _nonnegative("required_event_energy_j", required_event_energy_j) / _positive(
        "reference_event_energy_j", reference_event_energy_j
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event-rate", type=float, default=50.0)
    parser.add_argument("--transfer-voltage", type=float, default=100e3)
    parser.add_argument("--resonator-c", type=float, default=10e-9)
    parser.add_argument("--reference-impulse-charge", type=float, default=10e-9)
    args = parser.parse_args()

    f = _positive("event_rate", args.event_rate)
    v = _positive("transfer_voltage", args.transfer_voltage)
    c = _positive("resonator_c", args.resonator_c)
    q_ref = _nonnegative("reference_impulse_charge", args.reference_impulse_charge)
    e_ref = impulse_energy_j(q_ref, c)

    print("M2 V4.27 reservoir isolation / missing-source scale")
    print(f"event rate = {f:.6g} Hz")
    print(f"transfer voltage = {v:.6g} V")
    print(f"reference impulse = {q_ref:.6g} C into C={c:.6g} F -> {e_ref:.6g} J/event")
    print()
    print(f"{'target P[W]':>12s} {'E/event[J]':>14s} {'I@V[A]':>12s} {'Q/event[C]':>14s} {'C-voltage[V]':>14s} {'gap/ref':>14s}")
    for power in (1.0, 100.0, 300.0, 3000.0):
        e_event = energy_per_event_j(power, f)
        print(
            f"{power:12.6g} {e_event:14.6g} "
            f"{source_current_for_power_a(power, v):12.6g} "
            f"{charge_per_event_c(power, f, v):14.6g} "
            f"{capacitor_voltage_for_event_energy_v(power, f, c):14.6g} "
            f"{scale_gap(e_event, e_ref):14.6g}"
        )

    # V4.26 numerical bookkeeping example.
    closed = EnergyBudget(
        load_j=1.484e-11,
        delta_stored_j=7.672e-9,
        losses_j=2.2676e-8 + 1.9637e-8,
        mechanical_in_j=5.000e-8,
    )
    print("\nV4.26 bookkeeping example")
    print(f"demand = {closed.demand_j:.6g} J")
    print(f"known input = {closed.known_input_j:.6g} J")
    print(f"residual = {closed.residual_j:.6g} J (rounding-level mismatch expected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
