
import calendar
import datetime


#http://byatool.com/python/python-getting-the-current-year-day-month-hour-minute-second-even-microsecond-eh/
currentMonth = datetime.datetime.now().month
currentYear = datetime.datetime.now().year

#http://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python

monthRangeVals = calendar.monthrange(currentYear, currentMonth)

dayOfWeek = monthRangeVals[0]
lastDayOfMonth = monthRangeVals[1]

#myCal = calendar.HTMLCalendar(calendar.SUNDAY)
#print myCal.formatmonth(currentYear, currentMonth)

week = range(7)

print "<table border=\"1\">"
print "\t<thead>"
print "\t\t<tr>"
print "\t\t\t<th colspan=\"7\">"+calendar.month_name[currentMonth]+" "+str(currentYear)+"</th"
print "\t\t</tr>"
print "\t\t<tr>"
print "\t\t\t<th>Sun</th>" 
print "\t\t\t<th>Mon</th>" 
print "\t\t\t<th>Tue</th>" 
print "\t\t\t<th>Wed</th>" 
print "\t\t\t<th>Thu</th>" 
print "\t\t\t<th>Fri</th>" 
print "\t\t\t<th>Sat</th>" 
print "\t\t</tr>"
print "\t</thead>"





print "</table>"
