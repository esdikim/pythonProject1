# 2021-12-30 DataFrame
from pandas import DataFrame

data = {'open': [730,750], "high": [750,780], "low": [700, 710], "close":[750,770]}
df = DataFrame(data, index=["2021-12-28", "2021-12-29"])
print("index를 정의해 주고, Dataframe를 만들어본다")
print(df)