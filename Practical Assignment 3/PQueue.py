class PriorityQueue:
    def __init__(self):
        self.queue = []

    # 1. Add Process
    def enqueue(self, pid, name, priority):
        process = {
            "id": pid,
            "name": name,
            "priority": priority
        }

        self.queue.append(process)

        # Sort according to priority (1 = Highest)
        self.queue.sort(key=lambda x: x["priority"])

        print("Process added successfully!")

    # 2. Execute Process
    def dequeue(self):
        if len(self.queue) == 0:
            print("No processes available!")
        else:
            process = self.queue.pop(0)

            print("Executing Process:")
            print("Process ID:", process["id"])
            print("Process Name:", process["name"])
            print("Priority:", process["priority"])

    # 3. View Next Process
    def display_next(self):
        if len(self.queue) == 0:
            print("No processes available!")
        else:
            process = self.queue[0]

            print("Next Process:")
            print("Process ID:", process["id"])
            print("Process Name:", process["name"])
            print("Priority:", process["priority"])

    # 4. Display All Processes
    def display_all(self):
        if len(self.queue) == 0:
            print("No pending processes!")
        else:
            print("\nPending Processes:")

            for process in self.queue:
                print("ID:", process["id"],
                      "| Name:", process["name"],
                      "| Priority:", process["priority"])

    # 5. Count Processes
    def count(self):
        print("Total Pending Processes:", len(self.queue))


# Main Program

pq = PriorityQueue()

while True:
    print("\n--- CPU PROCESS SCHEDULING ---")
    print("1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Process ID: "))
        name = input("Enter Process Name: ")
        priority = int(input("Enter Priority (1-4): "))

        if priority >= 1 and priority <= 4:
            pq.enqueue(pid, name, priority)
        else:
            print("Invalid Priority! Enter between 1 and 4.")

    elif choice == 2:
        pq.dequeue()

    elif choice == 3:
        pq.display_next()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        pq.count()

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")