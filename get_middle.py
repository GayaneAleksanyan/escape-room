def get_middle(s):
    if len(s) % 2 != 0:
        return s[len(s) // 2]
    else:
        return s[len(s)//2 - 1 : len(s)//2 + 1]


print (get_middle("test"))