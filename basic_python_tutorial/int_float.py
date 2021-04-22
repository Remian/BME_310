
'''
#int and #float

#int -> 1,2,3,4,5,6
#float -> 1.0,2.0,3.0,4.0,5.0,6.0

#sum, substract, division, multiplication, mod, power

x = 20
y = 2.9

result = x+y
#print(result)

#22.6 --> integer -->30

result = round(result)

print(result)
print(type(result))

example_int = 23
print(example_int)
print(type(example_int))

example_int = float(example_int)
print(example_int)
print(type(example_int))
'''

#problem--> input two floats --> sum --> sum convert nearest integer --> print

input_1 = float(input("Please enter a float value bro! : "))
input_2 = float(input("Please enter a float value bro! : "))

sum_float = input_1+input_2

sum_int = round(sum_float)

print(sum_float)
print(sum_int)

def read_sensor_1():

    while(True):

        print("some bunchy of task happening")
        print("more bunchy of task happening")


def read_sensor_2():

    while (True):
        print("some bunchy of task happening")
        print("more bunchy of task happening")


read_sensor_1()
read_sensor_2()









