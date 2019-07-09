import openpyxl


class Excel(object):
    def __init__(self, file_path):
        self.wb = openpyxl.load_workbook(file_path)

    def get_sheet(self, sheet_name):
        sh = self.wb.get_sheet_by_name(sheet_name)
        # sh = self.wb[sheet_name]
        title_data = [cell.value for cell in sh[1]]
        data = []
        for row in sh.iter_rows(min_row=2):
            row_data = [cell.value for cell in row]
            data.append(dict(zip(title_data, row_data)))
        return data





if __name__ == '__main__':
    excel = Excel('data.xlsx')
    data = excel.get_sheet('执行用例')
    print(data)
    # for case in data:
    #     print(case['TITLE'])
    # data = load_yaml()
    # print(data['test_add_fuel_card'])
