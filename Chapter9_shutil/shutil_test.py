import os, shutil, send2trash, zipfile

os.chdir('D:\\temp\\project')


# 复制文件和文件夹
#shutil.copytree('D:\\temp\\project\\mysite', 'D:\\temp\\project\\mysite_bak')

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is a temp file')
baconFile.close()
send2trash.send2trash('bacon.txt')

print(os.listdir())

print("---------------------------------------------------------------")

for folderName, subfolders, filenames in os.walk('D:\\temp\\NoteHighLight_x64'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')

print("---------------------------------------------------------------")
send2trash.send2trash('D:\\temp\\project\\mysite_bak.zip')
os.chdir('D:\\temp\\project')
exampleZip = zipfile.ZipFile('mysite_bak.zip', 'a')
exampleZip.write('mysite_bak', compress_type=zipfile.ZIP_DEFLATED)
exampleZip.write('善用佳软.mobi', compress_type=zipfile.ZIP_DEFLATED)
exampleZip.close()
print("文件压缩完毕")

exampleZip=zipfile.ZipFile('mysite_bak.zip')
print("文件列表：", exampleZip.namelist())
spamInfo = exampleZip.getinfo('善用佳软.mobi')
print("压缩前文件大小:", spamInfo.file_size)
print("压缩后文件大小:", spamInfo.compress_size)
print("压缩率：", round(spamInfo.compress_size/spamInfo.file_size, 4) * 100, "%")
exampleZip.close()


exampleZip=zipfile.ZipFile('mysite_bak.zip')
exampleZip.extractall( 'D:\\temp\\project\\解压')
