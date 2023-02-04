Email = input(("Email:"))
lg=len(Email)
if lg<=20 and lg >= 10: 
    print("pass")
else:
        print("fail")


if Email.index("@"):
    print("Vaild")
else:
    print("Not Vaild")


