"""Tests for the matrix CLI (src/backend/cli.py)."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "backend"))

import pytest
from backend.cli import parse_positive_int, build_random_matrix


class TestParsePositiveInt:
    def test_valid_positive_integer(self):
        assert parse_positive_int("5", "rows") == 5

    def test_rejects_zero(self):
        with pytest.raises(ValueError):
            parse_positive_int("0", "rows")

    def test_rejects_negative(self):
        with pytest.raises(ValueError):
            parse_positive_int("-3", "rows")

    def test_rejects_non_numeric(self):
        with pytest.raises(ValueError):
            parse_positive_int("abc", "rows")

    def test_rejects_float_string(self):
        with pytest.raises(ValueError):
            parse_positive_int("3.5", "rows")


class TestBuildRandomMatrix:
    def test_correct_shape(self):
        matrix = build_random_matrix(4, 6)
        assert matrix.matrix.shape == (4, 6)

    def test_values_within_range(self):
        matrix = build_random_matrix(5, 5, low=1, high=10)
        assert matrix.matrix.min() >= 1
        assert matrix.matrix.max() < 10

    def test_single_cell_matrix(self):
        matrix = build_random_matrix(1, 1)
        assert matrix.matrix.shape == (1, 1)

    def test_different_calls_produce_different_matrices(self):
        m1 = build_random_matrix(5, 5)
        m2 = build_random_matrix(5, 5)
        # Extremely unlikely two random 5x5 matrices are identical
        assert not (m1.matrix == m2.matrix).all()
