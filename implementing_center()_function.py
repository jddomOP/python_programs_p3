def implement_center(s, width):
    spaces = max(width - len(s), 0)
    lspaces = spaces // 2
    rspaces = spaces - lspaces
    return ' '*lspaces + s + ' '*rspaces

print(implement_center("Hello", 10))


