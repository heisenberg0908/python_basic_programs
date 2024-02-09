# it is a simple python program to reverse a string:

def reverse(str):
    res=str[::-1] # in this we have used negative indexing
    print("the reversed of the given string is",res)
    

# to find if a string is paindrome or not

def to_check_palindrome(str):
    res=str[::-1]
    if(res==str):
        print("it is a palindrome number")
    else:
        print("it is not a palindrome number")
        