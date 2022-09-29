def valid_braces(string):
    if len(string) % 2 == 0:
        d = {'(': ')', '{': '}', '[': ']'}
        a = len(string) / 2
        sstring = []
        for j in range(len(string)):
            sstring.append(string[j])
        print(sstring)
        for i in range(int(a)):
            if sstring[i] == d.get(sstring[i + 1]):
                sstring.pop(i)
                sstring.pop(i)
            else:
                pass
        print(sstring)
        if len(sstring) > 0:
            res = False
        else:
            res = True
    else:
        res = False
    return res


aa = '()'
print(valid_braces(aa))
