def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    return str2 in (str1 + str1)


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if is_rotation(str1, str2):
    print("The second string is a rotation of the first string.")
else:
    print("The second string is not a rotation of the first string.")

