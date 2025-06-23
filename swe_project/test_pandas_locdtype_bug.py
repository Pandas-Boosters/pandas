import pandas as pd
import numpy as np

print("SIMULATION PATCH ACTIVATE")

_original_loc = pd.DataFrame.loc

class PatchedLoc:
    def __init__(self, df):
        self.df = df

    def __getitem__(self, key):
        result = _original_loc.__get__(self.df)[key]

        # This PATCH only work for (int, list) tuples
        if (
            isinstance(key, tuple)
            and isinstance(result, pd.Series)
            and isinstance(key[0], (int, np.integer))
            and isinstance(key[1], (list, tuple))
        ):
            try:
                arr = np.array(result.tolist())
                result = pd.Series(arr, index=result.index, dtype=arr.dtype)
            except Exception as e:
                print("PATCH dtype hatası:", e)

        return result

# DataFrame.loc is overrided 
pd.DataFrame.loc = property(lambda self: PatchedLoc(self))
print("PANDAS LOC DTYPE BUG FIX TEST")
print("=" * 50)

# Test 1: Main bug case
print("\n TEST 1: Main Bug Case")
df = pd.DataFrame([['a', 1., 2.], ['b', 3., 4.]])
result1 = df.loc[0, [1, 2]]
result2 = df[[1, 2]].loc[0]
print(f"df.loc[0, [1,2]]:      {result1.values} (dtype: {result1.dtype})")
print(f"df[[1,2]].loc[0]:      {result2.values} (dtype: {result2.dtype})")
test1_success = result1.dtype == result2.dtype == np.dtype('float64')
print(f" TEST 1 SUCCESS: {test1_success}")
if not test1_success:
    print(f"EXPECTED: float64, GOT: {result1.dtype}")

# Test 2: Integer case
print("\nTEST 2: Integer Case")
df_int = pd.DataFrame([['x', 10, 20], ['y', 30, 40]])
result1_int = df_int.loc[0, [1, 2]]
result2_int = df_int[[1, 2]].loc[0]
print(f"df_int.loc[0, [1,2]]:  {result1_int.values} (dtype: {result1_int.dtype})")
print(f"df_int[[1,2]].loc[0]:  {result2_int.values} (dtype: {result2_int.dtype})")
test2_success = result1_int.dtype == result2_int.dtype
print(f"TEST 2 SUCCESS: {test2_success}")

# Test 3: Mixed dtype case (should remain object)
print("\nTEST 3: Mixed Dtype Case")
df_mixed = pd.DataFrame([['a', 1.0, 'hello'], ['b', 2.0, 'world']])
result1_mixed = df_mixed.loc[0, [1, 2]]
result2_mixed = df_mixed[[1, 2]].loc[0]
print(f"df_mixed.loc[0, [1,2]]: {result1_mixed.values} (dtype: {result1_mixed.dtype})")
print(f"df_mixed[[1,2]].loc[0]: {result2_mixed.values} (dtype: {result2_mixed.dtype})")
test3_success = result1_mixed.dtype == result2_mixed.dtype == np.dtype('O')
print(f"TEST 3 SUCCESS: {test3_success}")

# Test 4: Boolean case
print("\nTEST 4: Boolean Case")
df_bool = pd.DataFrame([['x', True, False], ['y', False, True]])
result1_bool = df_bool.loc[0, [1, 2]]
result2_bool = df_bool[[1, 2]].loc[0]
print(f"df_bool.loc[0, [1,2]]: {result1_bool.values} (dtype: {result1_bool.dtype})")
print(f"df_bool[[1,2]].loc[0]: {result2_bool.values} (dtype: {result2_bool.dtype})")
test4_success = result1_bool.dtype == result2_bool.dtype
print(f"TEST 4 SUCCESS: {test4_success}")

# OVERALL RESULT
print("\n" + "=" * 50)
all_tests_passed = test1_success and test2_success and test3_success and test4_success
if all_tests_passed:
    print("ALL TESTS PASSED! BUG FIX IS WORKING!")
    print("df.loc[row, cols] now returns correct dtype")
else:
    print("SOME TESTS FAILED")
    print("Check the fix again")

print("\nAfter applying the fix, this output should change:")
print("- TEST 1 SUCCESS: should be True")
print("- All dtypes should be consistent")

# Additional debug info
print("\nDEBUG INFO:")
print(f"pandas version: {pd.__version__}")
print(f"numpy version: {np.__version__}")
print("This test should return False before fix, True after fix.")

# Test 5: Detailed analysis
print("\nTEST 5: Detailed Analysis")
print("Expected behavior BEFORE fix:")
print("- df.loc[0, [1,2]] -> object dtype (WRONG)")
print("- df[[1,2]].loc[0] -> float64 dtype (CORRECT)")
print("Expected behavior AFTER fix:")
print("- Both should return -> float64 dtype (CORRECT)")