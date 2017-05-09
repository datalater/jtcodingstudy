import random

# 컴퓨터가 미리 정해놓은 숫자를 사용자가 최소한의 시도로 맞히는 updown 게임

#-----컴퓨터가 문제를 내는 부분-----#

random_number = random.randint(1,99)

print("="*50)
print('''<목베개>
안녕, 나는 목베개야.
1이상 99 이하 자연수 중에 내 마음 속의 숫자를 맞혀봐.
네가 몇 번만에 맞히는지 지켜보겠어.''')
print("="*50)

# print(random_number)

#-----사용자가 문제를 맞히는 부분-----#

user_number = 0
count = 0

# 추리한 숫자가 틀리면 계속 반복되어야 한다.
# 따라서 while의 조건문은 "틀리는 경우"로 잡아야 한다.

while (random_number != user_number):
    user_number = int(input("\n숫자를 입력하세요: "))

    count += 1

    if (random_number > user_number):
        print("="*50)
        print("<목베개>\n하하하. up! %s아웃이지롱."%count)
        print("="*50)
    elif (random_number < user_number):
        print("="*50)
        print("<목베개>\n하하하. down! %s아웃!"%count)
        print("="*50)

print("="*50)
print('''<목베개>
오, 뭐야. 정답이야. %s번 시도해서 맞혔어.'''%count)
print("="*50)

#-----EOP-----#
