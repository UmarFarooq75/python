# exception handling is basically work of developer in this he
# has to control the code i error occur program will not stop
# it will show error

# lets start we use try except in python to control the programs error 

try:
    int(input("Enter Number : "))#if user enter number nothing will happen its ok if user enter any string data or any data instead of number except part will be run
except Exception as e:
    print("some error occurr",e)