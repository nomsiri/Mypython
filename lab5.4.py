def beforMidterm(a,b,c):
    bm = a+b+c
    return bm
    
scroe = int(input("คะแนนเก็บ:"))
jitpisai = int(input("คะแนนจิตพิสัย:"))
midterm = int(input("คะแนนกลสงภาค:"))
print("sum: %.2f " % beforMidterm(scroe,jitpisai,midterm))