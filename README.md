# excel-runner

Run Http requests list in excel sheet



## how to use

Install excel-runner v0.1.2

```shell
pip install excel-runner==0.1.2
```


Create excel data file data.xlsx

| name      | method | url                                                                | data                        | headers                                         | verify                                                         | result |
| --------- | ------ | ------------------------------------------------------------------ | --------------------------- | ----------------------------------------------- | -------------------------------------------------------------- | ------ |
| get请求     | get    | [https://httpbin.org/get?a=1&b=2](https://httpbin.org/get?a=1&b=2) |                             |                                                 | res.status_code==200                                           |        |
| post-form | post   | [https://httpbin.org/post](https://httpbin.org/post)               | name=Kevin&age=1            | Content-Type: application/x-www-form-urlencoded | res.status_code==200  <br>res.json()['form']['name']=='Kevin'] |        |
| post-json | post   | [https://httpbin.org/post](https://httpbin.org/post)               | {"name": "Kevin", "age": 1} | Content-Type: application/json                  |                                                                |        |
| post-xml  | post   | [https://httpbin.org/post](https://httpbin.org/post)               | <xml>hello</xml>            | Content-Type: application/xml                   | result.json()["data"]=="<xml>hello</xml>"                      |        |

Run excel data file

```python
from excel_runner import run_excel

run_excel('data.xlsx')

```

Open data.xlsx again, you will see the test result


| name      | method | url                                                                | data                        | headers                                         | verify                                                         | result |
| --------- | ------ | ------------------------------------------------------------------ | --------------------------- | ----------------------------------------------- | -------------------------------------------------------------- |--------|
| get请求     | get    | [https://httpbin.org/get?a=1&b=2](https://httpbin.org/get?a=1&b=2) |                             |                                                 | res.status_code==200                                           | PASS   |
| post-form | post   | [https://httpbin.org/post](https://httpbin.org/post)               | name=Kevin&age=1            | Content-Type: application/x-www-form-urlencoded | res.status_code==200  <br>res.json()['form']['name']=='Kevin'] |    PASS    |
| post-json | post   | [https://httpbin.org/post](https://httpbin.org/post)               | {"name": "Kevin", "age": 1} | Content-Type: application/json                  |                                                                |PASS|
| post-xml  | post   | [https://httpbin.org/post](https://httpbin.org/post)               | <xml>hello</xml>            | Content-Type: application/xml                   | result.json()["data"]=="<xml>hello</xml>"                      |PASS|

