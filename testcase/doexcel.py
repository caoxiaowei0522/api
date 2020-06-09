from xlutils.copy import copy
from lib.excelmanage import readExcel,getnewexcel
from lib.sendcourserequset import sendcourserequest
from lib.loginLib import loginlib
import json
from config import savepath,path,path1
#得到一个新工作簿
newworkbook=getnewexcel(path)
workneet=newworkbook.get_sheet(0)
list=readExcel(path,0)
print(list)
sessionID=loginlib('auto','sdfsdfsdf')
for i in range(0,len(list)):
    row=list[i]
    print(row)
    ret=sendcourserequest(row,sessionID)
    print(ret)
    data1=json.loads(row[6])
    print(data1)
    if ret['retcode']==data1['code']:
        print(row[0]+'测试通过')
        workneet.write(i+1, 7 ,'测试通过')
    else:
        print(row[0]+'测试不通过')
        workneet.write(i + 1, 7, '测试不通过')
        if 'reason' in ret.keys():  # 测试不通过,不一定有原因,所以要判断返回值字典中是否存在reason 的key
            workneet.write(i + 1, 8, ret['reason'])  # 把原因写入第i+1 行,第9列
newworkbook.save(savepath)