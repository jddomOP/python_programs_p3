def implement(s, sub):
    for i in range(len(s) - len(sub), -1, -1):
        if s[i:i+len(sub)] == sub:
            return i


