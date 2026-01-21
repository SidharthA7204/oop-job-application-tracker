from user import User
from tracker import JobApplication
from storage import Storage

def menu():
    print("\n1. Add Job")
    print("2. View Jobs")
    print("3. Exit")

user = User("Sidharth")

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        company = input("Company: ")
        role = input("Role: ")
        status = input("Status (Applied / Interview / Rejected): ")

        job = JobApplication(company, role, status)
        Storage.save(job.display())
        print("✅ Job Added")

    elif choice == "2":
        jobs = Storage.read()
        print("\n--- Job Applications ---")
        for j in jobs:
            print(j.strip())

    elif choice == "3":
        print("Exiting...")
        break
