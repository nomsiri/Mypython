def bmi(kg, cm):
    BMI = kg/(cm/100)**2
    return BMI

kg = int(input("kelogram "))
cm = int(input("height "))
print("BMI %.2f" % bmi(kg, cm))
