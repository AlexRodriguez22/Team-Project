#############
# How Many Zeros
# Alex Rodriguez
# Count all zeros from 1 to a number via user input 
#############
def totalZeros(user_input):
    numList = range(1, user_input +1)
    count = 0
    for nums in numList:
        nums = str(nums)
        for i in nums:
            i = i.split()
            if i == ['0']:
                count += 1
    return(count)
        

user_input = int(input("What is the target value?: "))
print("The number of zeros written from 1 to {:,} is {:,}.".format(user_input, totalZeros(user_input)))