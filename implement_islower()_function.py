def implement_islower(s):
    for char in s:
        while 'a' <= char <= 'z':
                return True
        return False

    #Test
    print(implement_islower("HELLO"))
    print(implement_islower("hello"))