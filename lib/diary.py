import math
from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.entries_list = []
        self.contacts = {}
        self.todo_list = []

    def add_entry(self, entry):
        self.entries_list.append(entry)
        if entry.check_for_mobile_number() == True:
            pass
        

    def read(self, entry):
        return entry.format_task()

    def count_words(self):
        count = 0
        for i in range(len(self.entries_list)):
            count += self.entries_list[i].word_count()
        return count
    
    def total_reading_time(self, wpm):
        estimated_reading_time = self.count_words() / wpm
        return math.ceil(estimated_reading_time)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        readable_entries = []
        if wpm == 0:
            raise Exception("Words per minute must be 1 or more!")
        if not isinstance(wpm, int):
            raise Exception("Words per minute must be an integer!")
        if minutes == 0:
            raise Exception("Minutes must be 1 or more!")
        if not isinstance(minutes, int):
            raise Exception("Minutes must be an integer!")
        for entry in self.entries_list:
            if entry.word_count() <= words_user_can_read:
                readable_entries.append(entry)
        best_entry = sorted(readable_entries, key=lambda entry: entry.word_count(), reverse=True)
        return best_entry[0]
    
    def view_contact_numbers(self):
        return self.contacts
    
    def add_todo(self, todo):
        self.todo_list.append(todo)

    def incomplete(self):
        if self.list == []:
            raise Exception("Task list is empty!")
        else:
            return [task for task in self.todo_list if task.complete == False]

    def completed(self):
        return [task for task in self.todo_list if task.complete == True]
    
    def give_up(self):
        if self.todo_list == []:
            raise Exception("You can't give up when there are no tasks to give up on!")
        else:
            [task.mark_complete() for task in self.todo_list]