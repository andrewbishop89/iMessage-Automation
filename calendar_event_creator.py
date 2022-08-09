import subprocess
from typing import List
import time
from datetime import datetime
from typing import Union
from dataclasses import dataclass


@dataclass
class Event:
    name: str
    start: Union[int, str]
    length: int
    calendar: str


@dataclass
class Calendar:

    # 9:00 am August 5, 2022 
    # x hour, minute, second, day

    @staticmethod
    def add_event(event: Event):
        event_name = event.name
        start_time = event.start
        event_length = event.length
        calendar_name = event.calendar

        if isinstance(start_time, str):
            date_pattern = "%I:%M %p %B %d, %Y"
            start_timestamp = int(time.mktime(datetime.strptime(start_time, date_pattern).timetuple())) 

        def format_apple_script_date(timestamp: int):
            return str(timestamp - int(time.time()))       

        start_time = format_apple_script_date(start_timestamp)
        end_time = format_apple_script_date(start_timestamp + event_length)
                
        res = subprocess.run(["osascript", "calendar_event_creator.scpt", start_time, end_time, calendar_name, event_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            assert res.returncode != 0, res.stderr.decode('utf-8')


if __name__ == "__main__":
    #NOTE the calendar must exist in your apple calendar or else it will crash, this is a work in progress for now
  
    # create an event starting now for 1 hour 
    Calendar.add_event("Test Event", int(time.time()), 3600, "Automation") 
    # create an event on August 20 at 9am for 4 hours
    Calendar.add_event("Test Event 2", "9:00 am, August 20, 2022", 4 * 3600, "Home")

