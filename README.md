# excel-runner

Run Http requests list in excel sheet



## testdata format

| SN  | MODULE | TITLE     | URL                                                                                            | METHOD | PARAMS | HEADERS | DATA | JSON                                                                            | SETUP                                                               | ASSERT                                                                                                              | TEARDOWN                            | STATUS | ERROR_MSG |
| --- | ------ | --------- | ---------------------------------------------------------------------------------------------- | ------ | ------ | ------- | ---- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------ | --------- |
| 1   | 添加加油卡  | 接口、参数正确   | [http://115.28.108.130:8080/gasStation/process](http://115.28.108.130:8080/gasStation/process) | POST   |        |         |      | {"dataSourceId":"bHRz","methodId":"00A","CardInfo":{"cardNumber":"1234567890"}} | db.del_card_if_exist('1234567890')                                  | res['code'] == 200  <br>res['msg'] == "添加卡成功"  <br>res['success'] is False  <br>db.check_card('1234567890') is True | db2.del_card_if_exist('1234567890') |        |           |
| 2   | 添加加油卡  | 参数相同，重复添加 | http://115.28.108.130:8080/gasStation/process                                                  | POST   |        |         |      | {"dataSourceId":"bHRz","methodId":"00A","CardInfo":{"cardNumber":"123456"}}     | db.execute('insert into cardinfo (`cardNumber`) values ("123456")') | res['code'] == 5000  <br>res['msg'] == "该卡已添加"  <br>res['success'] is False                                         |                                     |        |           |
