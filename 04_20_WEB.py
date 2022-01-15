# https://finance.naver.com/item/sise.naver?code=066570
# lg전자의 일별 시세를 웹에서 가져온다

import pandas as pd
url = "https://finance.naver.com/item/sise.naver?code=066570"
df = pd.read_html(url)
print(df)