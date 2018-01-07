#！python3
# ------------------------------------------------------------
# Filename  : phoneAndEmail.py
# Funcition : 在剪切板匹配电话号码和email
# CREATE    :
# DESC      :
# HISTORY   :
# ------------------------------------------------------------
import pyperclip, re

# step1 : 创建电话号码的正则表达式

phoneRegex = re.compile(r'''( # 分组
                (\d{3}|\(\d{3}\))?  # 地址码 > 三个数字 或 带括号的三个数组
                (\s|-|\.)?          # separator > 分隔符 
                (\d{3})             # 前三个数字
                (\s|-|\.)           # separator > 分隔符
                (\d{4})             # 最后四个数字
                (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension 扩展 > n 个空格符，ext|x|ext+任意字符 + n各个空格 + 2-5个数字
            )''', re.VERBOSE)

# step2 : 创建 Email 的正则表达式
emailRegex = re.compile(r'''(
                [a-zA-Z0-9._%+-]+
                @
                [a-zA-Z0-9.-]+
                (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# step3 : 在剪贴板文本中找到所有匹配
text = str(pyperclip.paste())   # 将剪切板中文本赋值给变量
matches = []

# 处理电话号码
for groups in phoneRegex.findall(text): # print(groups) >> ('415-863-9900', '415', '-', '863', '-', '9900', '', '', '')
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # > 字符串的 join() 方法：将参数列表用 分隔符 连接起来
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    # > 列表的 append() 方法：向列表中增加值。 补充：insert(1，str) 可以在列表的任意位置增加值
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')