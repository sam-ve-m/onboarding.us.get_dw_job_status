from unittest.mock import patch

from etria_logger import Gladsheim
from mnemosine import SyncCache

from src.repository.enum_employ_status_cache.repository import (
    EnumEmployStatusCacheRepository,
)

enum_dummy = [{"code": "a", "value": "b"}]


@patch.object(SyncCache, "save")
def test_save_enum_employ_status(save_mock):
    result = EnumEmployStatusCacheRepository.save_enum_employ_status(enum_dummy)
    assert save_mock.called
    assert result is True


@patch.object(Gladsheim, "error")
@patch.object(SyncCache, "save")
def test_save_enum_employ_status_when_value_error_occurs(save_mock, etria_mock):
    save_mock.side_effect = ValueError()
    result = EnumEmployStatusCacheRepository.save_enum_employ_status(enum_dummy)
    assert save_mock.called
    assert etria_mock.called
    assert result is False


@patch.object(Gladsheim, "error")
@patch.object(SyncCache, "save")
def test_save_enum_employ_status_when_type_error_occurs(save_mock, etria_mock):
    save_mock.side_effect = TypeError()
    result = EnumEmployStatusCacheRepository.save_enum_employ_status(enum_dummy)
    assert save_mock.called
    assert etria_mock.called
    assert result is False


@patch.object(Gladsheim, "error")
@patch.object(SyncCache, "save")
def test_save_enum_employ_status_when_exception_occurs(save_mock, etria_mock):
    save_mock.side_effect = Exception()
    result = EnumEmployStatusCacheRepository.save_enum_employ_status(enum_dummy)
    assert save_mock.called
    assert etria_mock.called
    assert result is False


@patch.object(SyncCache, "get")
def test_get_enum_employ_status(get_mock):
    get_return_value = enum_dummy
    get_mock.return_value = get_return_value
    result = EnumEmployStatusCacheRepository.get_enum_employ_status()
    assert result == get_return_value


@patch.object(Gladsheim, "error")
@patch.object(SyncCache, "get")
def test_get_enum_employ_status_exception(get_mock, etria_mock):
    get_return_value = enum_dummy
    get_mock.side_effect = Exception()
    result = EnumEmployStatusCacheRepository.get_enum_employ_status()
    assert etria_mock.called
    assert result is None
