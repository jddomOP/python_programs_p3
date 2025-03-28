def implement_isupper(s):
    for char in s:
        if 'a'<= char <= 'z':
            return False
        return True if s else False

print(implement_isupper("HELLO"))
print(implement_isupper("hello"))