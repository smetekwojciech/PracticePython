# Ask the user for a string and print out whether this string is a palindrome or not.

user_string=input("Please enter your string...")

user_string_reverse=user_string[::-1]

if user_string==user_string_reverse:
    print("Your string is a palindrome.")
elif user_string!=user_string_reverse:
    print("Your string is not a palindrome.")