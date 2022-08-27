sum1 = float(input("Enter a number: "))
operator = input("Enter a valid operator: ")
sum2 = float(input("Enter another number: "))

if operator == "+":
    print(sum1 + sum2)

elif operator == "-":
    print(sum1 - sum2)
    
elif operator == "*":
    print(sum1 * sum2)
    
elif operator == "/":
    print(sum1 / sum2)
    
else: 
    print("E be like say you no know wetin operator be :( ")
