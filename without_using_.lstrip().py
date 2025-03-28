#before i start, I searched the ff. codes and are still in the process of learning it

def custom_lstrip(s):
    word = 0
    while word < len(s) and s[word] == ' ':
        word += 1
    return s[word: ]

print(custom_lstrip("       hello world"))

