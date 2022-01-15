from pandas import Series

data2 = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04' ]
xrp_close = [501, 502, 503, 504]

s = Series(xrp_close, index=data2)

print(s.index)
print(s.values)

print(s[['2018-08-01', '2018-08-04']])
print(s['2018-08-01':'2018-08-04'])
print(s[0:3])

# 값 추가
s['2018-08-05'] = 505
print(s)


# 값 삭제
print("값 삭제 \n")
print(s.drop('2018-08-05'))
s2= s.drop('2018-08-05')
print(s2) # 새로운객체가 생성된다. s2로 새로운 객체를 받았다.



print(s)

my_list = [100, 200, 300]

new_list = []
for val in my_list:
    new_list.append(val/10)

print(my_list)
print(new_list)

s3 = Series([100,200,300,400])
print("\nSeries(행/열)을 사용하여서 쉽게 계산함. 리스트는 for 문이 필요하나 pandas는 바로 계산 가능함")
print(s3/10)