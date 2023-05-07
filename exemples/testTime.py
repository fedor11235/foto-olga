from datetime import datetime, timedelta

format = '%Y-%m-%d %H:%M:%S'
date = '2023-03-16 22:47:22.073245'

dot_index = date.find('.')
cut_date = date[0:dot_index]

utc = datetime.utcnow()
now = datetime.now()

result = now + timedelta()
result2 = now + timedelta(hours=1.5)
result = now + timedelta(minutes=30)

date_object = datetime.strptime(cut_date, format)








