import random

num_goin3g = True
time_num = 0
end = 0

#change this number to edit the number of times you require your numbers
while time_num <= 4:
    while num_going == True:
        #change this number if you want different types of dice
        num = random.randint(1, 6)
        time_num += 1
        #change this number to edit the numbers you want
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
