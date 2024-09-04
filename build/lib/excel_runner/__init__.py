import openpyxl
import requests

timeout = 60  # 默认请求超时时间


def run_excel(excel_file):
    excel = openpyxl.load_workbook(excel_file)  # 加载excel
    sheet = excel.active  # 得到第一张表（Sheet1）

    session = requests.session()  # 使用session来保留登录后的Cookies（如果有）
    session.timeout = timeout  # 设置统一超时时间

    for index, line in enumerate(sheet.values):  # 遍历excel所有行（仅数据）
        if index == 0:  # 跳过标题行
            continue
        name, method, url, data, headers, verify, *_ = line  # 解包，舍弃第7列以后的值
        # 处理请求头
        if headers:
            try:
                headers = {line.split(':')[0].strip(): line.split(':')[1].strip()
                           for line in headers.split('\n')}
            except Exception as ex:
                print('请求头格式异常：', ex)
        # 处理请求数据，为支持中文数据，需要将文本按utf-8编码为bytes
        if data is not None:
            data = data.encode('utf-8')

        # 发送请求
        print(f'请求第{index + 1}行接口: {name}')

        try:
            res = session.request(method, url, data=data, headers=headers)  # 使用同一个session发送请求，以保留过程中的Cookies
        except Exception as ex:
            result = 'ERROR'
            print('请求异常：', ex)
        else:
            result = 'PASS'
            print('响应：', res.text)

            # 处理断言
            if verify:  # 如果存在断言描述
                lines = verify.split('\n')  # 按行分割转为列表
                for line in lines:
                    if not line:  # 跳过空行
                        continue
                    try:
                        assert eval(line)  # 使用eval()来计算表达式的值
                    except AssertionError:
                        print("断言出错")
                        result = "FAIL"
                        break  # 该条断言失败后，后面的断言不再执行
                    except Exception as ex:
                        print("断言异常：", ex)
                        result = "ERROR"
                        break  # 该条断言失败后，后面的断言不再执行
                    finally:
                        print('执行断言：', line, '结果：', result)

        sheet.cell(index + 1, 7).value = result  # 在当前行第7列写入结果
    excel.save(excel_file)  # 保存并覆盖原文件

