import os
import pytest

from utils.db import LongTengServer
from utils.data import Excel
from utils.path import DATA_DIR


@pytest.fixture(scope='module')
def db():
    db = LongTengServer()  # 建立数据库连接
    yield db
    db.close()  # 关闭数据库

