import re
nameid=input("Nhập vào chuỗi tên và id: ")
id=[]
id=re.sub(r'\D','', nameid)
l=re.findall(r'\d',id)
t=tuple(l)
print("Mã sinh viên là:",id)
print (l)
print (t)