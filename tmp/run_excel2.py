import json

import requests
import pandas as pd


d = pd.read_excel(open('1.xlsx'), sheet_name='添加加油卡')

print(d)
