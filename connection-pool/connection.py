import asyncio


class Connection:

    def __init__(self, conn_id: int):
        self.conn_id = conn_id
        self.is_open = True

    async def execute(self, query: str) -> str:
        if self.is_open:
            await asyncio.sleep(1)
            print("query : ", query)
            return "execute success"
        else:
            return "execute failed"

    async def close(self):
        self.is_open = False
