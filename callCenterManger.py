from queue import Queue

class callCenterManager:
    def __init__(self):
        self._operators = []
        self._quee = Queue()