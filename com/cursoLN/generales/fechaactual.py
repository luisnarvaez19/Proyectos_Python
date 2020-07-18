from datetime import datetime

fecha = datetime.now()

date_time = fecha.strftime("%Y%m%d%H%M%S")
print(type(date_time))
