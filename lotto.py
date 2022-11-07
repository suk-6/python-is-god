import random
import time

def Check_number(input_number):
    check_list = []
    if len(input_number) != 6:
        return 1 
    for i in input_number:
        if i > 45 or i < 0:
            return 1
        if i in check_list:
            return 1
        check_list.append(i)
    return 0

def Create_lotto():
    lotto_number = []
    for i in range(6):
        num = random.randint(1, 45)
        lotto_number.append(num)
    
    lotto_number = list(set(lotto_number))

    if len(lotto_number) != 6:
        lotto_number = Create_lotto()
    return lotto_number

def Check_lotto(input_number, lotto_number):
    count = 0
    count_list = []
    for i in input_number:
        for j in lotto_number:
            if int(i) == int(j):
                count_list.append(int(i))
                count += 1
    return count, count_list

while True:
    print("\n\n\n\n---------------------------------------\n\n\n\n")
    print("룰: 1부터 45까지의 숫자 중 6개")
    print("로또 번호를 입력하세요.\nex) 3 5 12 27 29 33\n")
    input_number = input("input: ")
    input_number = input_number.split(" ")
    input_number = list(map(int, input_number))
 
    if Check_number(input_number) == 0:
        print(f"입력하신 번호는 {input_number} 입니다.")
    else:
        print("잘못된 번호입니다.")
        break

    print("당첨 번호 추첨 중..\n")
    time.sleep(2)

    print("이번 당첨 번호는?")
    lotto_number = []
    lotto_number = Create_lotto()
    print(f"당첨 번호는 {lotto_number} 입니다!\n")

    count, count_list = Check_lotto(input_number, lotto_number)

    print(f"맞추신 개수는 {count}개")
    print(f"맞춘 번호는 {count_list} 입니다.")
    if count == 6:
        print("와.. 이걸 다 맞추다니!")
    time.sleep(5)