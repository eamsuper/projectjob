import datetime
target_date = datetime.date(2023, 12, 31) 
timestamp = 1673838688
today = datetime.date.fromtimestamp(timestamp) 
time_left = target_date - today 
days_left = time_left.days
date = datetime.date.fromtimestamp(timestamp)
date_time = datetime.datetime.fromtimestamp(timestamp)
date_time_thai = date_time.strftime('%d') 
mon_time = date_time.strftime('%B') 
mon_time_thai = date_time.strftime('%m') 
thisdict =	{
    "01": "มกราคม",
    "02": "กุมภาพันธ์",
    "03": "มีนาคม",
    "04": "เมษายน",
    "05": "พฤษภาคม",
    "06": "มิถุนายน",
    "07": "กรกฎาคม",
    "08": "สิงหาคม",
    "09": "กันยายน",
    "10": "ตุลาคม",
    "11": "พฤศจิกายน",
    "12": "ธันวาคม",
    }
month = thisdict[mon_time_thai]
year_time_thai = int(date_time.strftime('%Y')) + 543
year_thai = str(year_time_thai)
hour_time_thai = date_time.strftime('%H')
minute_time_thai = date_time.strftime('%M')
second_time_thai = date_time.strftime('%S')
date_time_utc = date_time.strftime('%d/%m/%Y, %H:%M:%S') 
timer = date_time.strftime('%X %p') 
