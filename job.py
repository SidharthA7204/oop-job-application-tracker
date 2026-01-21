from abc import ABC, abstractmethod

class Job(ABC):
    def __init__(self, company, role, status):
        self.company = company
        self.role = role
        self.status = status

    @abstractmethod
    def display(self):
        pass
