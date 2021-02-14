from abc import ABC, abstractmethod


# Define custom error class (should inherit from the 'Exception' class)
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Invalid operation")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Invalid operation")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


# Have to implement the read() method from the abstract parent class otherwise the children classes will automatically
# become abstract and wont be able to be called

class FileStream(Stream):
    def read(self):
        print("read data from file")


class NetworkStream(Stream):
    def read(self):
        print("read data from network")


class MemoryStream(Stream):
    def read(self):
        print("read data from Memory")
