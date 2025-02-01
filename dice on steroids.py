import random

num_going = True
time_num = 0
end = 0

while time_num <= 4:
    while num_going == True:
        num = random.randint(1, 6)
        time_num += 1
        if num <= 3:
            print(num)
        else:
            time_num -= 1
            print(f'The number was acquired {time_num} number of times')
            print('the process has ended')
            end += 1
            num_going = False
            if time_num <= 3:
                time_num = 0
    num_going = True
print(f'the process took {end} number of times to finish')