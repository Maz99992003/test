n1= int(input("Eneter a number:"))
n2= int(input("Eneter a number:"))
n3= int(input("Eneter a number:"))

if n1 > n2:
    if n1 > n3 :
        print("n1")
else:
    if n2 > n3 :
        print("n2")
    elif n2 > n3:
        print("n2")
    else:
        if n3 > n2:
            print("n3")
        elif n3 > n1:
            print("n3")

