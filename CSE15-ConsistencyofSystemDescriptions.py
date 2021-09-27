from logic import TruthTable
# A set of propositions are said to be inconsistent when:
# none of the truth assignments that makes ex.(p ∨ q) true makes ex.(¬p ∧ ¬q) true;

inputProps = []
#Start by asking user for propositions 
morePropositions = True
while morePropositions == True:
    inputProps += [input("Enter a propositon:")]
    keepGoing = input("Would you like to enter another proposition? <Y,N>")
    if keepGoing == "N" or keepGoing == "n":
        morePropositions = False

#Create truth tables to evaluate consistency
consistencyTable = TruthTable(inputProps).table
evaluatedLogic = []
for tfVariables in consistencyTable:
    evaluatedLogic += [tfVariables[1]]

print(evaluatedLogic)


for checkingConsistency in evaluatedLogic:
    if sum(checkingConsistency) == len(checkingConsistency):
        isConsistent = True
        break
    else:
        isConsistent = False
    

if isConsistent == True:
    print("Proposistions are consistent")
else:
    print("Proposistions are NOT consistent")