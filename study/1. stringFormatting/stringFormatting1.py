#%% (2) 
# 서식문자 (format)
# 문자열 쌍따옴표 안에서 변수를 출력하고 싶을 때 사용 / ex. print("이름:name")
# 반드시 따옴표 안에서 작성한다.
# %d : decimal 데시말 (정수=10진수)
# %o : octal 오탈 (정수=8진수)
# %x : hexadecimal 데시말 (정수=16진수)
# %f : float (실수)
# %c : character (문자)
# %s : string (문자열)

name = "코모리"
age = 23
height = 160.36
hobby = "reading a book"

print("이름 : %s" %name)
print("나이 : %d살" %age)
# print("나이 : %d" %age, end = "살")
print("키 : %.1fcm" %height)
print("취미 : %s" %hobby)

#%% (3) 복습

name = "코모리"
age = 23
height = 160.36
hobby = "reading a book"

print("자기소개\n이름 : %s" %name)
print("나이 : %d" %age, end = "살\n")
print("키 : %.1fcm" %height)
print("취미 : %s" %hobby)

