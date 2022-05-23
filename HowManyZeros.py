#Program 7 How Many Zeros 
#Eboni Huggins
#April 1, 2022

target = int(input("What is the target value?"))
def count_Zeros(num):   
#https://coes.latech.edu/wp-content/uploads/sites/7/2018/07/130-student.pdf
#https://www.w3schools.com/python/
    zeros = 0
    while num > 0:
        if num % 10 == 0:
            zeros += 1
        num = num // 10
    return zeros
n = 1
count = 0
while n <= target:
    count += count_Zeros(n)
    n += 1
#https://www.kite.com/python/answers/how-to-add-commas-to-a-number-in-python
print ("The number of zeros written from 1 to {:,} is {:,}. " .format(target, count))
