import xlrd
import yaml


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


def load_yaml(file_path):
    with open(file_path, encoding='utf-8') as f:
        return yaml.safe_load(f)  # 把yaml文件转为字典格式
