def remove_char(char_to_remove,string):
    lower_case_str=string.lower()
    new_str =""
    for char in char_to_remove:
        lower_case_char = char.lower()
        new_str = lower_case_str.translate({ord(lower_case_char): None})
        lower_case_str = new_str
    print(new_str)


char_to_remove =['T','E']
string= 'Thinkbumblebee Analytics'
remove_char(char_to_remove,string)