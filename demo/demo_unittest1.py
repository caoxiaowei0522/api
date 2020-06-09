import unittest
from lib.loginLib import loginlib
from lib.courseLib import addcourse,listcourse,deletecourse,modifycourse
import json
import time
from lib.sendcourserequset import sendcourserequest
from lib.excelmanage import readExcel,getnewexcel
from config import path
class  DemoUnittest(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        cls.clearData()

    @classmethod
    def setUpClass(cls):
        cls.clearData()

    @classmethod
    def clearData(cls):
        # 1-1 调用列出课程接口
        sessionID = loginlib('auto', 'sdfsdfsdf')
        retList = listcourse(1, 400,sessionID)
        num = 0
        # 1-2 循环删除课程
        for data in retList['retlist']:
            deletecourse(data['id'],sessionID)
            num = num + 1
        print('本次共删除了:', num, '条数据')

    @classmethod
    def clearDb(cls):
        pass;

    def test001(self):
        sessionID = loginlib('auto', 'sdfsdfsdf')
        retList = readExcel(path, 0)
        print(retList)
        for i in range(0, len(retList)):
            time.sleep(0.0001)
            row = retList[i]
            print(row)
            ret = sendcourserequest(row,sessionID)
            print(ret)
            colus7 = json.loads(row[6])  # 第7列的值
            print(colus7)
            if ret['retcode'] == colus7['code']:
                print(row[0] + '测试通过')
            else:
                print(row[0] + '测试不通过')
    def test003(self):
        sessionID = loginlib('auto', 'sdfsdfsdf')
        courseName = "大学英语" + str(int(time.time() * 10000))
        retList0 = listcourse(1, 400,sessionID)
        ret = addcourse(courseName, '课程描述', '0',sessionID)
        print(ret)
        self.assertEqual(ret['retcode'] ,0,'新增课程失败1')
        print(">>>>>新增课程测试通过1")
        retList1 = listcourse(1, 400,sessionID)
        self.assertEqual(retList0['total'] + 1,retList1['total'],'新增课程失败2')
        print(">>>>>新增课程测试通过3")
    @unittest.skip('skip的原因')
    def test002(self):
        print('方法二调用了')

