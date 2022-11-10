def function1(list):
    print('\nHere are all the items the person wants: ')
    for i in list:
        print(i,end=' ')
    print('\n***********************\n')
    function1(['salami','cheese','ketchup'])
    function1(['tuna','cheese','jalapeno','sriracha'])
    function1(['pulled pork','bbq sauce','mayo','lettuce'])

def zybooks833():
    user_input = '90 92 94 95'
    hourly_temperature = user_input.split()

    ''' Your solution goes here '''
    str = ''
    for temp in hourly_temperature:
        str += temp + ' -> '
    print(str[:-4] + ' ')

def zybooks851():
    user_input = input()
    lines = user_input.split(',')

    # This line uses a construct called a list comprehension, introduced elsewhere,
    # to convert the input string into a two-dimensional list.
    # Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

    mult_table = [[int(num) for num in line.split()] for line in lines]

    ''' Your solution goes here '''
    for i in range(len(mult_table)):
        str1 = ''
        for j in range(len(mult_table[i])):
            str1 += str(mult_table[i][j]) + ' | '
        print(str1[:-3])
#zybooks833()
