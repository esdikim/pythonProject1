# dataframe에 index를 주고, 열값으로 조회함
# 2022-01-02

from pandas import DataFrame

data = {"open": [730, 750], "high": [755, 780], "low": [700,710], "close": [750,770]}
df = DataFrame(data, index=["2022-01-01", "2022-01-02"])
print("\nopen 열을 가져온다")
print(df["open"])

print("\n전체를 가져온다")
print(df)

print("\n2022-01-01의 하나의 행을 가져온다")
print(df.loc["2022-01-01"])

print("\n 기본 인덱스를 사용한다. iloc를 써준다")
print(df.iloc[0])

print("\n 하나 이상의 인덱스를 가져온다")
target = ["2022-01-01", "2022-01-02"]
print(df.loc[target])

print("\n 하나 이상의 인덱스를 가져온다. 기본 인덱스에서 가져온다. iloc를 사용한다")
target = [0,1]
print(df.iloc[target])