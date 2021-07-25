"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""

# class CashRegister:
#
#     def __init__(self, item):
#
#         self.total_items = {} # {'item': 'price'}
#         self.total_price = 0
#         self.discount = 0
#         self.item = item
#
#     def add_item(self):
#         for k, v in self.item.items():
#             self.total_items[k] = v
#         return self.total_items
#
#
#     def remove_item(self):
#         self.total_items.remove(self.item)
#
#     def apply_discount(self):
#         t = self.get_total()
#         return t-self.discount
#
#     def get_total(self):
#         mylist = self.add_item()
#         y = 0
#         for k,v in mylist.items():
#             y += v
#         return y
#
#
#     def show_items(self):
#         return self.add_item(self)[self.item]
#
#
#     def reset_register(self):
#         self.add_items = None
#         pass
#
#
# # EXAMPLE code run:
# item = {"Milk": 1, "Eggs":2, "Bread": 3}
#
# tst = CashRegister(item)
# print(tst.add_item())
# print(tst.get_total())
#

"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()
        self.total_marks = 0



class CFGStudent(Student):

    #     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)

    def add_subject(self):

        for k, v in self.subjects.items():
            self.subjects[k] = v
            return self.subjects

    #    create a method to view all subjects taken by a student

    def view_subjects(self):
        for k in self.subjects.items():
            return self.subjects[k]

    #     create a method  (and a new variable) to get student's overall mark (use average)

    def avg_mark(self):
        count = 0
        for v in self.subjects.items():
            avg_marks = total_marks / count
            count += count
            return self.subjects[k]




class DataStudent(Student):

    #     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)

    def add_subject(self):

        for k, v in self.subjects.items():
            self.subjects[k] = v
            return self.subjects

    #    create a method to view all subjects taken by a student

    def view_subjects(self):
        for k in self.subjects.items():
            return self.subjects[k]

    #     create a method  (and a new variable) to get student's overall mark (use average)

    def avg_mark(self):
        count = 0
        for v in self.subjects.items():
            avg_marks = total_marks / count
            count += count
            return self.subjects[k]

software = CFGStudent()
software.add_subject()
software.view_subjects()
software.avg_marks()


data = DataStudent()
data.add_subject()
data.view_subjects()
data.avg_marks()
