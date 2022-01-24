import pybithumb

with open("bithumb.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    print(key)
    print(secret)
#    bithumb = pybithumb.Bithumb(key, secret)

try: # 비정상 상태를 일부러 만들어서 비교함.
    if None > 123:
        print("정상")
except:
    print("에러발생")