def leapyear(year: int) -> bool:
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    year = int(input("Enter a year: "))
    if leapyear(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()