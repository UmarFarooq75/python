#write python program to show the table between 1 and 10


def table1(x):
    i=1
    while(i<=10):
        print(x," * ",i," = ",x*i)
        i+=1


def table(x):
    for i in range(1,11):
        print(x," * ",i," = ",x*i)

def df(num):
    match num:
        case 1:
            table1(1)
        case 2:
            table(2)
        case 3:
            table(3)
        case 4:
            table(4)
        case 5:
            table(5)
        case 6:
            table(6)
        case 7:
            table(7)
        case 8:
            table(8)
        case 9:
            table(9)
        case 10:
            table(10)
        case _:
            print("You have to choose number between 1-10")



while(True):
    num=int(input("Enter Number between 1-10 : "))
    if(num>0 and num <11):
        df(num)
        break


