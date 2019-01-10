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

class TestKeys:
    @pytest.fixture
    def vector_mock(self, mocker):
        vector = mocker.Mock()
        vector.anim.anim_list = []
        return vector

    def test_starts_wheel_motors(self, vector_mock):
        remote = vector_controller.RemoteControlVector(vector_mock)

        remote.handle_key(ord('W'), False, False, True)
        vector_mock.motors.set_wheel_motors.assert_called_once_with(75, 75, 300, 300)

    def test_stops_wheel_motors(self, vector_mock):
        remote = vector_controller.RemoteControlVector(vector_mock)

        remote.handle_key(ord('W'), False, False, False)
        vector_mock.motors.set_wheel_motors.assert_called_once_with(0, 0, 0, 0)

    def test_multiple_keys_set_wheel_motors(self, vector_mock):
        remote = vector_controller.RemoteControlVector(vector_mock)

        remote.handle_key(ord('W'), False, False, True)
        remote.handle_key(ord('S'), False, False, True)
        remote.handle_key(ord('S'), False, False, False)
        remote.handle_key(ord('D'), False, False, True)
        vector_mock.motors.set_wheel_motors.assert_called_with(125, 25, 500, 100)