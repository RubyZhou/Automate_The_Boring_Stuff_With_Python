#！python3
# ------------------------------------------------------------
# Filename  :
# Funcition : 多重剪切板
#   Usage:
#       py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.
# CREATE    :
# DESC      :
# HISTORY   :
# ------------------------------------------------------------

import os, shelve, pyperclip, sys

os.chdir('D:\\temp\\project')

mcbShelf = shelve.open('mcb')


if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    # TODO: Save clipboard content.
    # TODO: 输入 3 个参数，用key保存剪切板内容
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: 输入 2 个参数
    # TODO: List keywords and load content.
    if sys.argv[1].lower == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])



mcbShelf.close()