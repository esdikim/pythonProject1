# 2021년 티커 정보를 가져와서, 백 트레킹을 한 후
# 어떤 코인이 현재의 백트래킹과 가장 맞는지 찾아본다
# 백트래킹시 수수료는 0.0032로 계산해 준다... (시뮬레이션을 통해 구한 값)
# 백 트레킹을 위한 가장 좋은 K값을 구해야 한다. 현재는 0.5를 K값으로 사용하고 있다.

# ETH 3.654073082981359
# LTC 1.1550183846691318
# ETC 2.5955553911929803
# XRP 0.9171876278437564
# BCH 1.2543419923026697
# QTUM 3.6932500458069017
# BTG 0.6885242177962178
# EOS 0.422109568673658

# BTC 1.5385681435555352
# ETH 2.2177577370523305
# LTC 0.6938991671259638
# ETC 1.5676610346952609
# XRP 0.5432631176755105
# BCH 0.7659312117099591
# QTUM 2.312972481284436
# BTG 0.4098543049037302
# EOS 0.24550948943996112
# ICX 1.3392074318686082
# TRX 1.0418078116739646
# ELF 0.08098569424561912


import pybithumb
import numpy as np

# 티커정보를 가져온다

ticker = pybithumb.get_tickers()
fee = 0.0032
for tic in ticker:
    df = pybithumb.get_ohlcv(tic)
    df = df.loc['2021']
    df['range'] = (df['high']-df['low'])*0.5
    df['range_shift'] = df['range'].shift(1)
    df['target'] = df['open'] + df['range_shift']

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close']/df['target']-fee,
                         1)

    ror = df['ror'].cumprod()[-5]  # 어제의 수익률, -1 오늘의 수익률은 변동중이래서... 맞지 않음. 엑셀로 비교해서 만들어봄...
    print(tic, ror)

# df.to_excel('trade.xlsx')