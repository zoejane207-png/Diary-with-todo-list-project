# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
                                                                                       
    ┌────────────────────────────────────────────────────────────────────────────┐     
    │  Class: Diary                                                              │     
    │                                                                            │     
    │  Public Properties:                                                        │     
    │   - Entries_list                                                           │     
    │   - Mobile_list - dictionary?                                              │     
    │   - Todo list                                                              │     
    │                                                                            │     
    │  Methods: Diary Entry:                     Methods: Todo list:             │     
    │   - Add entry + contact(if included)         - Add todo                    │     
    │   - Read                                     - Completed                   │     
    │   - Count_words                              - Incompleted                 │     
    │   - Reading_time                             - Give up                     │     
    │   - Best_entries_to_read                                                   │     
    │   - view_contact_numbers                                                   │     
    │                                                                            │     
    └──────────┬───────────────────────────────────────┬─────────────────────────┘     
               │                                       │                               
               │         Owns a list of:               │                               
               ▼                                       ▼                               
    ┌───────────────────────┐     ┌─────────────────────────────────────────────┐      
    │  Class: Todo          │     │  Class: DiaryEntry                          │      
    │                       │     │                                             │      
    │  Public Properties:   │     │   Public Properties:                        │      
    │    - Task name        │     │    - Title                                  │      
    │    - Complete status  │     │    - Content                                │      
    │                       │     │    - Includes_mobile : Boolean              │      
    │                       │     │                                             │      
    │  Methods:             │     │                                             │      
    │    - Mark as complete │     │   Methods:                                  │      
    │                       │     │    - Word Count                             │      
    │                       │     │    - Reading time                           │      
    │                       │     │    - Check_for_mobile_number                │      
    │                       │     │                                             │      
    │                       │     │                                             │      
    │                       │     │                                             │      
    └───────────────────────┘     └─────────────────────────────────────────────┘      
                                                                                       


```

```python
class Diary:
    # User-facing properties:
    #   Entries_list: list of instances of DiaryEntry          
    #   Contacts: dictionary of name and mobile number
    #   Todo_list: list of instances of Todo         


    def __init__(self):
        pass # No code here yet

    def add_entry(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the entry to the entries_list property of the self object
        pass # No code here yet

    def read(self, entry):
        # Parameters:
        #   keyword: Instance of DiaryEntry
        # Returns:
        #   A formatted string of the Diary title and contents:
        #    Title:
        #    Contents
        pass # No code here yet

    def count_words(self):
        # Returns:
        #   Int: The sum of the word count of all diary entries
        pass # No code here yet

    def total_reading_time(self, wpm):
        # Parameters:
        #   wpm: Int representing amount of words reader can read per minute
        # Returns:
        #   Int reprenting how long it will take to read all the entries in minutes
        #   Uses count_words method 
        pass # No code here yet

    def best_entry_to_read(self, wpm, minutes):
        # Parameters:
        #   wpm: Int representing amount of words reader can read per minute
        #   minutes: Int representing how long the reader would like to read for
        # Returns:
        #   An instance of DiaryEntry that is the best to read in the time they have given and closest to the word count that they have given
        pass # No code here yet

    def view_contact_numbers(self):
        # Parameters:None
        # Returns:
        #   List of dictionary items(name: number)
        #   Uses DiaryEntry method: includes_mobile_number
        pass # No code here yet

    def add_todo(self, task):
        # Parameters:
        #   task: An instance of Todo
        # 
        #   Adds task to todo_list
        pass # No code here yet

    def completed(self):
        # Parameters:
        #   
        # Returns:
        #   A list of tasks that have been marked as completed
        pass # No code here yet

    def incomplete(self):
        # Parameters:
        #   
        # Returns:
        #   A list of tasks that have not yet been completed
        pass # No code here yet

    def give_up(self):
        # Parameters:
        #   
        # Returns:
        #   Nothing
        # Side Effects:
        #   Marks all tasks as complete
        pass # No code here yet




class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   content: string

    def __init__(self, title, content):
        # Parameters:
        #   title: string
        #   content: string
        #   includes_mobile_number: boolean set to False to begin with
        # Side-effects:
        #   Sets the title, content and includes_mobile_number properties
        pass # No code here yet

    def word_count(self):
        # Returns:
        #   Int: representing the number of words in the entry content
        pass # No code here yet

def reading_time(self, wpm):
        # Parameters:
        #   wpm: Int representing amount of words reader can read per minute
        # Returns:
        #   Int reprenting how long it will take to read the entry in minutes
        pass # No code here yet

def check_for_mobile_number(self):
        # side effects:
        #    Changes includes_mobile_number property to true
        pass # No code here yet


class Todo:
    # User-facing properties:
    #   title: string
    #   content: string

    def __init__(self, task):
        # Parameters:
        #   task: string
        #   completed: boolean set to False to begin with
        #   
        # Side-effects:
        #   Sets the task and completed properties
        pass # No code here yet

    def mark_completed(self):
        # Parameters:
        #   
        # Side-effects:
        #   Sets the completed property to True
        pass # No code here yet



```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a diary
When we add two diary entries
We see those entries reflected in the entries_list
"""
my_diary = Diary()
entry_1 = DiaryEntry("Day One", "Today was a good day!")
entry_2 = DiaryEntry("Day Two", "Today was an okay day.")
my_diary.add_entry(entry_1, entry_2)
my_diary.entries_list # => [entry_1, entry_2]

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given an entry with a title and content
We see the title and content reflected in the title and content properties
"""
entry_1 = DiaryEntry("Day One", "Today was a good day!")
entry_1.title # => "Day One"
entry_1.content # => "Today was a good day!"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
