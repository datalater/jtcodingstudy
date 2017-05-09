import random

#----------사용자 이름 설정하기----------#

user_name = "<"+input("당신의 이름을 입력하세요: ")+">"

#----------컴퓨터가 문제 내는 차례----------#

computer_number = random.randint(1, 99)
print("="*50)
print('''<목베개>
반가워, {}
안녕, 나는 목베개야.
1이상 99 이하 자연수 중에 내 마음 속의 숫자를 맞혀봐.
네가 몇 번만에 맞히는지 지켜보겠어.'''.format(user_name))
print("="*50)

# print(computer_number)

user_number = 0
user_count = 0

while computer_number != user_number:
    user_number = int(input("숫자를 입력하세요: "))

    if user_number < computer_number:
        print("up")
    elif user_number > computer_number:
        print("down")

    user_count += 1

print("\n")
print("정답:", computer_number, "축하합니다.")
print("\n")
print("="*50)
print("<목베게> 후후. 이제는 내 차례야 문제를 내.")
print("="*50)
print("\n")

#----------사용자가 문제 내는 차례----------#

user_number = int(input("목베개가 맞혀야 할 1이상 99 이하 숫자를 입력하세요: "))

while (user_number < 1 or user_number > 99):
    if user_number > 99:
        print("<목베개> 감히 날 속이려 하다니. 허튼 수작 부리지마!\n")
        user_number = int(input("목베개가 맞혀야 할 1이상 99 이하 숫자를 입력하세요: "))

    elif user_number < 1:
        print("<목베개> 감히 날 속이려 하다니. 다시 입력해.\n")
        user_number = int(input("목베개가 맞혀야 할 1이상 99 이하 숫자를 입력하세요: "))

computer_number = random.randint(1, 99)
computer_list = list(range(1,100))
computer_count = 0

while computer_number != user_number:
    print("\n<목베개>:", computer_number)

    if computer_number < user_number:
        user_response = input("up인가요, down인가요? [up/down]: ")
        if user_response == "up":
            computer_list = [a for a in computer_list if a > computer_number]
            computer_number = random.randint(min(computer_list), max(computer_list))
        elif user_response == "down":
            print("<목베개> 감히 날 속이려 하다니. 허튼 수작 부리지마!\n")

    elif computer_number > user_number:
        user_response = input("up인가요, down인가요? [up/down]: ")
        if user_response == "up":
            print("<목베개> 감히 날 속이려 하다니. 허튼 수작 부리지마!\n")
        elif user_response == "down":
            computer_list = [a for a in computer_list if a < computer_number]
            computer_number = random.randint(min(computer_list), max(computer_list))

    computer_count +=1

print("<목베개>:", computer_number, "축하합니다.")
print("\n")
print(user_name, ": ", user_count, "회")
print("<목베개> :", computer_count, "회")
print("-"*10)

if user_count > computer_count:
    print(user_name+"님, 지셨습니다.")
elif user_count < computer_count:
    print(user_name+"님, 이기셨습니다.")
else:
    print("비겼습니다.")
