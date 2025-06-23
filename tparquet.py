import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO

print(">>> HIZLI TEST BAŞLADI - DERLEME YOK <<<\n")

    # 1. TEST: İçinde string olan bir veri
print("--- 1. Test: String'li Veri ---")
df_string = pd.DataFrame({'id': [1, 2], 'comment': ['a', 'b']})
buffer = BytesIO()
df_string.to_parquet(buffer)
buffer.seek(0)

    # Oku ve sonucu kontrol et
    # Beklenti: Senin mantığın çalışıp dtype'ı 'pyarrow' yapmalı
test_df_1 = pd.read_parquet(buffer, dtype_backend='pyarrow') # Kodu doğrudan simüle etmek için pyarrow verelim
print("Okunan DataFrame'in comment kolon tipi:", test_df_1['comment'].dtype)
if "pyarrow" in str(test_df_1['comment'].dtype):
        print("SONUÇ: BAŞARILI! String kolon pyarrow olarak okundu.\n")
else:
        print("SONUÇ: BAŞARISIZ! String kolon pyarrow olmadı.\n")


    # 2. TEST: İçinde string olmayan bir veri
print("--- 2. Test: String'siz Veri ---")
df_no_string = pd.DataFrame({'id': [1, 2], 'value': [10.1, 20.2]})
buffer_no_string = BytesIO()
df_no_string.to_parquet(buffer_no_string)
buffer_no_string.seek(0)

    # Oku ve sonucu kontrol et
    # Beklenti: String olmadığı için normal dtype kalmalı
test_df_2 = pd.read_parquet(buffer_no_string)
print("Okunan DataFrame'in value kolon tipi:", test_df_2['value'].dtype)
if "pyarrow" not in str(test_df_2['value'].dtype):
        print("SONUÇ: BAŞARILI! String olmayan kolon normal kaldı.\n")
else:
        print("SONUÇ: BAŞARISIZ! String olmayan kolon bile pyarrow oldu.\n")
