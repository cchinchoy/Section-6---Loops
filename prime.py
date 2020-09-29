num = 15
if num > 1:
    for ii in range(2,num//2):
        print(num)
        print(ii)
        if(((num % 2) == 0) and ((num % 3) == 0)):
            print(num,"not prime - 1")
            break
        else:
            print(num,"prime")
else:
    print(num,"not prime - 2")
