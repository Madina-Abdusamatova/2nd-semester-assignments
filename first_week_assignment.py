class SchoolLocker:
    total_lockers=0
    school_name = "Al-Khwarizmi Academy"
    def __init__(self, student_name, locker_id, items=None):
        self.student_name=student_name
        self.locker_id=locker_id
        if items is None:
            self.items=[]
        else:
            self.items=items
        SchoolLocker.total_lockers+=1
    
    def store_item(self,item_name):
        if len(item_name)!=0:
            self.items.append(item_name)
            print(f"Stored: {item_name}")

    def retrieve_item(self,item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"Retrieved: {item_name}")
        else:
            print("Item not found")
    
    def display_locker(self):
        print(f"Locker {self.locker_id} assigned to {self.student_name} at {SchoolLocker.school_name}")

locker1=SchoolLocker("Gulnora","A-12")
locker2=SchoolLocker("Ravshan","A-15")
locker1.display_locker()
locker1.store_item("Calculator")
locker1.store_item("Notebook")
locker1.retrieve_item("Calculator")
locker2.display_locker()
locker2.retrieve_item("Backpack")
print(f"Total lockers: {SchoolLocker.total_lockers}")
