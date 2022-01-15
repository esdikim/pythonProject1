# dataframe에서 shift 연습
# 2022-01-02
# 04-25
from pandas import DataFrame
from pandas import Series

data = {"open": [730, 750], "high": [755, 780], "low": [700,710], "close": [750,770]}
df = DataFrame(data)
s = Series([300,400])
df["Volumn"]=s

df.loc[2] = (100,200,300,400,500)
df.loc[3] = [600,700,800,900,1000]

upper = df["open"]*1.3
df["upper"] = upper
print("\n전체를 가져온다")
print(df)

