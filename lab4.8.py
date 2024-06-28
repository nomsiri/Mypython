def bmi(kg, cm):
    bmi = kg/(cm/100)**2
    return bmi

def compare(bmi):
    if bmi < 18.50 :
        return "น้ำหนักน้อย"
    elif bmi >= 18.5 and bmi <= 22.90:
        return "ปกติ(สุขภาพดี)"
    elif bmi >= 23 and bmi <= 24.90:
        return "ท้วม/โรคอ้วนระดับ1"
    elif bmi >= 25 and bmi <= 29.90:
        return "อ้วน/โรคอ้วนระดับ2"
    else:
        return "อ้วนมาก/โรคอ้วนระดับ3"

kg = int(input("รับค่าน้ำหนัก:"))
cm = int(input("รับค่าส่วนสูง:"))
print("ดัชนีมวลกาย %.2f" % bmi(kg,cm))
print("อยู่ในเกณฑ์: %s" % compare(bmi(kg,cm)))
