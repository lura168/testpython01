# print("Hello kitty"+" From bbu"+str(6))
# print('double qoute')
# print("single \'quote\' and \"double\" qoute \ninside qoute")

# # name=input("whate is your name?")
# # print("sok " + name)
# qty1=int(input("Qty1 = "))
# qty2=int(input("Qty2 = "))
# price=float(input("Price = "))
# total_qty=qty1+qty2
# print("Total Qty= "+str(total_qty))
# amount=total_qty*price
# print("Total Amount="+str(amount))

# a = input("input a =")
# b = input("input b =")
# c = a
# a = b
# b = c
# print("a:" + a)
# print("b:" + b)

# print("welcome to the band name generator")
# city=input("which city did you grow up in?\n")
# pet=input("What is your pet name ?\n")
#
# print("your band name most be " + city +" " +pet)

# str_text="Hello World"
# print(str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str*10)
# print(str+" From BBU")
#Number
# a=1_000_000
# print(a)
# print(type(a))
# b=13.04
# print(type(b))
# print(b)
#
# val1=int("10")
# val2=int("20")
# total=val1+val2
# print(type(total))
# print("Total =" +str(total))
# print(len(str(total)))

# a=True
# print(bool(a))
# a=0.0
# print(bool(a))
# a=1.0
# print(bool(a))
# a=5
# b=10
# print(bool(a==b))
# a=10
# b=10
# print(bool(a==b))
# a=None
# print(bool(a))
# a=()
# print(bool(a))
# a={}
# print(bool(a))
# a="apple"
# print(bool(a))
# a=-5
# print(bool(a))
# num=input("Input two digit number :")
# res=int(num[0])+int(num[1])
# print("result :"+ str(res))



#Q 1 &=
a=12 #in binary 1100    10 in binary 1010
a=a&10
#perform bitwise and assigment opertaion
# 1100
# 1010
# 1st 1 and 1 =1
# 2nd 1 and 0 =0
# 3rd 0 and 1 =0
# 4th 0 and 0 =0
#and then we got new binary number 1000 equals 8 in decimal
print(a) # a =a&10 =8
#Q 2 |=
a=12 #in binary 1100    10 in binary 1010
a=a|10 #a|=10
#perform bitwise OR assigment opertaion
# 1100
# 1010
# 1st 1 OR 1 =1
# 2nd 1 OR 0 =1
# 3rd 0 OR 1 =1
# 4th 0 OR 0 =0
#and then we got new binary number 1110 equals 8 in decimal
print(a) # a |=10 =14
#Q 3 ^=
a=12
a^=10
#perform bitwise XOR assigment opertaion
# 1100
# 1010
# 1st 1 XOR 1 =0
# 2nd 1 XOR 0 =1
# 3rd 0 XOR 1 =1
# 4th 0 XOR 0 =0
#and then we got new binary number 0110 equals 8 in decimal
print(a) #a^=10 =6
#Q 4 >>=
a=32 #convert 32 to binary 00100000
a>>=5 #a=a>>5 mean shifting bits to the right by 5 positions result is 00000001
print(a) #result a=1
#Q 5 <<=
a=32 #convert 32 to binary 100000
a<<=5 #a=a>>5 mean shifting bits to the left by 5 positions result is 1000000000
print(a) #result a=1024

# identity Operator check operator
a=[1,2,3,4]
b=[1,2,3,4]
c=a
print("a is b :",a is b)
print("a is c :",a is c)

kg = input("Input your wieght :")
height





