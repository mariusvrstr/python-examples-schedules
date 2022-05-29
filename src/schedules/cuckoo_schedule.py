import datetime

from src.schedules.common.scheduling_abstract import SchedulingAbstract

class CuckooSchedule(SchedulingAbstract):

    def __init__(self, frequency_in_seconds):
        SchedulingAbstract.__init__(self, frequency_in_seconds, type(self).__name__)

    def exec(self):
       now = datetime.datetime.now()
       print()
       print("The clock opens...") 
       clock_says =  ''     
       for i in range(now.hour):
           clock_says += 'Cuckoo '

       print(f"{clock_says}")
       print("The clock closes.")
