#!/usr/bin/env python3
"""M2-V4.6: radioactive-ionization gate bounds.

Purpose: test whether a weak radioactive inclusion could plausibly act as an air-ionization
bias/gating element in a very high-impedance electrostatic circuit.

This model does NOT treat radioactivity as a 100 W-class power source and does NOT provide
instructions for handling radioactive material. Use simulation or non-radioactive laboratory
surrogates for replication work.
"""
from __future__ import annotations

import argparse

E_CHARGE_C = 1.602176634e-19
EV_TO_J = E_CHARGE_C
W_AIR_EV_PER_PAIR = 33.97  # mean energy per ion pair in dry air


def decay_power_w(activity_bq: float, deposited_energy_mev_per_decay: float) -> float:
    if activity_bq < 0 or deposited_energy_mev_per_decay < 0:
        raise ValueError("activity and energy must be non-negative")
    return activity_bq * deposited_energy_mev_per_decay * 1e6 * EV_TO_J


def saturation_ion_current_a(
    activity_bq: float,
    deposited_energy_mev_per_decay: float,
    collection_efficiency: float = 1.0,
) -> float:
    """Ideal radiation-limited ion-chamber current.

    Assumes the specified decay energy is actually deposited in the gas and the stated
    fraction of ion pairs is collected rather than recombined/lost to walls.
    """
    if not (0.0 <= collection_efficiency <= 1.0):
        raise ValueError("collection efficiency must be between 0 and 1")
    p = decay_power_w(activity_bq, deposited_energy_mev_per_decay)
    # W_air/e = 33.97 J/C, numerically identical to 33.97 eV per ion pair.
    return collection_efficiency * p / W_AIR_EV_PER_PAIR


def voltage_ramp_v_s(current_a: float, capacitance_f: float) -> float:
    if capacitance_f <= 0:
        raise ValueError("capacitance must be positive")
    return current_a / capacitance_f


def charge_per_revolution_c(current_a: float, rpm: float) -> float:
    if rpm <= 0:
        raise ValueError("rpm must be positive")
    return current_a * 60.0 / rpm


def voltage_per_revolution_v(current_a: float, capacitance_f: float, rpm: float) -> float:
    return charge_per_revolution_c(current_a, rpm) / capacitance_f


def activity_required_for_ion_current_bq(
    target_current_a: float,
    deposited_energy_mev_per_decay: float,
    collection_efficiency: float = 1.0,
) -> float:
    if target_current_a < 0 or deposited_energy_mev_per_decay <= 0:
        raise ValueError("target current non-negative and decay energy positive")
    if not (0.0 < collection_efficiency <= 1.0):
        raise ValueError("collection efficiency must be >0 and <=1")
    current_per_bq = saturation_ion_current_a(1.0, deposited_energy_mev_per_decay, collection_efficiency)
    return target_current_a / current_per_bq


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--activity-bq", type=float, default=10_000.0)
    p.add_argument("--energy-mev", type=float, default=5.0)
    p.add_argument("--eta", type=float, default=1.0)
    p.add_argument("--cap-pf", type=float, default=100.0)
    p.add_argument("--rpm", type=float, default=15.0)
    args = p.parse_args()

    i = saturation_ion_current_a(args.activity_bq, args.energy_mev, args.eta)
    pw = decay_power_w(args.activity_bq, args.energy_mev)
    c = args.cap_pf * 1e-12
    print("M2-V4.6 radioactive-ionization gate bound")
    print("Radioactivity is modeled as an ionization/gating source, not bulk output power.")
    print(f"activity                 = {args.activity_bq:.6g} Bq")
    print(f"deposited energy/decay   = {args.energy_mev:.6g} MeV")
    print(f"radiation power          = {pw:.6g} W")
    print(f"ideal saturation current = {i:.6g} A")
    print(f"dV/dt on {args.cap_pf:g} pF      = {voltage_ramp_v_s(i, c):.6g} V/s")
    print(f"dV/rev at {args.rpm:g} rpm       = {voltage_per_revolution_v(i, c, args.rpm):.6g} V/rev")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
