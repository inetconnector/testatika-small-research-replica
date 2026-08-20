from sim.m2_v4_29_surface_redox_reservoir import (
    aluminum_oxygen_mass_kg,
    required_area_m2,
    required_fuel_mass_kg,
)


def test_humidity_area_scale():
    assert abs(required_area_m2(100.0, 6.7) - 14.9253731343) < 1e-9
    assert abs(required_area_m2(3000.0, 6.7) - 447.76119403) < 1e-8


def test_al_air_mass_scale():
    # 100 W for 1 h at 1878 Wh/kg practical comparison.
    assert abs(required_fuel_mass_kg(100.0, 3600.0, 1878.0) - 0.0532481363) < 1e-10
    # 3 kW for 10 min.
    assert abs(required_fuel_mass_kg(3000.0, 600.0, 1878.0) - 0.2662406816) < 1e-10


def test_oxygen_stoichiometry_positive_and_large():
    m_al = required_fuel_mass_kg(100.0, 3600.0, 1878.0)
    m_o2 = aluminum_oxygen_mass_kg(m_al)
    assert 0.047 < m_o2 < 0.048
