def is_palindrome(string):
    return string == '' .join(reversed(string))

string=input()
print(is_palindrome('string'))
