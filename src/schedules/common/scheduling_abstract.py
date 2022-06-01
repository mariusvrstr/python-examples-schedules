import asyncio
import traceback
import time

from datetime import datetime
from abc import ABC, abstractmethod

class SchedulingAbstract(ABC):
    _is_active = False
    frequency_in_seconds = None
    schedule_manager = None
    last_run_time = None
    last_run_duration = None
    skipped_counter = None
    name = None    

    def __init__(self, frequency_in_seconds, name):
        self.frequency_in_seconds = frequency_in_seconds
        self.name = name

    @abstractmethod # Implimented in the derived class
    def exec(self):
        pass

    @asyncio.coroutine
    def start(self, schedule_manager, future):
        try:
            print(f"Starting schedule {self.name}.")
            if (self.schedule_manager is None):
                self.schedule_manager = schedule_manager

            self.schedule_manager.add_schedule(self.name, self)
            self._is_active = True

            while self._is_active:
                start = time.time()
                self.exec()
                self.last_run_time = datetime.now()
                completed = time.time()
                self.last_run_duration = completed - start
                yield from asyncio.sleep(self.frequency_in_seconds)
                print(f"Tic complete for {self.name}")

            print(f"Schedule completed for {self.name}")
            self.stop_schedule()

        except:
            ex = traceback.format_exc()
            print(f"Failed to do XXX. Error Details >> {ex}")
            raise # re-throw after writing error to screen 
        

    def stop(self):
        self._is_active = False
        print(f"Stopping [{self.name}]...")        
        self.schedule_manager.remove_schedule(self.name)


