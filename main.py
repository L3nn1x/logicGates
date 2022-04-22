from LogicGates import LogicGates
lg = LogicGates()
test_1 = [21!=21, False, 'run' in 'notron', []==()] # [False, False, False, False]
test_2 = [1+1==2, 'lol'+''=='lol', 'yes'=='yes'] # [True, True, True]
test_3 = [1+1==1, 'lol', 'yes'=='yess', 3>1] # [False, True, False, True]
alltest = [test_1, test_2, test_3]
gates = {}

print(['OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'AND'])
for t in alltest:
    all_gates = [lg.OR(t), lg.NOT(t, t), lg.NAND(t), lg.NOR(t), lg.XNOR(t), lg.XOR(t), lg.AND(t)]
    print(all_gates)