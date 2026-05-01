# Palindrome Program

def palindrome(s):
    k = ""

    for i in s.lower():
        if i.isalnum():
            k += i

    return k == k[::-1]


def display(a):
    if a:
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")


while True:
    s = input("Enter a string: ")

    if s.strip() == "":
        print("Input should not be empty.")
    else:
        break

a = palindrome(s)
display(a)