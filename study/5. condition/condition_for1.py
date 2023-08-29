#%% for test
for i in range(0, 10, 1) : 
    print("%d. 모리" %(i+1))
    
#%% 
for i in range(10, 0, -1) :
    print("%d. 모리" %i)


#%%
#0부터 1씩 증가하는 for문을 작성한다. (10번 반복)
#단, 10부터 1까지 출력한다.

for i in range(0, 10, 1) : 
    print(10 - i)
    
# n + 0 = 10
# 1. n = 10
# 2. 10 - 0 = 10
#%% for task (실습)

# =============================================================================
# (1) 1~100까지 출력
# (2) 100~1까지 출력 
# (3) 1~100까지 중 짝수만 출력
# (4) A~F까지 출력 
# (5) A~F까지 중 C를 제외하고 출력 
# (6) aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력 
# =============================================================================

# (1) 1~100까지 출력
for i in range (1,101,1) : 
    print(i)
    
for i in range (0, 100, 1) :
    print(i+1)
    
#%% (2) 100~1까지 출력 
for i in range (100, 0, -1) : 
    print(i)    
    
for i in range (0, 100, 1) :
    print(100 - i)
#%% (3) 1~100까지 중 짝수만 출력
for i in range (4, 103, 2) : 
    print(i - 2)
    
for i in range (0, 100, 2) :
    print(i + 2)

for i in range (0, 50, 1) : 
    print((i +1) * 2)
    

#%% range (start, end, step)

#start 가 0일 때에는 생략이 가능하다.
#step 이 1일 때에는 생략이 가능하다.

for i in range (0, 5, 1) :
    print(i)

for i in range (5) :
    print(i)

#%% (4) A~F까지 출력 
for i in range (65, 71, 1) : 
    print(chr(i))
    
for i in range (6) : 
    print(chr(i + 65))

#%% (5) A~F까지 중 C를 제외하고 출력 
for i in range (5):
    if i > 1 : 
        i += 1
    print(chr(i + 65)) 
    
  #%% (5) A~F까지 중 C를 제외하고 출력 - 2

# i 값을 직접 변경하고 싶지 않을 경우, temp 변수에 담아 변수를 변형한다.

temp = 0
for i in range (5) : 
    temp = i
    temp = temp + 1 if i > 1 else temp

    print(chr(65+temp))
    
 #%% (6) aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력

temp = 0
for i in range (97, 123) : 
    temp = i
    temp = temp - 32 if i%2 == 0 else temp

    print(chr(temp))
 

for i in range (97, 123) : 
    if i%2 == 0 : 
        i-= 32

    print(chr(i))
    
for i in range (26) :
        if i%2 == 1 :
            i -= 32
        print(chr(i + 97))
        
for i in range (26) :
        i = i if i%2 == 0 else i-32
        print(chr(i + 97))
    
#%% (6) aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력

for i in range (26) : 
     i = i + 97 if i%2 == 0 else i + 65
     print(chr(i), end = "")
    

#%% test

result = i
for i in range (6) :
    if i == 0 :
        result = "*"
    elif i == 1 :
        result = "**!"
    elif i == 2 : 
        result = "***"
    elif i == 3 : 
        result = "****"
    elif i == 4 :
        result = "*****"
    else :
        result = "******"
        
    print (result)
    