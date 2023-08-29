 #%% (1) 문자 형변환
# print("%c" %65)
# print("%d" %"S")

# chr(정수) : 정수를 문자로 변환
# ord(=oridnal, 서수) (문자) : 문자를 정수로 변환

print(chr(ord("A") * 4))


#%%(2) 암호화 test

pw = "a1b2c3"
en_pw = " "
de_pw = " "

for i in pw : 
    en_pw += chr(ord(i) * 9)
    
    print("기존 비밀번호 : %s" %pw)
    # print("암호화된 비밀번호 : {}". format(en_pw))
    print("암호화된 비밀번호 : {pw}". format(pw=en_pw))

#%% (3) decryption test
for i in en_pw : 
    de_pw += chr(ord(i) // 9)
    
    print("암호화된 비밀번호 : {en_pw}\n복호화된 비밀번호 : {de_pw}". format(en_pw=en_pw, de_pw=de_pw))

# 아스키코드를 통해서 암호화를 할 수 있다.
# 회원가입 시 사용자의 비밀번호 혹은 개인정보를 암호호할 때 아스키코드를 사용한다.