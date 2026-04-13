from fractions import Fraction

from compute.lib.scattering_diagram import s3_orbit_table, scattering_diagram_walls


def test_scattering_diagram_seed_walls_and_first_symmetric_root():
    walls = scattering_diagram_walls(4)

    assert walls[(1, 0, 0)] == Fraction(1)
    assert walls[(0, 1, 0)] == Fraction(1)
    assert walls[(0, 0, 1)] == Fraction(1)
    assert walls[(1, 1, 1)] == Fraction(8, 3)


def test_scattering_diagram_orbit_table_has_expected_seed_orbits():
    orbits = s3_orbit_table(4)
    height_one = next(orbit for orbit in orbits if orbit["representative"] == (0, 0, 1))
    diagonal = next(orbit for orbit in orbits if orbit["representative"] == (1, 1, 1))

    assert height_one["all_same"]
    assert height_one["orbit_size"] == 3
    assert diagonal["orbit_size"] == 1
