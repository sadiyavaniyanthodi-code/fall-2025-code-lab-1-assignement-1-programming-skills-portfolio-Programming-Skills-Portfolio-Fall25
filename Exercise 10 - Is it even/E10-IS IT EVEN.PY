## Exercise 10: Is it even? - 35 Marks

def is_even(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."


def main():
    num = int(input("Enter a number: "))
    result = is_even(num)
    print(result)


if __name__ == "__main__":
    main()