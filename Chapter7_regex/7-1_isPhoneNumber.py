import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 6):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

#print('415-555-4242 is a phone number:')
#print(isPhoneNumber('415-555-4242'))
#print('Moshi moshi is a phone number:')
#print(isPhoneNumber('Moshi moshi'))

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

for i in range(len(message)):
    chunk = message[i:i+12] # 表示取字符串字串,从第 i 位开始取向后12位
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

print('Done')

# 使用正则表达式的方法
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found :' + mo.group())


print("分组>>>>>>>>>>>")
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found :' + mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.groups())












