from collections import deque
from threading import Thread
from time import sleep

class ThreadPool:
    def __init__(self, max=1):
        self._max = max
        self._threads = []
    def run (self, tasks, delay=0):
        queue = deque(tasks)
        while True:
            # sleep(2)
            # print('sleeping')
            # print('all threads:', len(self._threads))
            self._threads = [x for x in self._threads if x.is_alive()]
            # print('alive:', len(self._threads))
            # print('max:', self._max)
            # print('tasks in queue', len(queue))
            while len(self._threads) < self._max and len(queue) > 0:
                # print('Len', len(self._threads))
                func, args = queue.pop()
                thread = Thread(target=func, args=args)
                sleep(delay)
                thread.start()
                self._threads.append(thread)
            if len(self._threads) == 0:
                break

