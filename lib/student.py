#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [ ]

# Knowledge is not in the parenthesis because they aren't starting with any knowledge, it's not a given like their name
    def learn(self, string):
        self.knowledge.append(string)