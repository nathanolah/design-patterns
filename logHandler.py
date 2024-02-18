#
#
#

from abc import ABC, abstractmethod

class Logger(ABC):

    def __init__(self, next_logger):
        self.__next_logger = next_logger

    @abstractmethod
    def make_entry(self, message):
        pass

    def log(self, message):

        self.make_entry(message)

        if (self.__next_logger == None):
            return
        else:
            self.__next_logger.log(message)

class ConsoleLogger(Logger):

    def make_entry(self, message):
        print("**CONSOLE**: " + message)

class FileLogger(Logger):

    def make_entry(self, message):
        print("**FILE**: " + message)

class DatabaseLogger(Logger):

    def make_entry(self, message):
        print("**DATABASE**: " + message)

#
#
        
console1 = ConsoleLogger(None)
file1 = FileLogger(console1)
database1 = DatabaseLogger(file1)
file2 = FileLogger(database1)

file2.log("test")

    
