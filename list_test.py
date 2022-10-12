my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
my_list2=[]
my_list3=[]
for num in my_list:
    if num>=10:
        my_list2.append(num)
print(my_list2)
input_num=int(input("test : "))
for number in my_list:
    if number>input_num:
        my_list3.append(number)
print(my_list3)
