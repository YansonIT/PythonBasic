num = int(input("Enter num: "))

firs_step = 1
step_result = 0

print(num)
while True:
    step_result = firs_step ** 2
    firs_step += 1
    if step_result <= num:
        print(step_result)
    if num < step_result:
        break
