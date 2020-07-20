
from commonTools.readExcel import ReadExcel
import requests
import json

class SendRequests():

    def sendRequests(self,s,apiData):
        method = apiData["method"]
        url = apiData["url"]
        if apiData["params"] == "":
            par = None
        else:
            par = eval(apiData["params"])

        if apiData["headers"] == "":
            h = None
        else:
            h = eval(apiData["headers"])

        if apiData["body"] == "":
            body_data = None
        else:
            body_data = eval(apiData["body"])

        ytype = apiData["ytype"]
        v = False
        if ytype == "json":
            body = json.dumps(body_data)
        if ytype == "data":
            body = body_data
        else:
            body = body_data

        #发送请求
        re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
        return re

if __name__ == '__main__':
    s = requests.session()
    testData = ReadExcel.readExcel("E:\MyPython\project\MyAPiProject\execldata\login.xlsx","Sheet1")
    print(testData[0])
    response = SendRequests().sendRequests(s,testData[0])
    print(response)