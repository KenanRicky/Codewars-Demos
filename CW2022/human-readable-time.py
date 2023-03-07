#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

#HH = hours, padded to 2 digits, range: 00 - 99
#MM = minutes, padded to 2 digits, range: 00 - 59
#SS = seconds, padded to 2 digits, range: 00 - 59
#The maximum time never exceeds 359999 (99:59:59)

#You can find some examples in the test fixtures.

# My Solution

def make_readable(sec):
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)
sec = 359999
print(make_readable(sec))