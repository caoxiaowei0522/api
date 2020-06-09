#环境清除
from lib.loginLib import loginlib
from lib.courseLib import addcourse,listcourse,deletecourse,modifycourse
import json
import time
from lib.sendcourserequset import sendcourserequest
from lib.excelmanage import readExcel,getnewexcel
sessionID = loginlib('auto', 'sdfsdfsdf')
retList = listcourse(1, 400,sessionID)
num = 0
for data in retList['retlist']:
    deletecourse(data['id'],sessionID)
    num = num + 1
print('本次共删除了:', num, '条数据')