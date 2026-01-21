class Storage:
    FILE = "jobs.txt"

    @staticmethod
    def save(job):
        with open(Storage.FILE, "a") as file:
            file.write(job + "\n")

    @staticmethod
    def read():
        try:
            with open(Storage.FILE, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []
