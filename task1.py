print("задание 1")
count = 0
for i in range(1, 10):
    if i % 3 == 0 or i % 5 == 0:
        count += i
print(count)
#####
count1 = 0
for i in range(1, 1000):
    if i % 3 ==0 or i % 5 ==0:
        count1 += i
print(count1)

print("задание 4")
data = input("Введите дату  формате (2022-06-29 12:30): ")
time = data.split(" ")[1]
new_data = data.split(" ")[0].split("-")
print(new_data.extend(time))
data_dict = {}
data_dict["год"] = new_data[0]
data_dict["мсяц"] = new_data[1]
data_dict["день"] = new_data[2]
data_dict["время"] = time
print(data_dict)
