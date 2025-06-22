import pandas as pd
import pytest

# ✅ Existing test for mixed types error
def test_dropna_mixed_types_error():
    df = pd.DataFrame({"A": [1, "two", None]})  # Mixed types in one column
    with pytest.raises(TypeError, match="dropna.*uniform column types"):
        df.dropna()

# ✅ Safe Test 1: dropna on uniform types, default settings
def test_dropna_uniform_column():
    df = pd.DataFrame({"A": [1, 2, None], "B": [3, 4, 5]})
    result = df.dropna()
    expected = pd.DataFrame({"A": [1.0, 2.0], "B": [3, 4]}, index=[0, 1])
    pd.testing.assert_frame_equal(result, expected)

# ✅ Safe Test 2: dropna(axis=1) to drop all-NaN columns
def test_dropna_axis1():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [None, None, None],
        "C": [4, 5, 6]
    })
    result = df.dropna(axis=1)
    expected = pd.DataFrame({
        "A": [1, 2, 3],
        "C": [4, 5, 6]
    })
    pd.testing.assert_frame_equal(result, expected)

# ✅ Safe Test 3: dropna with subset on clean data
def test_dropna_with_subset():
    df = pd.DataFrame({
        "A": [1, None, 3],
        "B": [4, 5, 6],
        "C": [None, None, 9]
    })
    result = df.dropna(subset=["A"])
    expected = pd.DataFrame({
        "A": [1.0, 3.0],
        "B": [4, 6],
        "C": [None, 9]
    }, index=[0, 2])
    pd.testing.assert_frame_equal(result, expected)
