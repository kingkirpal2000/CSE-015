from logic import TruthTable


# not a
notA = TruthTable(["-a"])
notA.display()


#a and b
aAndb = TruthTable(["a and b"])
aAndb.display()

#a or b
aOrb = TruthTable(["a or b"])
aOrb.display()

#a implies b
aImpb = TruthTable(["a -> b"])
aImpb.display()

#material equivalence 
matEq = TruthTable(["a <-> b"])
matEq.display()