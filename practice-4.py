# SFWRTECH 4SA3 – Software Architecture - Practice #4
# Nathan Olah
#
# Chain-of-Responsibility design pattern

from abc import ABC, abstractmethod

class Handler(ABC):
    
    def __init__(self, filename, priority):
        self._filename = filename
        self._priority = priority
        self._next_handler = None

    def set_next_handler(self, handler):
        self._next_handler = handler
    
    def handle_request(self, message, priority):
        if priority >= self._priority:
            self.write_file(message)
        else:
            self._next_handler.handle_request(message, priority)

    @abstractmethod
    def write_file(self, message):
        pass

class FileHandler(Handler):
    def write_file(self, message):
        with open(self._filename, 'a') as file:
            file.write(message + '\n')

#            
handler1 = FileHandler('log.txt', 1)
handler2 = FileHandler('log.txt', 2)
handler3 = FileHandler('log.txt', 3)

# Chain the handlers
handler1.set_next_handler(handler2)
handler2.set_next_handler(handler3)

handler1.handle_request('high priority', 3)
handler1.handle_request('low priority', 1)
handler1.handle_request('medium priority', 2)