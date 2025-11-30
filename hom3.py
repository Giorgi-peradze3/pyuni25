


def medium():

    num_input1 = input('enter numbers: ')
    num_input2 = input('enter numbers: ')
    num_input3 = input('enter numbers: ')
    num_input4 = input('enter numbers: ')
    num_input5 = input('enter numbers: ')



    numbers1 = [float(num) for num in num_input1.split()]
    numbers2 = [float(num) for num in num_input2.split()]
    numbers3 = [float(num) for num in num_input3.split()]
    numbers4 = [float(num) for num in num_input4.split()]
    numbers5 = [float(num) for num in num_input5.split()]


    total = sum(numbers1 + numbers2 + numbers3 + numbers4 +numbers5)
    count = len(numbers1) + len(numbers2) + len(numbers3) + len(numbers4) + len(numbers5)

    average = total / count


    print('average is', average)

result = medium()
