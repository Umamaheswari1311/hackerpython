def mutate_stringToList(string, position, character):
    l=list(string)
    l[position]=character
    string = ''.join(l)
    return string

def mutate_stringSlice(string, position, character):

    return string[:position]+ character+ string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_stringToList(s, int(i), c)
    print(s_new)
    s_newval = mutate_stringSlice(s, int(i), c)
    print(s_newval)