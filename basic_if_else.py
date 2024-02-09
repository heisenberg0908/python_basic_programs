# in this we will do some basics if else programs 

#1) this is a simple if else program to check a number if a number , greater or equal to some num

def check(num):
    if(num<0):
        print("number is smaller than 0")
    elif(num==0):
        print("number is equal to 0")
    else:
        print("number is greater than 0")
        
# 2) this program takes a number and tells us if it is an even or odd number

def check_even_odd(num):
    if(num%2==0):
        print("the number is an even number")
    else:
        print("the number is an odd number")
        
# 3) this program takes a string and checks it's length:

def check_len(str):
    if(len(str)>3):
        print("it is small letter")
    elif(len(str)>7):
        print("it's length is medium")
    else:
        print("it is long letter")

