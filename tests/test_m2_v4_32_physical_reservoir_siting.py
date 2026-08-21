import pytest

from sim.m2_v4_32_physical_reservoir_siting import (
    canonical_site_volumes_l,
    dielectric_energy_j,
    energy_density_wh_l,
    multilayer_parallel_capacitance_f,
    stored_energy_j,
)


def test_m2_and_m6_envelope_scales():
    sites = canonical_site_volumes_l()
    assert sites["M2 two side-pot external envelopes"] == pytest.approx(1.2191892770)
    assert sites["M2 top-carrier bounding box"] == pytest.approx(0.08568)
    assert sites["M6 two large-cylinder external envelopes"] == pytest.approx(7.8685272080)
    assert sites["M6 two capacitor-can external envelopes"] == pytest.approx(0.8129310814)
    assert sites["M6 base gross working envelope"] == pytest.approx(7.2352)


def test_required_density_separates_burst_from_continuous_claim():
    sites = canonical_site_volumes_l()
    base_l = sites["M6 base gross working envelope"]
    assert energy_density_wh_l(10000.0 / 3600.0, base_l) == pytest.approx(0.3839255)
    assert energy_density_wh_l(1500.0, base_l) == pytest.approx(207.3197700)


def test_m6_large_cylinder_volume_is_large_enough_for_low_density_finite_store_geometry():
    sites = canonical_site_volumes_l()
    cyl_l = sites["M6 two large-cylinder external envelopes"]
    assert energy_density_wh_l(1500.0, cyl_l) == pytest.approx(190.6328796)


def test_even_ideal_dielectric_filling_both_m6_can_envelopes_is_far_below_10kj():
    sites = canonical_site_volumes_l()
    caps_l = sites["M6 two capacitor-can external envelopes"]
    # Deliberately optimistic: every cubic millimetre is er=3 active dielectric at 100 MV/m.
    e_j = dielectric_energy_j(caps_l, 3.0, 100e6)
    assert e_j == pytest.approx(107.9676671)
    assert e_j < 10000.0 / 90.0


def test_favourable_20_sheet_stack_remains_small_at_field_limited_example():
    c = multilayer_parallel_capacitance_f(20, 0.078, 1e-3, er=3.0)
    assert c == pytest.approx(2.4115855464e-9)
    # 30 MV/m across 1 mm corresponds to 30 kV terminal voltage for the parallel-gap model.
    e = stored_energy_j(c, 30e3)
    assert e == pytest.approx(1.0852134959)
    assert e < 2.0
