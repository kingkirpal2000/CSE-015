numList = []
oddList = []
for i in range(10):
    numList.append(int(input("Please enter an integer: ")))
for numbers in numList:
    if numbers % 2 != 0:
        oddList.append(numbers)

if len(oddList) >= 1:       
    print(max(oddList))
else:
    print("No odd numbers were entered.")