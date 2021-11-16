"""
섭씨온도를 입력 받아서 화씨로 변환하기 (p.23)
"""

def fah_convert(celsius):
    return ((9/5) * float(celsius)) + 32

print("변환하고 싶은 섭씨 온도를 입력하세요")
user_input = input()
print(type(user_input), user_input)

fah = fah_convert(user_input)

print("섭씨온도 : " + user_input)
"""
print("섭씨온도 : " + float(user_input)) 
이건 오류남. 
"""
print("섭씨온도 : ", float(user_input))
print(f"섭씨온도 : {user_input}")
print("화씨온도 : {0:.2f}".format(fah))  # 소숫점 2째자리까지만
print(f'화씨온도 : {round(fah, 2)}')
