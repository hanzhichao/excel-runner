import os

import xlrd
import yaml

from utils.path import DATA_DIR


class Excel(object):
    def __init__(self, file_path):
        self.wb = xlrd.open_workbook(file_path)

    def get_sheet(self, sheet_name):
        sh = self.wb.sheet_by_name(sheet_name)
        title = sh.row_values(0)
        data = []
        for row in range(1, sh.nrows):
            case_data = sh.row_values(row)
            data.append(dict(zip(title, case_data)))
        return data


def load_yaml(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, encoding='utf-8') as f:
        return yaml.load(f)  # 把yaml文件转为字典格式


if __name__ == '__main__':
    pass
    # excel = Excel('data.xls')
    # data = excel.get_sheet('添加加油卡')
    # print(data)
    # for case in data:
    #     print(case['TITLE'])
    # data = load_yaml()
    # print(data['test_add_fuel_card'])
