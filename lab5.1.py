def rectangle(w, l):
    area = w * l
    return area

w = int(input("กว้าง:"))
l = int(input("ยาว:"))
print("พื้นที่สี่เหลี่ยม %d" % rectangle(w,l))