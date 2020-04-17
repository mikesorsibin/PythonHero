>>> import datetime
>>> t = datetime.time(5,34,5)
>>> t
datetime.time(5, 34, 5)
>>> t.min
datetime.time(0, 0)
>>> datetime.time
<class 'datetime.time'>
>>> datetime.time.min
datetime.time(0, 0)
>>> print(datetime.time.min)
00:00:00
>>> today = datetime.date.today()
>>> today
datetime.date(2020, 4, 7)
>>> print(today)
2020-04-07
>>> print(today.timetuple())
time.struct_time(tm_year=2020, tm_mon=4, tm_mday=7, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=98, tm_isdst=-1)
>>> today.year
2020
>>> datetime.date.min
datetime.date(1, 1, 1)
>>> datetime.date.max
datetime.date(9999, 12, 31)
>>> datetime.date.resolution
datetime.timedelta(1)
>>> d1=datetime.date(2020,4,7)
>>> d1
datetime.date(2020, 4, 7)
>>> d2=d1.replace(2021)
>>> d2
datetime.date(2021, 4, 7)
>>> d1
datetime.date(2020, 4, 7)
>>> d1-d2
datetime.timedelta(-365)
