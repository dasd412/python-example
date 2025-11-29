from unittest.mock import Mock, patch
import pytest
from jitter import retry_with_backoff

"""
성공 케이스

첫 시도 성공
N번째 시도 성공


실패 케이스

모든 재시도 실패
예외 타입별 처리


백오프 검증

대기 시간이 올바른가?
Jitter가 적용되었나?


함수 인자 전달

원본 함수의 인자가 제대로 전달되나?
"""
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

def test_timeout():
    raise TimeoutError("timeout!")

try:
    retry_with_backoff(test_timeout, max_retries=2)()
except TimeoutError:
    print("TimeoutError가 제대로 잡혔습니다")
except:
    print("뭔가 잘못됐습니다")