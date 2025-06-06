#!/usr/bin/env python3

#!/usr/bin/env python3

def first_five(string):
    return str(string)[:5]

def last_seven(string):
    return str(string)[-7:]

def middle_number(number):
    num_str = str(number)
    if '.' in num_str:
        # For floats like 1.50 → extract middle two characters around the decimal
        decimal_index = num_str.index('.')
        return num_str[decimal_index:decimal_index + 2]
    else:
        # For integers like 1500 → extract middle 2 digits
        mid = len(num_str) // 2
        return num_str[mid - 1:mid + 1]

def first_three_last_three(str1, str2):
    return str1[:3] + str2[-3:]

