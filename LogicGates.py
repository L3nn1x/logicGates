class LogicGates:

    def OR(self, *objects_):
        booleans = []
        list(objects_)
        for ob in list(objects_).pop():
            if ob:
                booleans.append(True)
            elif not ob:
                booleans.append(False)

        if True in booleans and False in booleans:
            return True
        elif False in booleans and True not in booleans:
            return False
        if True in booleans and False not in booleans:
            return True

    def NOR(self, *objects_):
        booleans = []

        for ob in list(objects_).pop():
            if ob:
                booleans.append(True)
            if not ob:
                booleans.append(False)

        if False in booleans and True not in booleans:
            return True
        elif True in booleans and False in booleans:
            return False
        elif True in booleans and False not in booleans:
            return False

    def XNOR(self, *objects_):
        booleans = []

        for ob in list(objects_).pop():
            if ob:
                booleans.append(True)
            if not ob:
                booleans.append(False)

        if False in booleans and True not in booleans:
            return True
        elif True in booleans and False in booleans:
            return False
        elif True in booleans and False not in booleans:
            return True

    def AND(self, *objects_):
        booleans = []

        for ob in list(objects_).pop():
            if ob:
                booleans.append(True)
            if not ob:
                booleans.append(False)

        if False in booleans and True not in booleans:
            return False
        elif True in booleans and False in booleans:
            return False
        elif True in booleans and False not in booleans:
            return True

    def NAND(self, *objects_):
        booleans = []

        for ob in list(objects_).pop():
            if ob:
                booleans.append(True)
            if not ob:
                booleans.append(False)

        if False in booleans and True not in booleans:
            return True
        elif True in booleans and False in booleans:
            return True
        elif True in booleans and False not in booleans:
            return False

    def NOT(self, obj_A, obj_B):
        if obj_A is not obj_B:
            return True
        elif obj_A is obj_B:
            return False

    def XOR(self, *objects_):
        booleans = []

        for ob in list(objects_).pop():
            if ob:
                booleans.append(True)
            if not ob:
                booleans.append(False)


        if False in booleans and True not in booleans:
            return False
        elif True in booleans and False in booleans:
            return True
        elif True in booleans and False not in booleans:
            return False

"""
lg = LogicGates()
test_1 = [21!=21, False, 'run' in 'notron', []==()] # [False, False, False, False]
test_2 = [1+1==2, 'lol'+''=='lol', 'yes'=='yes'] # [True, True, True]
test_3 = [1+1==1, 'lol', 'yes'=='yess', 3>1] # [False, True, False, True]


print(lg.OR(test_2))
print(lg.XOR(test_3))
print(lg.NOR(test_1))
print(lg.XNOR(test_3))
print(lg.AND(test_2))
print(lg.NAND(test_1))
"""