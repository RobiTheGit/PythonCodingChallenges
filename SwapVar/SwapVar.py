#!/usr/bin/python3
def SwapVar(Var1, Var2):
    Var1 = Var1-Var2
    Var2 = Var1+Var2
    Var1 = Var2-Var1
    print("Var1", Var1,"Var2", Var2)
SwapVar(2,6)
