from pandas import Series

data = [100,200,300,400]
s = Series(data)
print(type(s))
print(s)

data2 = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04' ]
xrp_close = [501, 502, 503, 504]

# index 를 지정해주면 문자열 인덱스를 사용할 수 있다,
# 0부터 시작하는 인덱스도 사용 가능하다
s2 = Series(xrp_close, index=data2)
print(s2)

# 인덱스를 지정하지 않으면, 0부터 인덱스가 생성된다
s3 = Series(xrp_close)
print(s3)

# 두개의 인덱스 사용이 가능함을 알 수 있다.
print(s2[0])
print(s2['2018-08-01'])

