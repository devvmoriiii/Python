#%% 기타 제어문

# break : 인터프리터가 break 를 만나자마자 반복문 즉시 탈
출
# continue : 아래 문장을 하지 않고 다음 반복 
#(아래 문장을 하지 않음이 중요 / 밑에 소스코드를 실행하고 싶지 않을 때)


# 1~10까지 중 4까지만 출력
# (무조건 10번 반복해야 하는 고정된 상황에서 조절하는 방법)

for i in range (10) :
    print(i + 1)
    
    if i == 3 :
        break
    
for i in range (10) :
        if i == 3 :
            break
        print(i + 1)
#%% . 

#1~10까지 중 4를 제외하고 출력

for i in range (10) :
    if i == 3 :
        continue
    print(i + 1)
    
#%% 문제 -1 성공
# (1) 100~1까지 중 70까지만 출력 (break)

for i in range (100, 0, -1) : 
    print(i)
    
    if i == 70:
        break
    
for i in range (100) : 
    print(100 - i)
    
    if i == 30 : 
        break

for i in range (100) :
    if i == 31 :
        break
    print(100 - i)

#%% 문제 -2 ㅠ
# (2) 1~100까지 중 3과 5의 공배수만 출력 (continue)

# for i in range (100) :
#     temp = i
#     temp != i%3 == 0 and i%5 == 0
    
#     if i == temp :
#         continue
    
#     print (i + 1)


# for i in range (1, 101) :
#     temp == i%3 == 0 and i%5 == 0 
#     if i != temp :
#         continue
    
#     print (i)

#  공배수 빼고 다 나옴 ;;
for i in range (1, 101, 1) : 
    if i != i%3 == 0 and i%5 == 0 :
        continue
    print (i)


# for i in range (1, 101, 1) : 
#     result = i
#     result = (i%3 == 0 and i%5 == 0)
#     if i != result :
#         continue
#     print (i)
    
    
for i in range (1, 101) :
    if i%3 == 0 and i%5 == 0 :
        print(i)    


#%% 문제 2 - 답안

# (i+1) %3 == 0 and (i+1) %5 == 0

for i in range (100) :
    if not ((i+1) % 3 == 0 and (i+1) % 5 == 0) :
        continue
    print(i+1)
    
    
for i in range (100) :
    if (i +1) % 3 != 0 or (i + 1) % 5 != 0:
        continue
    print(i + 1)
    
    
#%% 답안

for i in range (100) :
    if (i+1) % 3 == 0 and (i+1) % 5 == 0 :
        print(i+1)        
        
    #%%
    
for i in range (100) :
    if (i +1) % 3 == 0 and (i + 1) % 5 == 0:
        print(i + 1)
        
for i in range (100) :
    if not ((i + 1) % 3 == 0 and (i + 1) % 5 == 0) :
        continue
    print(i + 1)
        
        
#%% 
for i in range (1, 101) :
    if not (i % 3 == 0 and i % 5 == 0):
        continue
    print(i)
    





    


    

        
        
        