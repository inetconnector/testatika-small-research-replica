#!/usr/bin/env python3
"""V4.15 electrically-small resonant effective-aperture bounds.

A subtle loophole in simple physical-area arguments is that a matched receiving
antenna can have an effective aperture much larger than its geometric area,
especially when wavelength is enormous.  V4.15 tests that loophole against the
fundamental Q/bandwidth/ring-up cost of an electrically small passive receiver.

The calculations are deliberately optimistic: free-space propagation, perfect
polarization, ideal conjugate match, no material loss, and a dipole-like gain.
They are therefore upper-bound diagnostics, not a historical M2 circuit claim.
"""

from __future__ import annotations

import math

C0 = 299_792_458.0
SECONDS_PER_YEAR = 365.25 * 24.0 * 3600.0


def _positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def wavelength_m(frequency_hz: float) -> float:
    _positive(frequency_hz, "frequency_hz")
    return C0 / frequency_hz


def electrical_size_ka(radius_m: float, frequency_hz: float) -> float:
    _positive(radius_m, "radius_m")
    return 2.0 * math.pi * radius_m / wavelength_m(frequency_hz)


def chu_mclean_q_bound(radius_m: float, frequency_hz: float) -> float:
    """Single-mode electrically-small antenna radiation-Q lower-bound scale.

    Uses the familiar TM10/TE10 small-antenna expression
    Q >= 1/(ka)^3 + 1/(ka).  For ka << 1 the cubic term dominates.
    """
    ka = electrical_size_ka(radius_m, frequency_hz)
    return 1.0 / ka**3 + 1.0 / ka


def amplitude_time_constant_s(q_factor: float, frequency_hz: float) -> float:
    """Approximate amplitude e-folding time tau ~= Q/(pi*f)."""
    _positive(q_factor, "q_factor")
    _positive(frequency_hz, "frequency_hz")
    return q_factor / (math.pi * frequency_hz)


def half_power_bandwidth_hz(q_factor: float, frequency_hz: float) -> float:
    """Narrow-resonance bandwidth scale Delta f ~= f/Q."""
    _positive(q_factor, "q_factor")
    _positive(frequency_hz, "frequency_hz")
    return frequency_hz / q_factor


def ideal_effective_aperture_m2(frequency_hz: float, gain_linear: float = 1.5) -> float:
    """Matched far-field receiving aperture A_e = G*lambda^2/(4*pi).

    This is a steady-state reciprocal antenna result.  It does not include the
    Q, efficiency, coherence-time, or finite-source back-reaction penalties.
    """
    _positive(gain_linear, "gain_linear")
    lam = wavelength_m(frequency_hz)
    return gain_linear * lam**2 / (4.0 * math.pi)


def plane_wave_power_density_w_m2(e_rms_v_m: float) -> float:
    """Free-space plane-wave flux S = E_rms^2/Z0."""
    _positive(e_rms_v_m, "e_rms_v_m")
    z0 = 376.730313668
    return e_rms_v_m**2 / z0


def ideal_available_power_w(
    e_rms_v_m: float,
    frequency_hz: float,
    gain_linear: float = 1.5,
    radiation_efficiency: float = 1.0,
) -> float:
    """Optimistic steady-state far-field available power S*A_e*eta."""
    if radiation_efficiency <= 0 or radiation_efficiency > 1:
        raise ValueError("radiation_efficiency must be in (0, 1]")
    return (
        plane_wave_power_density_w_m2(e_rms_v_m)
        * ideal_effective_aperture_m2(frequency_hz, gain_linear)
        * radiation_efficiency
    )


def q_allowed_by_settle_time(frequency_hz: float, settle_time_s: float) -> float:
    """Q whose amplitude time constant equals settle_time_s."""
    _positive(frequency_hz, "frequency_hz")
    _positive(settle_time_s, "settle_time_s")
    return math.pi * frequency_hz * settle_time_s


