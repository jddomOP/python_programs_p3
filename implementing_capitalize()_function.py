def implement_capitalize(s):
    if not s:
        return s
    return s[0].upper() + custom_lower(s[1:])

print(implement_capitalize("HEllO WORLD"))

