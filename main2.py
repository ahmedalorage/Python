
#Tempertature = 35

#if Tempertature >= 35 :
 #   print("It is a hot day")
#else:
 #   print("It is not hot day")

Title = input("enter your name ? ")

if len(Title) < 3 :
    print("name must be at least 3 character")
elif len(Title) > 10 :
    print("name can not be maxumim than 10 character")
else:
    print("name looks good !")