def q_time_gap(radius_m: float, frequency_hz: float, settle_time_s: float) -> float:
    """Fundamental Q divided by Q compatible with the requested response time."""
    return chu_mclean_q_bound(radius_m, frequency_hz) / q_allowed_by_settle_time(
        frequency_hz, settle_time_s
    )


def radiation_resistance_short_dipole_ohm(length_m: float, frequency_hz: float) -> float:
    """Short uniform-current dipole radiation resistance scale 80*pi^2*(l/lambda)^2."""
    _positive(length_m, "length_m")
    lam = wavelength_m(frequency_hz)
    return 80.0 * math.pi**2 * (length_m / lam) ** 2


def max_loss_resistance_for_efficiency(radiation_resistance_ohm: float, efficiency: float) -> float:
    """Loss resistance compatible with eta=Rrad/(Rrad+Rloss)."""
    _positive(radiation_resistance_ohm, "radiation_resistance_ohm")
    if efficiency <= 0 or efficiency >= 1:
        raise ValueError("efficiency must be in (0, 1)")
    return radiation_resistance_ohm * (1.0 / efficiency - 1.0)


def years(seconds: float) -> float:
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    return seconds / SECONDS_PER_YEAR


def summary_row(radius_m: float, frequency_hz: float) -> dict[str, float]:
    q = chu_mclean_q_bound(radius_m, frequency_hz)
    return {
        "frequency_hz": frequency_hz,
        "wavelength_m": wavelength_m(frequency_hz),
        "ka": electrical_size_ka(radius_m, frequency_hz),
        "q_min": q,
        "bandwidth_hz": half_power_bandwidth_hz(q, frequency_hz),
        "tau_s": amplitude_time_constant_s(q, frequency_hz),
        "tau_years": years(amplitude_time_constant_s(q, frequency_hz)),
        "ideal_ae_m2": ideal_effective_aperture_m2(frequency_hz),
    }


def main() -> None:
    radius = 0.1
    print("V4.15 electrically-small resonant effective-aperture bounds")
    print("radius = 0.1 m; ideal dipole gain = 1.5; free-space/matched/lossless upper bounds")
    for f in (2.5e-3, 7.83, 24.0, 50.0, 1e3, 10e3, 100e3, 1e6):
        row = summary_row(radius, f)
        print(
            f"f={f:g} Hz  ka={row['ka']:.6g}  Qmin={row['q_min']:.6g}  "
            f"BW={row['bandwidth_hz']:.6g} Hz  tau={row['tau_years']:.6g} y  "
            f"Ae_ideal={row['ideal_ae_m2']:.6g} m^2"
        )

    # A Schumann-like electric-field example is intentionally used only to
    # expose the misleading steady-state aperture result.  The associated Q
    # makes that state unreachable on any practical source-coherence timescale.
    f_sr = 7.83
    e_sr = 0.2e-3
    p_ideal = ideal_available_power_w(e_sr, f_sr)
    q_min = chu_mclean_q_bound(radius, f_sr)
    print(f"Schumann-like free-space steady-state ideal P at E=0.2 mV/m: {p_ideal:.6g} W")
    print(f"but Qmin={q_min:.6g}, tau={years(amplitude_time_constant_s(q_min, f_sr)):.6g} years")
    print(f"Q gap versus 60-s response: {q_time_gap(radius, f_sr, 60.0):.6g}x")

    # Show why enormous theoretical effective aperture does not rescue a
    # practical 20-cm ELF receiver: radiation resistance is vanishingly small.
    rrad = radiation_resistance_short_dipole_ohm(0.2, f_sr)
    print(f"0.2-m short-dipole Rrad at 7.83 Hz: {rrad:.6g} ohm")
    print(f"Rloss allowed for 50% radiation efficiency: {max_loss_resistance_for_efficiency(rrad, 0.5):.6g} ohm")


if __name__ == "__main__":
    main()
