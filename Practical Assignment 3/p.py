import heapq
import itertools

PRIORITY_NAMES = {
    1: "System Process",
    2: "Interactive Process",
    3: "Background Process",
    4: "Low-Priority Process",
}


class Process:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority

    def __str__(self):
        return (f"PID: {self.pid} | Name: {self.name} | "
                f"Priority: {self.priority} ({PRIORITY_NAMES[self.priority]})")


class PriorityQueue:
    def __init__(self):
        self._heap = []                    # entries: (priority, arrival_no, Process)
        self._counter = itertools.count()  # keeps FIFO order within a priority

    # 1. Add Process (enqueue)
    def enqueue(self, pid, name, priority):
        if priority not in PRIORITY_NAMES:
            print("Invalid priority! Choose a value from 1 to 4.")
            return False
        if any(p.pid == pid for _, _, p in self._heap):
            print(f"A process with ID {pid} already exists.")
            return False
        heapq.heappush(self._heap, (priority, next(self._counter),
                                    Process(pid, name, priority)))
        print(f"Process added: {pid} - {name} (Priority {priority})")
        return True

    # 2. Execute Process (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("No processes to execute. Queue is empty.")
            return None
        _, _, process = heapq.heappop(self._heap)
        print(f"Executing process -> {process}")
        return process

    # 3. View Next Process
    def display_next(self):
        if self.is_empty():
            print("No pending processes.")
            return None
        process = self._heap[0][2]
        print(f"Next process to execute -> {process}")
        return process

    # 4. Display Processes (priority order)
    def display_all(self):
        if self.is_empty():
            print("No pending processes.")
            return
        print("Pending processes (in execution order):")
        for i, (_, _, process) in enumerate(sorted(self._heap), start=1):
            print(f"  {i}. {process}")

    # 5. Count Processes
    def count(self):
        print(f"Total pending processes: {len(self._heap)}")
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    pq = PriorityQueue()
    menu = """
===== CPU Process Scheduler =====
1. Add Process
2. Execute Process
3. View Next Process
4. Display All Processes
5. Count Processes
6. Exit"""

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pid = read_int("Process ID: ")
            if pid is None:
                continue
            name = input("Process Name: ").strip()
            print("Priority: 1-System, 2-Interactive, 3-Background, 4-Low")
            priority = read_int("Priority (1-4): ")
            if priority is None:
                continue
            pq.enqueue(pid, name, priority)
        elif choice == "2":
            pq.dequeue()
        elif choice == "3":
            pq.display_next()
        elif choice == "4":
            pq.display_all()
        elif choice == "5":
            pq.count()
        elif choice == "6":
            print("Exiting scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()