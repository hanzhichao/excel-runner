import pytest

from excel_runner.db import LongTengServer


@pytest.fixture(scope='module')
def db():
    db = LongTengServer()  # 建立数据库连接
    yield db
    db.close()  # 关闭数据库

