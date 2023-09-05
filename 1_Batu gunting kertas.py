N = input("")

if N == ("[] ()"):
    print ("Pemain A menang")
elif N == ("() []"):
    print ("Pemain B menang")
elif N == ("[] 8<"):
    print ("Pemain B menang")
elif N == ("8< []"):
    print ("Pemain A menang")
elif N == ("() 8<"):
    print ("Pemain A menang")
elif N == ("8< ()"):
    print ("Pemain B menang")
else:
    print("Draw")
