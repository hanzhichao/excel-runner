# excel-runner

Run Http requests list in excel sheet



## testdata format

| case_name              | method | url   | a             | b             | except_value   | actual_result | status |
| ---------------------- | ------ | ----- | ------------- | ------------- | -------------- | ------------- | ------ |
| test_add_normal        | get    | /add/ | 1             | 2             | 8              |               |        |
| test_add_normal2       | post   | /add/ | 100           | 2             | 102            |               |        |
| test_add_negative      | get    | /add/ | -3            | 5             | 2              |               |        |
| test_add_zero          | get    | /add/ | 0             | 0             | 0              |               |        |
| test_add_float         | get    | /add/ | 3.5           | 5.6           | 9.1            |               |        |
| test_add_large         | get    | /add/ | 9999999999999 | 9999999999999 | 19999999999998 |               |        |
| test_add_string_number | get    | /add/ | '3'           | '5'           | 8              |               |        |
| test_add_octal         | get    | /add/ | 0xAF          | 0x36          | 229            |               |        |
| test_add_hex           | get    | /add/ | 0o4           | 0o13          | 15             |               |        |
| test_add_blank         | get    | /add/ | ''            | ''            | None           |               |        |
| test_add_part_blank    | get    | /add/ | ''            | 5             | None           |               |        |
| test_add_null          | get    | /add/ | None          | None          | None           |               |        |
| test_add_part_null     | get    | /add/ | 3             | None          | None           |               |        |
| test_add_char          | get    | /add/ | a             | b             | None           |               |        |
| test_add_special_char  | get    | /add/ | %             | #             | None           |               |        |
| test_add_cn_char       | get    | /add/ | 汉             | 字             | None           |               |        |
