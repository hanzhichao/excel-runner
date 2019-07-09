import os
import json

import requests
import pytest
from utils.path import DATA_DIR
from utils.data import Excel

data_file = os.path.join(DATA_DIR, 'data.xls')


def json2dict(text):  # json字符串转字典
    text = text or '{}'  # 如果text为空, 则使用默认值 '{}'防止转字典报错
    try:
        return json.loads(text)
    except json.decoder.JSONDecodeError:
        print(f'{text}不是合法的json格式')


@pytest.mark.parametrize('case', Excel(data_file).get_sheet('执行用例'))
def test_fuel_card(db, case):
    print(f"执行用例: 编号: {case['SN']} 模块: {case['MODULE']} 标题: {case['TITLE']} ")

    # 组装并执行setup
    setups = case['SETUP']
    if setups:  # 如果setups不为空
        for line in setups.split('\n'):  # 将setups按换行符分割,然后遍历
            print(f'执行setup语句: {line.strip()}')
            eval(line.strip(), {}, {'db': db})

    # 组装请求
    print(f'发送请求 ......')
    res = requests.request(
        method=case['METHOD'],
        url=case['URL'],
        params=json2dict(case['PARAMS']),
        headers=json2dict(case['HEADERS']),
        data=json2dict(case['DATA']),
        json=json2dict(case['JSON'])
    ).json()

    ass = case['ASSERT']
    if ass:
        for line in ass.split('\n'):  # 将ass按换行符分割,然后遍历
            print(f'执行断言语句: {line.strip()}')
            assert eval(line.strip(), {}, {'db': db, 'res': res})

    teardowns = case['TEARDOWN']
    if teardowns:  # 如果setups不为空
        for line in teardowns.split('\n'):  # 将setups按换行符分割,然后遍历
            print(f'执行teardown语句: {line.strip()}')
            eval(line.strip(), {}, {'db': db})

if __name__ == '__main__':
    pytest.main(['test_excel.py', '--html=report.html'])