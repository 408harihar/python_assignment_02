# Question 1
# Write a recursive function to calculate the Fibonacci series
from time import sleep


def myFibonacci(firstnum, secondnum, nterms):  # not allowed to change the args
    if nterms != 0:
        print(firstnum)
        myFibonacci(secondnum, firstnum + secondnum, nterms - 1)


if __name__ == '__main__':
    firstnum = 0
    secondnum = 1

    nterms = 10
    myFibonacci(firstnum, secondnum, nterms)  # not allowed to change the args
    sleep(5)