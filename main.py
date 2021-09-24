# Cron Expression Generator With Python V1.0.
#
# Copyright (C) 2021  Iven Leni Fernandez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

print(
    """
* * * * *	Every minute
0 * * * *	Every hour
0 0 * * *	Every day at 12:00 AM
0 0 * * FRI	At 12:00 AM, only on Friday
0 0 1 * *	At 12:00 AM, on day 1 of the month
    """
)


def cron_generator(minute, hour, day, month, dotw):

    if not minute:
        minute = '*'

    if not hour:
        hour = '*'

    if not day:
        day = '*'

    if not month:
        month = '*'

    if not dotw:
        dotw = '*'

    cron = f"{minute} {hour} {day} {month} {dotw}"
    return cron


def months_name(month):
    month_dic = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }
    return month_dic[month]


def days_name(dotw):

    day_dic = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return day_dic[dotw]


def minute():
    global tminute
    while True:
        try:
            minute = int(input('minute (0 - 59):'))
            if minute == 0:
                tminute = "Every hour"
                return minute
                break  # if you want to stop the loop
            else:
                tminute = f"At {minute} minutes past the hour"
                return minute
                break  # if you want to stop the loop

        except ValueError:
            print("Your input set to every minute.")
            tminute = ''
            minute = '*'
            return minute
            break


def hour():
    global thour
    while True:
        try:
            hour = int(input('hour (0 - 23):'))
            if hour in range(0, 12):
                thour = am_hours[hour]
                return hour
                break  # if you want to stop the loop
            elif hour in range(13, 24):
                thour = pm_hours[hour]
                return hour
                break  # if you want to stop the loop
            else:
                hour = '*'
                return hour
                break  # if you want to stop the loop

        except ValueError:
            print("Your input set to every hour.")
            hour = '*'
            return hour
            break


def day():
    while True:
        try:
            day = int(input('day of the month (1 - 31) or zero for every day:'))
            if day in range(1, 32):
                return day
                break  # if you want to stop the loop
            else:
                print("Your input set to every day.")
                day = '*'
                return day
        except ValueError:
            day = '*'
            return day
            break


def month():
    while True:
        try:
            month = int(input('month (1 - 12) or zero for every month:'))
            if month in range(1, 13):
                return month
                break  # if you want to stop the loop
            else:
                print("Your input set to every month.")
                month = '*'
                return month
            # implicit continue
        except ValueError:
            print("Your input set to every month.")
            month = '*'
            return month


def dotw():
    global tdotw
    while True:
        try:
            dotw = int(
                input('day of the week (0 - 6) or zero for every day in the week:'))
            if dotw in range(0, 7):
                tdotw = f"Only in {days_name(dotw)}"
                return dotw
                break  # if you want to stop the loop
            else:
                dotw = '*'
                return dotw
        except ValueError:
            dotw = '*'
            return dotw


am_hours = {0: 12, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5,
            6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11}
pm_hours = {12: 12, 13: 1, 14: 2, 15: 3, 16: 4,
            17: 5, 18: 6, 19: 7, 20: 8, 21: 9, 22: 10, 23: 11}

tminute = ''
thour = ''
tdotw = ''

minute = minute()
hour = hour()
day = day()
month = month()
dotw = dotw()

pmam = ''
if hour in range(0, 12):
    pmam = 'AM'
else:
    pmam = 'PM'

if minute == '*' and hour != '*':
    print(f'Every minute, between {thour}:00 {pmam} and {thour}:59 {pmam}')
elif minute == '*' and hour == '*':
    print('Every minute')
else:
    print(f'At {thour}:{minute} {pmam}')

if day == '*' and month == '*':
    print('Every day')
else:
    print(f'On day {day} of the {months_name(month)}')

if dotw == '*':
    print('Every day in the week')
else:
    print(f"Only in {days_name(dotw)}")

print('-------------')
print(cron_generator(minute, hour, day, month, dotw))
print('-------------')
