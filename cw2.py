def get_middle(s):
    if len(s) % 2 == 1:
        res = s[int(abs(len(s)/2))]
    else:
        res = s[int(len(s)/2) - 1] + s[int(len(s)/2)]
    return res


a = '1ff1'
print(get_middle(a))