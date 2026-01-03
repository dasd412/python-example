class PooledConnection:
    """
    비동기 컨텍스트 매니저

    사용 예:
        async with PooledConnection(pool) as conn:
            await conn.execute("SELECT ...")
    """

    def __init__(self, pool: ConnectionPool):
        self.pool = pool
        self.conn = None

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
