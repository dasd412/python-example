import time
import random


# 1단계 : 설정 값을 받는 함수로 max_retries와 base_delay를 기억한다
def retry_with_backoff(max_retries=3, base_delay=1):
    """
    :param max_retries: 최대 재시도 횟수
    :param base_delay: 기본 대기 시간 (초)
    """

    # 2단계 : 실제 함수를 받는 데코레이터로서 func를 기억한다.
    def decorator(func):
        # 3단계: 실행시 호출되는 래퍼
        def wrapper(*args, **kwargs):
            # 클로저를 활용해 max_retries, base_delay, func 모두 접근 가능
            for attempt in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    print(f"성공 : (시도 횟수 {attempt + 1} 회)")
                    return result
                except ValueError:  # Value Error 같은 예외는 바로 실패
                    raise
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_retries - 1:
                        print(f"재시도 횟수 초과 :{e}")
                        raise
                    jitter = random.uniform(0, 0.2 * base_delay)  # 여러 프로세스가 동시에 같은 작업을 수행하는 것을 피하기 위해 흔들림 사용

                    delay = base_delay * (2 ** attempt) + jitter
                    print(f"재시도 {attempt + 1}/{max_retries}: {delay:.2f}초 후 재시도...")
                    time.sleep(delay)

        return wrapper

    return decorator
