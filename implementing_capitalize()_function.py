def implement_capitalize(s):
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

print(implement_capitalize("HEllO WORLD"))

