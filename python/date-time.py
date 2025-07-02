from datetime import datetime, date, time, timedelta
import pytz

# now method is used to get the current date and time
current= datetime.now()
print("current Date & Time: ", current) # pip install datetime in terminal

present_date = datetime.today()
print("Date: ", present_date)

#printing the today's date in this format: dd-mm-yy
present_date = current.strftime("%d-%m-%Y")
print(present_date)

#printing the today's date in this format: dd/mm/yy
present_date = current.strftime("%d/%m/%Y")
print(present_date)
print("current date: ", current.strftime("%d"))
print("current Month in number: ", current.strftime("%m"))
print("current year: ", current.strftime("%Y"))
print("current year (short-form): ", current.strftime("%y"))

#printing the date with month in words
print("current month (short-form): ", current.strftime("%b"))
print("current month (full Name): ", current.strftime("%B"))
print("current Day (short-form): ", current.strftime("%a")) # short form day name - a
print("current Day (full Name): ", current.strftime("%A")) # day name - A
second_date = date(2026, 4, 2) #date(yyyy, m/mm, d/dd)
print("The given month (short-form): ", second_date.strftime("%b")) # sting format time( Short form month name)
print("The given month (full Name): ", second_date.strftime("%B")) #Month name -B
print("The given Day (short-form): ", second_date.strftime("%a"))
print("The given Day (full Name): ", second_date.strftime("%A"))

current = datetime(2025, 5, 14, 12, 55, 5)
second_date = datetime(2025, 6, 15, 12, 0, 0)

difference = second_date - current
print("The duration b/w both the dates:", difference)


dob = datetime(2003, 4, 2, 12, 0, 0) # datetime(yyyy, m/mm, d/dd, h/hh, m/mm, s/ss)
today = datetime.now()

difference = today - dob
print("The duration b/w both the dates:", difference)

day_number = current.timetuple().tm_yday
print("day number of the year: ", day_number)

week_number = current.strftime("%U") # week number -U
print("week number of the year: ", week_number)



#printing the current hour, minute & second
print("current Hour:", current.strftime("%H"))
print("current Hour in 24H format:", current.strftime("%H"))
print("current Hour in 12H format:", current.strftime("%I"))
print("current Minute:", current.strftime("%M")) # capital M -minute, small m - month
print("current second:", current.strftime("%S"))

print("current time in 24H format: ", current.strftime("%H:%M %p"))
print("current time in 12H format: ", current.strftime("%I:%M %p")) # p- am and pm

# printing Date in different format
print("Date with hyphens: ", current.strftime("%d-%M-%Y"))
print("Date with Month Name: ", current.strftime("%d-%b-%Y"))
print("Date with Month Name: ", current.strftime("%d %b %Y"))
print("Date : ", current.strftime("%b %d, %Y"))
print("Date : ", current.strftime("%d/%m/%y"))
print("Date with time(24H): ",current.strftime("%b %d, %Y %H:%M %p"))
print("Date with time(12H): ",current.strftime("%b %d, %Y %I:%M %p"))
print("Date with time(24H): ",current.strftime("%b %d, %Y %H:%M %S %p"))
print("Date with time(12H): ",current.strftime("%b %d, %Y %I:%M %S %p"))

#converting the date to String: "strftime" - string Format Time
#converting the string to Date: "strptime" - string parse Time
today = "14-05-2025"
converted_date = datetime.strptime(today, "%d-%m-%Y")
print("Modified the string to Date: ", converted_date)

#checking the current timezone and time
time_zone = datetime.now(pytz.timezone('Asia/Kolkata'))
time_zone_dubai = datetime.now(pytz.timezone('Asia/Dubai'))
time_zone_ny = datetime.now(pytz.timezone('America/New_York'))
time_zone_gmt = datetime.now(pytz.timezone('Africa/Lome'))
print("current Timezone's Time: ", time_zone )
print("Dubai Time: ", time_zone_dubai )
print("New york Time: ", time_zone_ny)
print("Greenwhich Mean Time: ", time_zone_gmt)

# Add or Subtract Days from current date
next_day = current + timedelta(days=1)
prev_day = current - timedelta(days=1)
print("Tomorrow: ", next_day.strftime("%d-%m-%Y"))
print("Yesterday: ", prev_day.strftime("%d-%m-%Y"))