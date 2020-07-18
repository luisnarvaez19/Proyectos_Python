from datetime import datetime, timedelta

past = datetime.now() - timedelta(days=1)

print(past < presente)
print(datetime(3000, 1, 1) < presente)
presente - datetime(2000, 4, 4)
# datetime.timedelta(4242, 75703, 762105)

presente = datetime.now()
prorroga=datetime(2020, 7, 20)
if presente < prorroga:
    print('sigue')
    print(presente)
else:
    print('para')