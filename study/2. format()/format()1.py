#%%(1) format test
data = 10
data2 = "%d" %100

# print("data : %d" %data)
print(data)
print(data2)
print(type(data2))

#%%(2) format test2
# 문자열값. format()
#A.B : A 안에 B

data1 = 10
data2 = 10.345
data3 = "A"
data4 = "ABC"

print("data1 : {}". format(data1))
print("data2 : {}". format(data2))
print("data3 : {}". format(data3))
print("data4 : {}". format (data4))

print("data1 : {}\ndata2 : {}". format(data1, data2))
print("data3 : %s" %data3)
print("data3 : %c" %data3)
print("data4 : %s" %data4)

print("아스키코드 a : %c" %97)

#%% (3) format test

pw = 5
pw2 = 10

print("pw + pw2 : {}". format(pw+pw2))


#%% (4) 자동형변환
# // : 몫 연산
print(10/3)
print(10//3.0)

#%% (5) 강제형변환
print(float(10)//3)

#%% 복습

result1 = 10
result2 = 15

print("%d, %d" %(result1, result2))














