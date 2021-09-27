from logic import TruthTable

#write a Python program that asks the user to enter two propositions,
    #where both propositions the variables p and q
#then determine whether or not thetwo propositions are equivalent, and report the result.

prop1 = input("Please enter proposition 1: ")
prop2 = input("Please enter proposition 2: ")

comparisonTable = TruthTable([prop1, prop2])


if comparisonTable.table[0][1][0] == comparisonTable.table[0][1][1]:
    if comparisonTable.table[1][1][0] == comparisonTable.table[1][1][1]:
        if comparisonTable.table[2][1][0] == comparisonTable.table[2][1][1]:
            if comparisonTable.table[3][1][0] == comparisonTable.table[3][1][1]:
                print("Proposition is equivalent.")
            else:
                print("Proposition is not equivalent.")
        else:
            print("Proposition is not equivalent.")
    else:
        print("Proposition is not equivalent.")
else:
    print("Proposition is not equivalent.")
    
