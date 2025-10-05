'''validate Finnish Personal Identity Codes (PIC)

The program should check the validity by these three criteria:
The first half of the code is a valid, existing date in the format ddmmyy.
The century marker is either + (1800s), - (1900s) or A (2000s).
The control character is valid.

The control character is calculated by taking the nine-digit number created by the date of birth and the personal identifier, dividing this by 31, and selecting the character at the index specified by the remainder from the string 0123456789ABCDEFHJKLMNPRSTUVWXY. For example, if the remainder was 12, the control character would be C.'''

import datetime as dt

def is_it_valid(pic: str):
    z_pool = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    x_pool = '-+A'

    ddmmyy = pic[:6]
    print(f'ddmmyy={ddmmyy}')
    x = pic[6] # The century marker is either + (1800s), - (1900s) or A (2000s).
    id = pic[7:10] # personal id
    print(f'id={id}')
    z = pic[-1] # control char


    # check: length
    if len(pic) != 11:
        return False
    # check: id and ddmmyy are num
    numbers = pic[:6]+pic[7:10]
    for x in numbers:
        if x not in "0123456789":
            return False
    # check: x(century marker) and year
    if x in x_pool:
        if x == '-':
            yyyy = '18' + ddmmyy[-2:]
        elif x == '+':
            yyyy = '19' + ddmmyy[-2:]
        else:
            yyyy = '20' + ddmmyy[-2:]
    else:
        return False
    print(f'x, yyyy = {x, yyyy}')

    # check: if date is valid
    try:
        birth = dt.datetime(int(yyyy), int(ddmmyy[2:4]), int(ddmmyy[:2])) # year, month, day
        print(f'birth = {birth.date()}')
    except ValueError:
        print('ValueError fasle')
        return False
    
    # Check: The control character is valid
    remainder = int((ddmmyy + id)) % 31 # nine_digit % 31
    check_z = z_pool[remainder]
    # print(f'9digit = {int((ddmmyy + id))},remainder = {remainder}, check_z = {check_z}, z = {z}')
    if check_z == z:
        return True
    else:
        return False
    

if __name__ == "__main__":
    # print(is_it_valid('230827-906F')) # true
    print(is_it_valid('290200A1239')) # true
    # print(is_it_valid('030103A493DD')) # false