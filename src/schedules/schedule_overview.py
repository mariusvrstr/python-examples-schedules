import os

from src.schedules.common.scheduling_abstract import SchedulingAbstract

class ScheduleOverview(SchedulingAbstract):

    def __init__(self, frequency_in_seconds):
        SchedulingAbstract.__init__(self, frequency_in_seconds, type(self).__name__)

    def exec(self):
        os.system('cls')
        print('=====================================================')
        print('===============  Running Schedules ==================')
        print('=====================================================')
        print()

        for schedule_key in self.schedule_manager.schedules:
            schedule = self.schedule_manager.schedules[schedule_key]
            last_run = "N/A" if schedule.last_time_ran is None else schedule.last_time_ran.strftime("%Y-%m-%d %H:%M:%S")

            print(f"[{schedule.name}]: Active, last ran at {last_run}")