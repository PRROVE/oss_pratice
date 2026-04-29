# 숫자 두 개를 한 줄에 입력 (예: 3 5)
num1,num2 = map(int,input("숫자 두 개를 입력하세요: ").split())

# 연산자 입력
op = input("연산자를 입력하세요 (1.+ 2.- 3.* 4./): ")

# 조건문으로 계산
if op == 1:
    print("결과:", num1 + num2)

elif op == 2:
    print("결과:", num1 - num2)

elif op == 3:
    print("결과:", num1 * num2)

elif op == 4:
    if num2 != 0:
        print("결과:", num1 / num2)
    else:
        print("0으로 나눌 수 없습니다.")

else:
    print("잘못된 연산자입니다.")