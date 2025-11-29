import time
import random


def retry_with_backoff(func, max_retries=3, base_delay=1):
    """
    :param func: 실행할 함수
    :param max_retries: 최대 재시도 횟수
    :param base_delay: 기본 대기 시간 (초)
    """

    def wrapper(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                result = func(*args, **kwargs)
                print(f"success : (attempt {attempt + 1} )")
                return result
            except ValueError:  # Value Error 같은 예외는 바로 실패
                raise
            except ConnectionError or TimeoutError as e:
                if attempt == max_retries - 1:
                    print(f"exceed max retries. fail :{e}")
                    raise
                jitter = random.uniform(0, 2)  # 여러 프로세스가 동시에 같은 작업을 수행하는 것을 피하기 위해 0~2초 흔들림 사용

                delay = base_delay * (2 ** attempt) + jitter
                time.sleep(delay)
                print(f"delay :{delay}")  # 몇 초 후 재시도하는 지 출력

        return wrapper
