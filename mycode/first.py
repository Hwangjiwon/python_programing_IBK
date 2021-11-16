## ctrl + shift + f10 실행

add2 = lambda n1,n2 : n1 + n2
print(add2(10,20))

print(type(add2))


# 클래스선언
class User:
    # 생성자선언
    def __init__(self, name):
        self.name = name

    # toString()
    def __str__(self):
        return self.name


# 객체생성
user = User("Python 객체 생성")
print(user)


'''
파이썬 모듈안에는 함수와 클래스를 선언할 수 있다
'''