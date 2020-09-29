"""Project name :  Lists training
    File name : main.py
    Programmer : Colin B. Chin Choy
"""

for i in range(1,101,1):
    tr = i % 3
    qu = i % 5
    # if i > 1:
    #     for ii in range(2,i//2):
    #         if(i % ii) == 0:
    #             print("not prime")
    #         else:
    #             print("prime")
    if ((tr == 0) and (qu == 0)):
        print("FizzBuzz")
        continue
    if tr == 0:
        print("Fizz")
        continue
    if qu == 0:
        print("Buzz")
        continue
    print(i)
