from lib.excelmanage import readExcel
import json
from lib.courseLib import addcourse,add2course,listcourse,deletecourse,modifycourse
import time
def sendcourserequest(row,sessionID):
    data=json.loads(row[5])
    dictBody = []
    if(row[4]=='add'):
        randomster=str(int(time.time()*10000))
        coursename=data['name']
        coursename=(coursename).replace('{{courseName}}',randomster)
        dictBody = addcourse(coursename, data['desc'], data['display_idx'], sessionID)
    elif (row[4] == 'list'):
        dictBody = listcourse(data['pagenum'], data['pagesize'], sessionID)
    elif (row[4] == 'delete'):
        dictBody = deletecourse(data['id'], sessionID)
    # return 结果
    return dictBody