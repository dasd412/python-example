import pytest
from unittest.mock import Mock, patch
from retry_with_backoff import retry_with_backoff


def test_success_on_third_attempt():
    """3번째 시도에 성공하는 케이스"""
    # given
    mock_api = Mock(side_effect=[
        ConnectionError(),
        TimeoutError(),
        "success",
    ])

    # when
    decorated = retry_with_backoff(max_retries=3)(mock_api)
    result = decorated()

    # then
    assert result == "success"
    assert mock_api.call_count == 3


def test_max_retries_exceeded():
    """최대 재시도 횟수를 초과하는 케이스"""
    # given
    mock_api = Mock(side_effect=[TimeoutError(), ConnectionError(), ConnectionError()])

    # when & then
    decorated = retry_with_backoff(max_retries=3)(mock_api)

    with pytest.raises(ConnectionError):
        decorated()

    assert mock_api.call_count == 3


def test_value_error_no_retry():
    """ValueError는 재시도하지 않는 케이스"""
    # given
    mock_api = Mock(side_effect=ValueError())

    # when & then
    decorated = retry_with_backoff(max_retries=5)(mock_api)

    with pytest.raises(ValueError):
        decorated()

    assert mock_api.call_count == 1


def test_function_with_arguments():
    # given
    mock_api = Mock(side_effect=[ConnectionError(), "success"])

    # when
    decorated = retry_with_backoff(max_retries=3)(mock_api)
    result = decorated(123, token="abc")

    # then
    assert result == "success"
    assert mock_api.call_count == 2
    mock_api.assert_called_with(123, token="abc")


@patch('time.sleep')  # time.sleep을 Mock으로 대체
def test_multiple_retries_with_mocked_sleep(mock_sleep):
    """실제 시간을 기다리지 않고 재시도 로직 테스트"""
    # given
    mock_api = Mock(side_effect=[
        ConnectionError(),
        TimeoutError(),
        TimeoutError(),
        "success",
    ])

    # when
    decorated = retry_with_backoff(max_retries=5, base_delay=2)(mock_api)
    result = decorated()

    # then
    assert result == "success"
    assert mock_api.call_count == 4
    assert mock_sleep.call_count == 3  # 3번 재시도 == 3번 sleep
