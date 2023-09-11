import os
import datetime
class Todo:
    def __init__(self, name, priority=2, due_date=None, completed=False):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
    def __repr__(self):
        status = "Completed" if self.completed else "Incomplete"
        due_date_str = self.due_date.strftime("%d %b %Y") if self.due_date else ''
        return f"{self.name} ({self.priority}) due {due_date_str} - {status}"
class TodoManager:
    def __init__(self):
        self.todos = []
    def add(self, name, priority=2, due_date=None):
        todo = Todo(name, priority, due_date)
        self.todos.append(todo)
    def remove(self, index):
        if 0 <= index < len(self.todos):
            self.todos.pop(index)
        else:
            print("Invalid index. Todo not removed.")
    def complete(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].completed = True
        else:
            print("Invalid index. Todo not marked as completed.")
    def display(self):
        for i, todo in enumerate(self.todos, start=1):
            print(f"{i}. {todo}")
    def save(self, filename):
        with open(filename, 'w') as f:
            for todo in self.todos:
                f.write(f"{todo.name}\n")
                f.write(f"{todo.priority}\n")
                if todo.due_date:
                    f.write(f"{todo.due_date.strftime('%d/%m/%Y')}\n")
                else:
                    f.write("\n")
                f.write(f"{todo.completed}\n")
    def load(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                while True:
                    name = f.readline().strip()
                    if not name:
                        break
                    priority = int(f.readline().strip())
                    due_date_str = f.readline().strip()
                    due_date = None
                    if due_date_str:
                        due_date = datetime.datetime.strptime(due_date_str, "%d/%m/%Y")
                    completed = bool(f.readline().strip())
                    self.add(name, priority, due_date)
                    if completed:
                        self.complete(len(self.todos) - 1)
if __name__ == "__main__":
    manager = TodoManager()
    filename = 'todos.txt'
    manager.load(filename)
    while True:
        print("\n1. Add Todo")
        print("2. Remove Todo")
        print("3. Complete Todo")
        print("4. Display Todos")
        print("5. Save & Quit")
        choice = input("Choice: ")
        if choice == '1':
            name = input("Todo Name: ")
            priority = int(input("Priority (1-3): "))
            due_date_str = input("Due Date (dd/mm/yyyy): ")
            if due_date_str:
                try:
                    due_date = datetime.datetime.strptime(due_date_str, "%d/%m/%Y")
                except ValueError:
                    print("Invalid date format. Todo not added.")
                    continue
            else:
                due_date = None
            manager.add(name, priority, due_date)
        elif choice == '2':
            index = int(input("Todo Number: ")) - 1
            manager.remove(index)
        elif choice == '3':
            index = int(input("Todo Number: ")) - 1
            manager.complete(index)
        elif choice == '4':
            manager.display()
        elif choice == '5':
            manager.save(filename)
            break
