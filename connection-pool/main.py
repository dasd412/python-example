import asyncio
from pool import ConnectionPool

async def basic(pool: ConnectionPool):
    conn=await pool.acquire()
    result=await conn.execute("SELECT * FROM users")
    await pool.release(conn)
    print(f"basic : {result}, stats:{pool.get_stats()}")

async def concurrent1(pool: ConnectionPool):
    async def worker(i:int):
        conn=await pool.acquire()
        if conn:
            await conn.execute(f"Query {i}")
            await pool.release(conn)

    await asyncio.gather(*[worker(i) for i in range(100)])

async def main():
    pool=ConnectionPool()
    #await basic(pool)
    await concurrent1(pool)

if __name__ == "__main__":
    asyncio.run(main())