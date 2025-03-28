def implement_center(s, width):
    spaces = max(widrh - len(s), 0)
    lspaces = spaces // 2
    rspaces = spaces - lspaces
    return ''*lspaces + s + ''*rspaces


