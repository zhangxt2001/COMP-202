time_24hrs = int(input('Enter the time:'))

hours = time_24hrs // 100
minutes = time_24hrs % 100

if minutes <10:
    min_str = '0' + str(minutes)
else:
    min_str = str(minutes)
    

if hours == 12:
    am_pm ="pm"
    time_12hrs = str(hours)+ ':' + min_str + am_pm
    print("The current time is:" + time_12hrs)
if hours % 12 == 0:
    am_pm ="am"
    hours = hours % 12
    time_12hrs = str(hours)+ ':' + min_str + am_pm
    print("The current time is:" + time_12hrs)
elif hours % 12 != hours:
    am_pm = "pm"
    hours = hours % 12
    time_12hrs = str(hours)+ ':' + min_str + am_pm
    print("The current time is:" + time_12hrs)
else:
    am_pm = "am"
    time_12hrs = str(hours)+ ':' + min_str + am_pm
    print("The current time is:" + time_12hrs)

print(not(type(c)!=str and c<10))