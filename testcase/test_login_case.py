
import requests
from commonTools.readExcel import ReadExcel
from commonTools.sendRequests import SendRequests
from testcase.BaseCase import BaseCase
from path_dir import execl_dir
from ddt import ddt,data,unpack

excelpath = execl_dir+"\\login.xlsx"
testData = ReadExcel.readExcel(excelpath, "Sheet1")

@ddt
class test_login_case(BaseCase):
    def setUp(self):
        super().setUp()
        self.s = requests.session()
        # super(test_login_case, self).setUp()

    def tearDown(self):
        super().setUp()

    @data(*testData)
    def test_login(self,data):
        # res = requests.get("http://www.httpbin.org/get?a=1&b=2")
        res = SendRequests().sendRequests(self.s, data)
        print(res.text)
        self.logger.info(''.join([self.log_cur_name(), " - response : ", res.text]))


