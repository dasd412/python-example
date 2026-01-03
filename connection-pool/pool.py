import asyncio
from typing import Optional
from connection import Connection


class ConnectionPool:

    def __init__(self, pool_size: int = 5):
        self.pool_size = pool_size
        self.queue = asyncio.Queue(self.pool_size)
        self.connections = {}

        for i in range(self.pool_size):
            conn = Connection(i)
            self.connections[i] = conn
            self.queue.put_nowait(conn)

    async def acquire(self, timeout: float = 5.0) -> Optional[Connection]:
        """
        연결 획득

        Args:
            timeout: 대기 최대 시간 (초) <- 모든 요청이 사용중일 때, 새로운 요청이 얼마나 기다릴지
        Returns:
            Connection 객체 또는 None
        """
        try:
            conn = await asyncio.wait_for(
                self.queue.get(), # 공유 자원이 thread-safe한 큐 뿐이므로 락이 필요 없다.
                timeout=timeout,
            )
            return conn
        except asyncio.TimeoutError:
            print("timeout")
            return None

    async def release(self, conn: Connection):
        """
        연결 반환

        Args:
            conn: 반환할 Connection
        """
        await self.queue.put(conn) # 공유 자원이 thread-safe한 큐 뿐이므로 락이 필요 없다.

    async def close_all(self):
        for conn_id in self.connections:
            await self.connections[conn_id].close()

    def get_stats(self) -> dict:
        return {
            "total": self.pool_size,
            "available": self.queue.qsize(),
            "in_use": self.pool_size - self.queue.qsize()
        }
