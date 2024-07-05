def Fa (c):
    F = (9/5)*c+32
    return F

def Kel (c):
    K = c + 273.15
    return K

C = int(input("C:"))
print("Fa: %.2f" % Fa(C))
print("Kel: %.2f" % Kel(C))