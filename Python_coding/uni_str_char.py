def if_string_has_uni_char(string):
    s = sorted(string)
    print(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


string = 'abcds fjhdsj'
print(if_string_has_uni_char(string))