
# Write a simple program to determine if a given year is leap year. using user input.


year = int(input("Enter a Year:  "))

if (year%4 ==0 and year%100 != 0) or (year%400==0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a leap year")