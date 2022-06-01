import os
from abc import ABC, abstractmethod
from src.schedules.common.scheduling_abstract import SchedulingAbstract

class BatchScheduleAbstract(SchedulingAbstract):
    _batch_size = None
    _batch = None

    def __init__(self, frequency_in_seconds, batch_size, name):
        SchedulingAbstract.__init__(self, frequency_in_seconds, name)
        self._batch_size = batch_size

    @abstractmethod
    def count_items_to_process(self):
        return None

    @abstractmethod
    def fetch_next_batch(self, batch_size):
        pass

    @abstractmethod
    def process_item(self, item):
        pass

    def exec(self):
        remaining_items = self.count_items_to_process()   
        size = self._batch_size if self._batch_size < remaining_items else remaining_items

        self._batch = self.fetch_next_batch(size)       

        if self._batch is None:
            print('No items found to process')
            pass
            
        if not isinstance(self._batch, list):
            raise ValueError(f'Did not return a valid list of items to be processed. List or None expected but {self._batch} was given.')

        os.system('cls')
        print(f'Starting a batch of [{size}] from the remaining [{remaining_items}]')
        print()

        count = 0

        for item in self._batch:
            self.process_item(item)
            count += 1
            
        print(f'Batch done. [{count}] items processed, [{remaining_items - count}] remaining.')
        print()

