math = input("math score")
math = int(math)
eng = input("english score")
eng = int(eng)
if math >= 90 and eng >=90:
    print("有獎")
elif math < 60 and eng <60:
    print("要處罰") 
else:
    print("再加油")
