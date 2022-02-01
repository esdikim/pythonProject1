import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("ADA")
df = df.loc['2021']
df['range'] = (df['high']-df['low'])*0.5
df['range_shift'] = df['range'].shift(1)
df['target'] = df['open'] + df['range_shift']

df['ror'] = np.where(df['high'] > df['target'],
                     df['close']/df['target'],
                     1)

ror = df['ror'].cumprod()[-5]  # 어제의 수익률, -1 오늘의 수익률은 변동중이래서... 맞지 않음. 엑셀로 비교해서 만들어봄...
print(ror)
df.to_excel('trade.xlsx')