# here are some basic strings operations 
#1) for printing all the string characters

str="India"
for i in str:
    print(i)

#2) string concatination(conact):
str1="fname"
str2="lname"
str3=str1+str2
print(str3)

#3) to find the length of the string
str="india"
print(len(str))

#4) indexing in strings
str="california"
res=str[1:3]
print(res)

#5)convert in upper case
str="name"
res=str.upper()
print(res)

#6) convert to lower case
str="NAME"
res=str.lower()
print(res)

#7) to replace characters of string:
str="brock"
res=str.replace('b','s')
print(res)

#8) to check the type of data type
str="ayush"
print(type(str))