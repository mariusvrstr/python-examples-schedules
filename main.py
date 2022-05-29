import asyncio
from src.schedule_manager import ScheduleManager
from src.schedules.cuckoo_schedule import CuckooSchedule
from src.schedules.schedule_overview import ScheduleOverview

schedule_manager = ScheduleManager()

cuckoo = CuckooSchedule(15)
overview = ScheduleOverview(5)

async def register_schedules():    
    await overview.start(schedule_manager)
    await cuckoo.start(schedule_manager)     

def start():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)      

    try:
        loop.run_until_complete(register_schedules())
    except KeyboardInterrupt:
        print('Stopping schedules')
    
start()

