num1 = 0
num2 = 1
count = 2
print(num1)
print(num2)
while count < 10:
    next_fibonacco =  num1 + num2
    print (next_fibonacco)
    num1 = num2
    num2 = next_fibonacco
    count += 1

