def hello():
    print('hello user')

def pack(arg1, arg2, arg3):
    return [arg1,arg2,arg3]
    
def eat_lunch(list):
    if len (list) == 0:
        print('Empty lunchbox! :(')
    else:
        for i in range (len(list)):
            if i == 0:
                print(f'First I eat {list[0]}')
            else:
                print(f'Next I eat {list[i]}')


pack('bye','user','adios')
hello()
eat_lunch([])
eat_lunch(['burger','ham sandwich'])
eat_lunch(['tuna'])
eat_lunch(['apple','banana','cookie','donut'])