import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO



    # 1. TEST: İçinde string olan bir veri
print("--- 1. Test: Data with string ---")
df_string = pd.DataFrame({'id': [1, 2], 'comment': ['a', 'b']})
buffer = BytesIO()
df_string.to_parquet(buffer)
buffer.seek(0)

    # read and check the result
    # expectation: the logic should work and the dtype should be 'pyarrow'
test_df_1 = pd.read_parquet(buffer, dtype_backend='pyarrow') # let's directly simulate the code
print("Read DataFrame's comment column type:", test_df_1['comment'].dtype)
if "pyarrow" in str(test_df_1['comment'].dtype):
        print("RESULT: SUCCESS! String column read as pyarrow.\n")
else:
        print("RESULT: FAILED! String column not read as pyarrow.\n")


    # 2. TEST: Data without string
print("--- 2. Test: Data without string ---")
df_no_string = pd.DataFrame({'id': [1, 2], 'value': [10.1, 20.2]})
buffer_no_string = BytesIO()
df_no_string.to_parquet(buffer_no_string)
buffer_no_string.seek(0)

    # read and check the result
    # expectation: the logic should work and the dtype should be 'pyarrow'
test_df_2 = pd.read_parquet(buffer_no_string)
print("Read DataFrame's value column type:", test_df_2['value'].dtype)
if "pyarrow" not in str(test_df_2['value'].dtype):
        print("RESULT: SUCCESS! String-less column kept its normal dtype.\n")
else:
        print("RESULT: FAILED! String-less column read as pyarrow.\n")
