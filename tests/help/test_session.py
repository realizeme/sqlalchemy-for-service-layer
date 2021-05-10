import pytest

from app.config.db import Settings
from app.help.session import SessionMaker


# @pytest.mark.skip(reason="only available at integration testing")
def test_create_db_session():
    # given
    setting = Settings()

    # when`````````````````````````````````````````````````````````````````````````````
    session_maker = SessionMaker(setting)
    session = session_maker.get_session()

    # then
    with session.begin():
        print(session)
