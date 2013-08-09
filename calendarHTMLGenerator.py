import math
import calendar
import datetime


#http://byatool.com/python/python-getting-the-current-year-day-month-hour-minute-second-even-microsecond-eh/
currentMonth = datetime.datetime.now().month
currentYear = datetime.datetime.now().year


#myCal = calendar.HTMLCalendar(calendar.SUNDAY)
#print myCal.formatmonth(currentYear, currentMonth)


print "<center>"
print "<table border=\"1\" cellpadding=\"10\">"
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


#http://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python
monthRangeVals = calendar.monthrange(currentYear, currentMonth)

dayOfWeekMonthStart = monthRangeVals[0]
lastDayOfMonth = monthRangeVals[1]

allDays = range(1,lastDayOfMonth+1)
prevMonthCell = True
numRows = math.ceil( ( lastDayOfMonth + dayOfWeekMonthStart ) / 7.0 )

prevMonth = currentMonth - 1
if currentMonth == 1:
   prevMonth = 12
prevMonthName = calendar.month_abbr[prevMonth]

nextMonth = currentMonth + 1
if currentMonth == 12:
   nextMonth = 1
nextMonthName = calendar.month_abbr[nextMonth]


curDay = 1
print "\t<tbody>"

for weekRow in range(int(numRows)):
   print "\t\t<tr>"
   for dayNum in range(7):
      print "\t\t\t<td>"
      if prevMonthCell:
         if dayNum <= dayOfWeekMonthStart:
            print"<div style=\"color:gray\">"+ prevMonthName+"</div>"
         else:
            prevMonthCell = False;
            print curDay
            curDay +=1
      elif curDay <= lastDayOfMonth:
         print curDay
         curDay += 1
      else:
         print"<div style=\"color:gray\">"+ nextMonthName+"</div>"

      print "\t\t\t</td>"
   print "\t\t</tr>"



print "\t</tbody>"

print "</table>"
