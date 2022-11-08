def calc(input_number):
    result = []
    input_number = int(input_number)
    if input_number > 0 and input_number < 100:
        for i in range(101):
            if i * input_number >= 100:
                return result
            result.append(i * input_number)
            

while True:
    input_number = input("0부터 100까지의 정수를 입력하세요. => ")
    print(calc(input_number))
