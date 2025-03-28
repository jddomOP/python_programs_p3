def implement_title(s):
    words = s.split()
    result = [word[0].upper() + word[1:].lower() if word else '' for word in words]
    return ' '.join(result)

#test
print(implement_title("hello world im jaydie"))

