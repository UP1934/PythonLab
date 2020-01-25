import datetime 
from datetime import timedelta
time_of_leaving =  datetime.time(6,52,00)
print("Time Of Leaving The House:\n",time_of_leaving)
time_taken_at_easy_pace= datetime.time(0,8,15)
time_taken_at_tempo= datetime.time(0,7,12)
print("Time taken to travel a mile at easy pace:\n",time_taken_at_easy_pace)
print("Time taken to travel a mile at tempo pace:\n",time_taken_at_tempo)

print("He Ran 2 miles at easy pace and 3 miles at tempo pace\n")

time_of_reaching=timedelta(hours=time_of_leaving.hour,minutes=time_of_leaving.minute,seconds=time_of_leaving.second)+timedelta(minutes=(2*time_taken_at_easy_pace.minute+ 3*time_taken_at_tempo.minute),seconds=(2*time_taken_at_easy_pace.second+ 3*time_taken_at_tempo.second))

print("Time of Reaching Home for Breakfast:\n",time_of_reaching)


OUTPUT :

C:\Users\Admin>cd Desktop

C:\Users\Admin\Desktop>python Exp_1(b).py
Time Of Leaving The House:
 06:52:00
Time taken to travel a mile at easy pace:
 00:08:15
Time taken to travel a mile at tempo pace:
 00:07:12
He Ran 2 miles at easy pace and 3 miles at tempo pace

Time of Reaching Home for Breakfast:
 7:30:06

C:\Users\Admin\Desktop>

