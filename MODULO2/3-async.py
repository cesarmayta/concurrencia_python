import asyncio

async def tarea1():
    print('ejecutando tarea 1')
    await asyncio.sleep(1)
    
async def tarea2():
    print('ejecutando tarea 2')
    await asyncio.sleep(2)
    
async def tarea3():
    print('ejecutando tarea 3')
    await asyncio.sleep(3)
    
async def main():
    print("Hola estamos en el metodo MAIN")
    #tarea_1 = asyncio.create_task(tarea1())
    #tarea_2 = asyncio.create_task(tarea2())
    #tarea_3 = asyncio.create_task(tarea3())
    #await tarea_1
    #await tarea_2
    #await asyncio.gather(tarea_1,tarea_2,tarea_3)
    async_tasks = [asyncio.create_task(task()) for task in [tarea1,tarea2,tarea3]]
    await asyncio.gather(*async_tasks)
    print('Hemos terminado todas las tareas')
    
asyncio.run(
    main()
)