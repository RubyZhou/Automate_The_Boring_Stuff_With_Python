#！python3
# ------------------------------------------------------------
# Filename  :
# Funcition : 将一个文件夹备份到一个ZIP 文件
# CREATE    :
# DESC      :
# HISTORY   :
# ------------------------------------------------------------

import zipfile, os
def bakupToZip(folder):
    bakdir = "E:\\我的文档备份"
    os.chdir(bakdir)

    folder = os.path.abspath(folder)

    # TODO: 遍历文件名
    #for name in os.listdir(folder):
    #   print(name)

    # TODO：获取文件序号
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO: 创建 zip 文件
    print('Creating %s ...' % (zipFilename))
    bakupZip=zipfile.ZipFile(zipFilename, 'w')

    # TODO: 遍历目录树并且添加到 zip 文件中
    for foldername, subfolders, filenames in os.walk(folder):
        print('\tAdding files in %s ...' % (foldername))
        bakupZip.write(foldername)
    for filename in filenames:
        print('\t\tAdding file %s ....' %(filename))
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue
        bakupZip.write(os.path.join(foldername, filename))

    bakupZip.close()
    print('Done.')

bakupToZip('D:\\我的文档\\工作\\周报\\2017')


