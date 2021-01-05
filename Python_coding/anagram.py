def is_angaram(s1,s2):
    if sorted(s1) == sorted(s2):
        print('strings are anagram')
    else:
        print('strings are not angaram' )


s1 = input()
s2 = input()
is_angaram(s1,s2)