#%% dict test
중국집 = {"짜장면" : 1500, "짬뽕" : 2500}

# print(중국집["짜장면"])

if "짜장면" in 중국집 :
    중국집["짜장면"] = 4000
    
print(중국집)

if "탕수육" not in 중국집 :
    중국집["탕수육"] = 9000
    
print(중국집)

# del 중국집["짬뽕"] 
# print(중국집)


for i in 중국집.keys() :
    print(i)
    
for i in range (len(중국집)) : 
    print(str(i + 1) + "." + list(중국집.keys()) [i])

#%% dict task (답안)

# 등급을 입력받아서 학점을 출력해주는 프로그램
# 2 입력 시 B학점입니다. 출력
# 1~5등급, A~F학점 (E학점 제외)

scoreDict = {}
# 0 1 2 3 4
# A B C D F

for i in range(5) :
    scoreDict[i+1] = chr(i+66) if i == 4 else chr(i+65)

print(scoreDict)

rating = int(input("등급 : "))

for i in range(5) : 
    if rating == i + 1 :
        print(scoreDict[rating] + "학점입니다.")
        break