from job import Job

class JobApplication(Job):
    def __init__(self, company, role, status):
        super().__init__(company, role, status)

    def display(self):
        return f"{self.company} | {self.role} | {self.status}"
