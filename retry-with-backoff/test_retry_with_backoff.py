from unittest.mock import Mock, patch
import pytest
from retry_with_backoff import retry_with_backoff

def test_retry_success_on_third_attempt():
    # TODO: Mock 함수 만들기
    # - 처음 2번은 예외 발생
    # - 3번째는 성공

    mock_func = Mock()
    # side_effect로 순차적인 동작 정의하면?

    # TODO: 데코레이터 적용

    # TODO: 호출 및 검증
    # - 결과가 올바른가?
    # - 정확히 3번 호출되었나?
    # - call_count 속성 활용
