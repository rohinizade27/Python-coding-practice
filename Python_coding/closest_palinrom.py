# examples: lets take 911
# Ignore the last 1 we only take the first half (round up). so 91X.
# Replace X with 9. we have 919. this is out mid point.
# We know our original 911 is less than 919 so subtract 1 from our middle number so we get our second (lower bound) 909.
# Compare 911 - 919 and 911 - 909
# return the one with the smallest difference


def is_palindrom(num):
    return  True if str(num) == str(num)[::-1] else False


def closest_palindrom(num):
    lpnum = num-1
    while(not(is_palindrom(abs(lpnum)))):
        lpnum -= 1

    spnum = num + 1
    while (not (is_palindrom(abs(spnum)))):
        spnum += 1

    if abs(num-lpnum) > abs(num-spnum):
        return spnum
    else:
        return lpnum

num = int(input())
print(closest_palindrom(num))