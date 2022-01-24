# _, __  테스트
#
# customer1 = 0
#
# def order(price):
#     global customer1
#     customer1 += price
#     return customer1
#
# print(order(3000))
# print(order(5000))
#
# # class를 활용하면 함수의 반복을 줄인다.

class Order:
    def __init__(self, name):
        self.customer = 0
        self.name = name
        print(name)
    def order(self, price):
        self.customer += price
        return self.customer

customer1 = Order("홍길동") # customer1은 클래스를 통해 생성한 객체이고, customer1의 Order Class의 인스턴스라고 합니다.
# customer1.Order("홍길동")
# customer2.Order("장길산")

print(customer1.order(14000))
print(customer1.order(5000))
print()
customer2 = Order("장길산")
print(customer2.order(1000))
print(customer2.order(4000))

# Order class를 상속하여 extraOrder 함수를 만들었다.
class extraOrder(Order):
    def order(self, price):  # 기존 함수를 변경해서 기능을 추가했다. 메소드 오버라이딩 임...
        self.customer += price
        return str(self.customer) + '원'

extraCustomer = extraOrder("영희")
print(extraCustomer.order(1000))

class Family:
    lastname = "김"
print(Family.lastname)
print()

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)
print()

Family.lastname = '박'
print(a.lastname)
print(b.lastname)

# __ 에 대해 .. 보자..

class vector:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        x_ = self.x + other.x
        y_ = self.y + other.y
        z_ = self.z + other.z
        return vector(x_, y_, z_)

    def show(self):
        print(f"x:{self.x}, y:{self.y}, z:{self.z}")

v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = v1 + v2
v3.show()