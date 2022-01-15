# 엑셀의 파일 처리
import pandas as pd

# 파일 처리를위해서 \는 두개를 써줘야 한다
df = pd.read_excel("C:\\Anaconda3\\esdiworkplace\\aaa.xlsx")
print(df)

df = df.set_index('date')
print(df)

df.to_excel("C:\\Anaconda3\\esdiworkplace\\bbb.xlsx")