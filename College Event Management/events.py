from algorithms import count_items, maximum, selection_sort

class EventManager:
    def __init__(self):
        self.events = {}
        self.next_id = 1

    def create_event(self):
        name = input("Event name: ").strip()
        venue = input("Venue: ").strip()
        self.events[self.next_id] = {
            "name": name,
            "venue": venue,
            "participants": []
        }
        print("Created event ID:", self.next_id)
        self.next_id += 1

    def register_student(self):
        try:
            event_id = int(input("Event ID: "))
        except ValueError:
            print("Invalid ID")
            return

        if event_id not in self.events:
            print("Event not found")
            return

        student = input("Student name: ").strip()
        if student in self.events[event_id]["participants"]:
            print("Already registered")
            return

        self.events[event_id]["participants"].append(student)
        print("Registration successful")

    def show_events(self):
        if not self.events:
            print("No events")
            return

        for event_id, event in self.events.items():
            print(event_id, event["name"], "-", event["venue"],
                  "| registrations:", len(event["participants"]))

    def view_participants(self):
        if not self.events:
            print("No events")
            return

        try:
            event_id = int(input("Event ID: "))
        except ValueError:
            print("Invalid ID")
            return

        if event_id not in self.events:
            print("Event not found")
            return

        event = self.events[event_id]
        participants = event["participants"]

        print("\nRegistered students for", event["name"], "-", event["venue"])
        if not participants:
            print("No students registered")
            return

        for position, student in enumerate(selection_sort(participants), start=1):
            print(position, student)
        print("Total registered:", len(participants))

    def report(self):
        counts = [len(event["participants"]) for event in self.events.values()]
        print("Total events:", len(self.events))
        print("Total registrations:", count_items(counts))
        print("Maximum registrations:", maximum(counts) if counts else 0)

    def run(self):
        while True:
            print("\nCollege Event Management")
            print("1. Create event")
            print("2. Register student")
            print("3. Show events")
            print("4. View registered students")
            print("5. Report")
            print("6. Exit")
            choice = input("Choose: ")

            if choice == "1":
                self.create_event()
            elif choice == "2":
                self.register_student()
            elif choice == "3":
                self.show_events()
            elif choice == "4":
                self.view_participants()
            elif choice == "5":
                self.report()
            elif choice == "6":
                break
            else:
                continue
