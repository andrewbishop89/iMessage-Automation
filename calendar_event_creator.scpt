#!/usr/bin/osascript

on run argv

	set startOffset to (item 1 of argv) as number / 3600
	log startOffset
	set endOffset to (item 2 of argv) as number / 3600
	log endOffset
	
	set startDate to (current date) + (startOffset * hours)	
	log startDate	
	set endDate to (current date) + (endOffset * hours)
	log endDate

	set calendarName to (item 3 of argv)
	set eventName to (item 4 of argv)

    tell application "Calendar"
      tell calendar calendarName 
        make new event with properties {summary: eventName, start date: startDate, end date: endDate} 
      end tell
    end tell
end run
