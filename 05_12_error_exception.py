price = {"open": 100}
print("point-1")

print("exception이 발생하면 넘어간다.")
try:
    open=price['open1']
except:
    pass

print("point-2")