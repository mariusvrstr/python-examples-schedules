import asyncio

from datetime import datetime
from abc import ABC, abstractmethod

class SchedulingAbstract(ABC):
    frequency_in_seconds = None
    schedule_manager = None
    last_time_ran = None
    name = None
    _is_active = False

    def __init__(self, frequency_in_seconds, name):
        self.frequency_in_seconds = frequency_in_seconds
        self.name = name

    @abstractmethod # Implimented in the derived class
    def exec(self):
        pass

    async def start(self, schedule_manager):
        print(f"Starting schedule {self.name}.")
        if (self.schedule_manager is None):
            self.schedule_manager = schedule_manager

        self.schedule_manager.add_schedule(self.name, self)
        self._is_active = True

        while self._is_active:
            self.exec()
            self.last_time_ran = datetime.now()
            await asyncio.sleep(self.frequency_in_seconds)
            print(f"Tic complete for {self.name}")

        print(f"Schedule completed for {self.name}")
        self.stop_schedule()

    def stop(self):
        self._is_active = False
        print(f"Stopping [{self.name}]...")        
        self.schedule_manager.remove_schedule(self.name)


