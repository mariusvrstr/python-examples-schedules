import asyncio
from src.schedule_manager import ScheduleManager
from src.schedules.cuckoo_schedule import CuckooSchedule
from src.schedules.schedule_overview import ScheduleOverview
from src.schedules.batch_schedule import BatchSchedule

schedule_manager = ScheduleManager()

cuckoo = CuckooSchedule()
overview = ScheduleOverview()
batch = BatchSchedule(20)

def register_schedules(future):
    asyncio.ensure_future(cuckoo.start(schedule_manager, 12, future))
    asyncio.ensure_future(overview.start(schedule_manager, 5, future))
    asyncio.ensure_future(batch.start(schedule_manager, 5, future))

def start():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    register_schedules(future)

    try:
        loop.run_forever()
    finally:
        loop.close()


    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)      

    try:
        loop.run_until_complete(register_schedules())
    except KeyboardInterrupt:
        print('Stopping schedules')
    
start()

