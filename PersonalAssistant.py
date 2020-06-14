class PersonalAssistant:
  def __init__(self, todos):
    self.contacts = {
      'Ann': 'Marketing Coordinator', 
      'Chelsea': 'Software Developer', 
      'Nichole': 'Sales Representative', 
      'Max': 'Technical Writer'
    }
    self.birthdays = {
      'Chris': '4/8/1991',
      'Carolyn': '12/21/1993',
      'Ali': '5/12/1993',
      'Kim': '6/11/1993'
    }
    self.todos = todos

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "not a contact."

  def add_contact(self, name, position):
    if name in self.contacts:
      return "Contact already exists!"
    else:
      self.contacts[name] = position

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name, None)
    else:
      return "That contact isn't saved."

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    # Checks if todo_item is in todos list
    if todo_item in self.todos:
      # Gets the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      return "To-do is not in list."

  def get_todo(self):
    return self.todos

  # Gets a birthday from the dictionary
  def get_birthday(self, name):
    if name in self.birthdays:
      return self.birthdays[name]
    else:
      return "I don't know this person's birthday! How embarassing!"

  def add_birthday(self, name, birthday):
    if name in self.birthdays:
      return "You already have that person's birthday saved!"
    else:
      self.birthdays[name] = birthday

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
    else:
      return "I can't remove that person's birthday since I don't know it!"
