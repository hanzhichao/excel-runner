import requests
import xlrd
from xlutils.copy import copy
base_url = 'http://127.0.0.1:5000'


def run_excel(path):
    wb = xlrd.open_workbook(path) #xlrd新版本支持读取.xlsx
    # wb = xlrd.open_workbook("接口测试用例.xlsx", formatting_info=True) # xlrd现在不支持带格式拷贝
    sh = wb.sheet_by_index(0)
    wb2 = copy(wb)
    sh2 = wb2.get_sheet(0)
    for i in range(1, sh.nrows):
        url = base_url + sh.cell(i,2).value
        data = {"a": sh.cell(i,3).value, "b": sh.cell(i,4).value}
        if sh.cell(i,1).value == 'get':
            response = requests.get(url=url, data=data)
        elif sh.cell(i,1).value == 'post':
            response = requests.post(url=url, data=data)
        try:
            assert response.text == str(sh.cell(i,5).value)
            sh2.write(i,7, "PASS")
        except AssertionError:
            sh2.write(i,7, "FAIL")
        finally:
            sh2.write(i,6, response.text)
            wb2.save("用例执行结果.xls") # xlutils不支持保存未.xlsx


if __name__ == "__main__":
    run_excel("data.xlsx")
