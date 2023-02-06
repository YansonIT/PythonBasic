n = int(input("Enter num of apples "))
k = int(input("Enter num of children "))

apples_for_each_child = int(n / k)
remaining_apples = n % k


print("Number of apples for one child: ", apples_for_each_child)
print("The rest of the apples in the basket: ", remaining_apples)