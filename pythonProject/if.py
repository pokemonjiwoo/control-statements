#1. 사용자가 입력
data = int(input('입력하세요.'))
#2. 3의 배수
th = data%3
if th == 0 :
    # 3의 배수면 ok
    print("ok")
    # 아니면 no
else :
    print("no")


var = [1, 2, 3]

if 3 in var :
    print("원하는 숫자가 있습니다.")
else :
    print("찾는 숫자가 없습니다.")
