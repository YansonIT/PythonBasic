f_class = int(input("Enter num of children in first class: "))
s_class = int(input("Enter num of children in second class: "))
t_class = int(input("Enter num of children in third class: "))


f_class_desks = (f_class // 2) + (f_class % 2)
s_class_desks = (s_class // 2) + (s_class % 2)
t_class_desks = (t_class // 2) + (t_class % 2)


print("Desks in firs class: ", f_class_desks)
print("Desks in second class: ", s_class_desks)
print("Desks in third class: ", t_class_desks)
print("Total desks needed: ", f_class_desks + s_class_desks + t_class_desks)