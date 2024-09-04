from excel_runner import run_excel


def test_excel_runner():
    run_excel("testdata/data.xls", "testdata/output.xls", base_url='http://127.0.0.1/add')