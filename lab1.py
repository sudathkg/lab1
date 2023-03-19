# 1 --------------optimized code to performance using only one variable------------------
x=float(input("Input number 1"))
x=x+float(input("Input number 2"))
print("summation is " ,x)

# 2 ========less performanced but more readable code==============
input1=(input("Input number 1"))
input2=(input("Input number 2"))

num1=float(input1)
num2=float(input2)

sum=num1+num2
print("summation is " , sum)

#3 =========balanced performance and readable=======================
num1=float(input("Input number 1"))
num2=float(input("Input number 2"))
print("summation is " ,num1+num2)
