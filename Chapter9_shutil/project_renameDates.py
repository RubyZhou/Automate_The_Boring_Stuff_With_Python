#！python3
# ------------------------------------------------------------
# Filename  :
# Funcition : 将带有美国风格日期的文件改名为欧洲风格日期(MM-DD-YYYY => DD-MM-YYYY)
# CREATE    :
# DESC      :
# HISTORY   :
# ------------------------------------------------------------


import shutil, os, re

# TODO: 创建一个美国日期风格的正则表达式
datePattern=re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
""", re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing