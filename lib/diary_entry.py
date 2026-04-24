import math
import re

class DiaryEntry:

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.words_read = 0

    def word_count(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Words per minute must be 1 or more!")
        if not isinstance(wpm, int):
            raise Exception("Words per minute must be an integer!")
        estimated_reading_time = self.word_count() / wpm
        return math.ceil(estimated_reading_time)

    def check_for_mobile_number(self):
        pattern = r'(?:\\+44|0)7\\d{3}\\s?\\d{3}\\s?\\d{3}'
        return bool(re.search(pattern, self.contents))
