from prefect import flow,task
from tasks.task_extract import (task_extract)
from tasks.task_load import (task_load)
import asyncio

@flow(name='ETL OFERTAS LABORALES')
async def main_flow():
    search = ['python','react']
    for s in search:
        offers = await task_extract(s)
        await task_load(offers)
    
    
    
if __name__ == '__main__':
    asyncio.run(main_flow())