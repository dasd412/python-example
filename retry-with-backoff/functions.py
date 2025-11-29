import random
from retry_with_backoff import retry_with_backoff

call_count = 0


@retry_with_backoff(max_retries=5, base_delay=1)
def unstable_api() -> str:
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError(f"API 호출 실패 (시도 {call_count})")
    return "success"


@retry_with_backoff(max_retries=3, base_delay=0.5)
def fetch_user(user_id, token):
    if random.random() < 0.7:
        raise TimeoutError("서버 응답 없음")
    return f"User {user_id} 정보 :{token}"


@retry_with_backoff(max_retries=5)
def validate_data(value):
    if value < 0:
        raise ValueError("음수는 허용되지 않음")
    if random.random() < 0.5:
        raise ConnectionError("일시적 오류")
    return f"검증 완료: {value}"
