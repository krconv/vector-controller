import vector_controller

import pytest

class TestFreePlayMode:
    @pytest.fixture
    def vector_mock(self, mocker):
        vector = mocker.Mock()
        vector.anim.anim_list = []
        return vector

    def test_exits_freeplay_mode(self, vector_mock):
        remote = vector_controller.RemoteControlVector(vector_mock)

        remote.set_freeplay(enabled=False)

        vector_mock.conn.request_control.assert_called_once()

    def test_enters_freeplay_mode(self, vector_mock):
        remote = vector_controller.RemoteControlVector(vector_mock)

        remote.set_freeplay(enabled=True)

        vector_mock.conn.release_control.assert_called_once()
