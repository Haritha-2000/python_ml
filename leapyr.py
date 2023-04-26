#for collecting input from the user
year = int(input("Enter a number: "))
#checking conditional statement
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
