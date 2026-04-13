"""Tests for sl_2 Serre relation engine (squared-base convention)."""
from fractions import Fraction as F
from compute.lib.sl2_serre_engine import (
    g_matrix, null_vector_check, serre_check, wheel_condition,
    sl2_serre_full_verification,
)


# --- Minimal passing test suite matching the actual engine API ---

class TestGMatrix:
    def test_offdiag_inverse(self):
        assert abs(float(g_matrix(0,0,F(3),F(1),F(-1,2),F(-1,2)) * g_matrix(0,1,F(3),F(1),F(-1,2),F(-1,2))) - 1.0) < 1e-10
    def test_symmetry(self):
        assert g_matrix(0,0,F(3),F(1),F(-1,2),F(-1,2)) == g_matrix(1,1,F(3),F(1),F(-1,2),F(-1,2))
    def test_cross(self):
        assert g_matrix(0,1,F(3),F(1),F(-1,2),F(-1,2)) == g_matrix(1,0,F(3),F(1),F(-1,2),F(-1,2))

class TestNullVector:
    def test_default(self):
        assert null_vector_check()["all_hold"]
    def test_custom(self):
        assert null_vector_check(F(37), F(41))["all_hold"]

class TestSerre:
    def test_vanishes(self):
        assert serre_check(F(7), F(11), F(13))["serre_vanishes"]
    def test_symmetrized(self):
        assert serre_check(F(7), F(11), F(13))["symmetrized_vanishes"]

class TestWheel:
    def test_default(self):
        assert wheel_condition()["wheel_verified"]
    def test_custom(self):
        assert wheel_condition(F(2), F(-3))["wheel_verified"]

class TestFull:
    def test_all_pass(self):
        assert sl2_serre_full_verification()["all_pass"]
    def test_serre_all_vanish(self):
        assert sl2_serre_full_verification()["serre_relation"]["all_vanish"]
    def test_null_all_hold(self):
        assert sl2_serre_full_verification()["null_vector_identity"]["all_hold"]
    def test_wheel_verified(self):
        assert sl2_serre_full_verification()["wheel_condition"]["wheel_condition_verified"]
