#%% myException

class NicknameError(Exception) :
    pass

def checkNickname(name) :
    if name == "바보" :
        raise NicknameError
        

nickname = input("닉네임: ")

try :
    checkNickname(nickname)
    print("닉네임 생성 성공")
    
except NicknameError :
    print("비속어는 사용할 수 없습니다.")
    
#%% myException task
# 외부에서 채팅 문자열을 받아와서 in 으로 비속어 검사를 한다.
# 비속어는 바보, 멍청이, 똥
# 사용자 예외 처리로 선언하여 만든다. 비속어가 없다면 채팅 메세지를 출력한다.


class BadWordError(Exception) :
    pass

chat = ""

def checkChatting(temp) :
    badwords = ["바보", "멍청이", "똥개"]
    for i in badwords :
        if i in temp :
            global chat
            chat = temp.replace(i, "**")
            raise BadWordError
cnt = 0

while True :
    chat = input("채팅 [나가기:q] : ")
    if chat.lower() == "q" :
        break
    
    try :
        checkChatting(chat)
        print(chat)
    except BadWordError :
        cnt += 1
        print("%d회 비속어를 사용하였습니다" %cnt)
        print(chat)
    
        
    
    

















    
    