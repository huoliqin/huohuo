import os
print(__file__)
currpath = os.path.realpath(__file__) #根据系统获取绝对路径

print(currpath)

parpath = os.path.dirname(currpath) #获取文件夹层

casespath = os.path.join(parpath, "cases")

print(casespath)

reportpath = os.path.join(parpath, "report")

print(reportpath)