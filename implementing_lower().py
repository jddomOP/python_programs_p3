def implement_lower(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) +  32)
        else:
            result += char
        return result

print(implement_lower("Hello WORLD!"))
