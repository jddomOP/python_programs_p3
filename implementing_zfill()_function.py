def implement_zfill(s, width):
    return '0' * (width - len(s)) + s if len(s) < width else s
