import csv

f1 = open("./connectlog_2022-11-27-23_6_35.csv")

f1_r = csv.reader(f1)

f2 = open("./export.csv",'w', newline='')

f2_w = csv.writer(f2)

user_list = ["suk6", "mazoola12", "wol7282", "guest12", "lmk0511", "bs510"]

def IP_split(original_str):
    left = original_str.split("[")
    right = left[2].split("]")
    
    return right[0].split()

def User_split(original_str):
    left = original_str.split("[")
    right = left[1].split("]")

    return right[0]

def sort(original_str):
    user = User_split(original_str[4])
    
    for i in user_list:
        if user == i:
            return 0

    f2_w.writerow(IP_split(original_str[4]))
    return user

count = 0

for value in f1_r:
    count += 1
    print(sort(value))

print(count)

f1.close()
f2.close()