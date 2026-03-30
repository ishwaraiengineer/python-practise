#wap for check palindrom
txt = input("enter your text here:-")

if txt == txt[::-1]:
    print ("its a paindrom")
else:
    print ("its not palindrom")