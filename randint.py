import random

schet=random.randint(0,12000)
dopnalog=1000
doprub=500
if schet>10000 :
    print(schet - dopnalog )
elif schet < 10000:
    print( schet + doprub )
else:
    print(schet + doprub)
    
    