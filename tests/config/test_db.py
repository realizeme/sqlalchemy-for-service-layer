from app.config.db import Settings


def test_pass_get_db_config():
    # when
    setting = Settings()

    # then
    assert setting.host is not None
    assert setting.port is not None
