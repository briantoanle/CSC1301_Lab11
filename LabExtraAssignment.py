def driving_cost(mpg,dpg,md):
    return (md/mpg)*dpg

#print(driving_cost(20.0,3.1599,50.0))

def feet_to_steps(feet):
    return feet/2.5
def testProblem1():
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400.0):.2f}')

def testProblem2():
    input_feet = float(input())
    steps_walked = int(feet_to_steps(input_feet))
    print(steps_walked)


# uncomment to test either problem
#testProblem1()
#testProblem2()