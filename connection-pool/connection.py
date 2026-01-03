
class Connection:

    def __init__(self,conn_id:int):
        sef.conn_id=conn_id
        self.is_open=True

    async def execute(self,query:str)->str:
        pass

    async def clos(self):
        pass