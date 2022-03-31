def swap_case(s):
    return s.swapcase()

def withoutswap(s):
    new=""
    for i in range (0,len(s)):
        if(s[i].isupper()):
            new +=s[i].lower()
        elif(s[i].islower()):
            new +=s[i].upper()
        else:
            new+=s[i]
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    result = withoutswap(s)
    print(result)
