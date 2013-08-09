
import calendar
import datetime


#http://byatool.com/python/python-getting-the-current-year-day-month-hour-minute-second-even-microsecond-eh/
currentMonth = datetime.datetime.now().month
currentYear = datetime.datetime.now().year

#http://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python

monthRangeVals = calendar.monthrange(currentYear, currentMonth)

dayOfWeek = monthRangeVals[0]
lastDayOfMonth = monthRangeVals[1]

myCal = calendar.HTMLCalendar(calendar.SUNDAY)
print myCal.formatmonth(currentYear, currentMonth)

