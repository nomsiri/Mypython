#โปรแกรมหาพื้นที่สามเหลี่ยม 1/2*ฐาน*สูง
def triangle(base, height):
    area = 1/2*base*height
    #print("พื้นที่สามเหลี่ยม, %d" % area)
    return area

b = int(input("รับค่าฐาน"))
h = int(input("รับค่าสูง"))
print("พื้นที่สามเหลี่ยม %d" % triangle(2,3))
triangle(5,10)
triangle(2,3)