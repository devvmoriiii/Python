#%% (1) 대소비교
#두 정수 입력받기

n1Msg = "첫번째 정수 : "
n2Msg = "두번째 정수 : "

num1 = int(input(n1Msg))
num2 = int(input(n2Msg))

#num1 이 num2 보다 크면 num1이 큰 값
#num1 이 num2 보다 작으면 num2이 큰 값
#num2 가 더 크거나, num1 과 num2 가 같으면 False 쪽으로 이동한다.
#else쪽 (False쪽) 에서 한 번 더 두 수가 같은지 물어본다.
#만약 두 수가 같다면 "두 수가 같습니다.", 두 수가 같지 않다면 num2 가 큰 값이다.

result = num1 if num1 > num2 else "X\n두 수가 같습니다." if num1 == num2 else num2
print("더 큰 값: {}". format(result))

#%% 퀴즈게임 (실습)

print("다음 중 프로그래밍 언어가 아닌 것은?\n1. JAVA\n2. 파이썬\n3. C언어\n4. 망둥어")

answer = int(input("정답은 몇 번? : "))
correct_answer = 4

result = "정답입니다." if answer == correct_answer else "오답입니다."

print(result)

#%% 퀴즈게임 (답안)

qMsg = "다음 중 프로그래밍 언어가 아닌 것은?"
choiceMsg = ("1. JAVA\n2. 파이썬\n3. C언어\n4. 망둥어\n답: ")

choice = int(input(qMsg + "\n" + choiceMsg))
answer = 4

result = "정답!" if choice == answer else "오답..."
print(result)


#%% 연산과 연결

print(10+9)
print("10"+ "9")
print("10" + str(9))











