def is_palindrome(num):
    s = str(abs(num))
    return s == s[::-1]


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        if is_palindrome(n):
            print(f"{n} is a palindrome")
        else:
            print(f"{n} is not a palindrome")
    except ValueError:
        print("Invalid input")