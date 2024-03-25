def check_palindrome(string):
    return (string == string[::-1])


string=input()
a=check_palindrome(string)

print(a)