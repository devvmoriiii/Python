#%% (1)
#1~100까지 값 넣고 출력

dataList = [0] * 100

for i in range (len(dataList)) :
    dataList[i] = i + 1

for i in dataList :
    print(i)
    
print ("========\n답안(1)")

dataList = []

for i in range (100) :
    dataList.append(i+1)

print(dataList)

print ("========\n답안(2)")

dataList = [0 ] * 100

for i in range (100):
    dataList[i] = i + 1

print(dataList)

#%% (2)
#1~100까지 중 짝수만 넣고 출력

dataList = [0] * 50

for i in range(len(dataList)) :
    dataList[i] = (i * 2) + 2

print(dataList)

for i in dataList :
    print(i)
    
print ("========\n답안")

dataList = [0] * 50

for i in range (len(dataList)) :
        dataList[i] = (i+1) * 2
        
print(dataList)
#%% (3)
# A~F까지 넣고 출력

dataList = [0] * 6

for i in range (len(dataList)) :
    dataList[i] = i + 65
    
print(dataList)

for i in dataList :
    print(chr(i))
     
print ("========\n답안")

dataList = []

for i in range (6) :
    dataList.append(chr(i + 65))
print(dataList)
#%% (4)
# A~f까지 중 C를 제외하고 출력

dataList = [0] * 6

for i in range(len(dataList)) :
    dataList[i] = i + 65
    
print(dataList)

for i in dataList :
    if i == 67 :
        continue
    print(chr(i))
    
print ("========\n답안(1)")

dataList = [""] * 5
temp = 0

for i in range (len(dataList)) :
    temp = i
    if temp > 1 :
          temp += 1
    dataList[i] = chr(temp + 65)

print(dataList)


# for i in range(len(dataList)) :
#     if i > 1 :
#         i += 1
    
#     dataList[i] = i + 65

# print(dataList)

print ("========\n답안(2)")

dataList = [""] * 5

for i in range(len(dataList)) :
    dataList[i] = chr((i + 1 if 1 < i else i) + 65) 
print(dataList)
     


 #%% (5)
# aBcDeFgHiJkLmNoPqRsTuVwXyZ 출력

dataList = [0] * 26

for i in range (len(dataList)) :
    dataList[i] = i + 65
    
for i in dataList :
    if not i%2 == 0 :
        i = i + 32
    print(chr(i))

print ("========\n답안")

dataList = [""] * 26

for i in range (len(dataList)) :
    dataList [i] = chr(i + 97 if i%2 == 0 else i + 65) 

print(dataList)

for i in dataList:
    print(i,  end = "")





#%% (6)
# "ABC" 에서 B를 Z로 변경하기

#1
dataList = ["A", "B", "C"]

dataList[1] = "Z"
print(dataList)

#2
dataList = ["ABC"]

# ...?


print ("========\n답안 전 풀이")

# "abcd" = 문자열

strList = "abcd"
print(strList[0])

print ("========\n답안")

strList = "ABC"
strList = strList.replace("B", "Z")
print(strList)

#%% (7)
# 자연수를 한글로 변경하기 예) 1024 > 일공이사

print ("========\n답안 전 풀이")
# %10 처리를 하여 나오는 나머지가 각 자리 수의 숫자
# 1) 1024 % 10 == 4
# 2) 1024 // 10 = 102
# 3) 102 % 10 == 2
#     .
#     .
#     .

print ("========\n답안")

num =  int(input("자연수 입력 : "))
hangle = "영일이삼사오육칠팔구"
result = ""

while num != 0 :
    result = hangle[num % 10] + result
    num = num // 10
print(result)
    









