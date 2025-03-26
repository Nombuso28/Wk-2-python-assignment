My_list = []
print(My_list)

My_list.append(10)
My_list.append(20)
My_list.append(30)
My_list.append(40)
print(My_list)

My_list.insert(1,15)
print(My_list)

UR_list = [50,60,70]
My_list.extend(UR_list)
print(My_list)

del My_list[7]
print(My_list)

My_list.sort()
print(My_list)

index = My_list.index(30)
print(index)