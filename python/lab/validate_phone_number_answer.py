import re

def validate_phone_number(number):
    #==================================#
    pattern = r"^010[1-9]\d{7}$"
    #==================================#
    if not re.match(pattern, number):
        return "휴대폰 번호가 아닙니다."
    else:
        return "휴대폰 번호입니다."

def main():
    number = input("핸드폰 번호를 입력하세요: ")
    print(validate_phone_number(number))


if __name__ == "__main__":
    main()
