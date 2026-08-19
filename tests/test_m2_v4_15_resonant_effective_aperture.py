import pytest

from sim.m2_v4_15_resonant_effective_aperture import (
    amplitude_time_constant_s,
    chu_mclean_q_bound,
    electrical_size_ka,
    half_power_bandwidth_hz,
    ideal_available_power_w,
    ideal_effective_aperture_m2,
    max_loss_resistance_for_efficiency,
    q_time_gap,
    radiation_resistance_short_dipole_ohm,
    wavelength_m,
    years,
)


def test_2_5_mhz_magnetospheric_wavelength_is_120_million_km():
    assert wavelength_m(2.5e-3) == pytest.approx(1.199169832e11)


def test_20cm_receiver_is_extremely_electrically_small_at_pc5_frequency():
    assert electrical_size_ka(0.1, 2.5e-3) == pytest.approx(5.2396125549e-12)


def test_chu_mclean_q_at_pc5_is_about_7e33():
    q = chu_mclean_q_bound(0.1, 2.5e-3)
    assert q == pytest.approx(6.9518833739e33)


def test_pc5_q_implies_absurd_ringup_time():
    q = chu_mclean_q_bound(0.1, 2.5e-3)
    assert years(amplitude_time_constant_s(q, 2.5e-3)) == pytest.approx(2.8048434678e28)


def test_schumann_7_83hz_q_is_about_2e23():
    q = chu_mclean_q_bound(0.1, 7.83)
    assert q == pytest.approx(2.2627533552e23)
    assert years(amplitude_time_constant_s(q, 7.83)) == pytest.approx(2.9148862775e14)


def test_schumann_ideal_effective_aperture_is_huge_but_steady_state_only():
    assert ideal_effective_aperture_m2(7.83) == pytest.approx(1.7498437746e14)


def test_schumann_receiver_bandwidth_is_effectively_zero():
    q = chu_mclean_q_bound(0.1, 7.83)
    assert half_power_bandwidth_hz(q, 7.83) == pytest.approx(3.460385986e-23)


def test_schumann_q_gap_for_one_minute_response_is_twenty_orders():
    assert q_time_gap(0.1, 7.83, 60.0) == pytest.approx(1.5332510549e20)


def test_naive_free_space_aperture_can_predict_large_power_and_is_therefore_not_enough():
    # This intentionally demonstrates the loophole: steady-state A_e alone can
    # suggest kilowatt-scale available power. The Q/ring-up tests above show why
    # this state cannot be established by a 20-cm passive ELF receiver.
    p = ideal_available_power_w(0.2e-3, 7.83)
    assert p == pytest.approx(18579.465716, rel=1e-6)


def test_radiation_resistance_at_7_83hz_is_tens_of_femto_ohms():
    rrad = radiation_resistance_short_dipole_ohm(0.2, 7.83)
    assert rrad == pytest.approx(2.1544272917e-14)
    assert max_loss_resistance_for_efficiency(rrad, 0.5) == pytest.approx(rrad)


def test_frequency_transition_shows_why_mhz_is_different_from_elf():
    q_10khz = chu_mclean_q_bound(0.1, 10e3)
    q_100khz = chu_mclean_q_bound(0.1, 100e3)
    q_1mhz = chu_mclean_q_bound(0.1, 1e6)
    assert years(amplitude_time_constant_s(q_10khz, 10e3)) == pytest.approx(109.5641980)
    assert years(amplitude_time_constant_s(q_100khz, 100e3)) == pytest.approx(0.01095642028)
    assert amplitude_time_constant_s(q_1mhz, 1e6) == pytest.approx(34.5752076, rel=1e-6)
