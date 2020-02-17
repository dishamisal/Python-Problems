import pandas as pd
#import the input file
df = pd.read_csv("/home/worker_hours.csv")
print(df)

from datetime import datetime

hours_dict = {}
#make a list of the column with worker ids
id_list = df['worker_id'].tolist()

#extracting time from date and time:
def date_convert(date_to_convert):
     return datetime.strptime(date_to_convert, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S')
df['new_time'] = df['new_time'].apply(date_convert)

#subtracting the corresponding time of each worker with the next timestamp, which is the time at which he logs out.
date_format = "%H:%M:%S"
one_time = datetime.strptime(new_df['new_time1'].iloc[0], date_format)
two_time = datetime.strptime(new_df['new_time1'].iloc[-1], date_format)
total_time = (one_time - two_time).seconds
#store the list with worker ids into a set
s = set(new_list)

#make a list with the difference in timestamps for each worker_id
for i in s:
    if i: # Not 0
        d = []
        for index in range(0, len(new_list)):
            if i==new_df['worker_id'].iloc[index]:
                # d.append((new_df['new_time1'])[index+1])
                try:
                    one = new_df['new_time1'].iloc[index+1]
                except IndexError:
                    continue
                two = new_df['new_time1'].iloc[index]
                one_time = datetime.strptime(one, date_format)
                two_time = datetime.strptime(two, date_format)
                diff = (one_time - two_time).seconds
                d.append(diff)

        hours_dict[i] = sum(d) * 100 / total_time
for k,v in hours_dict.items():
    print(k, v)

#plot a bar plot showing the distribution of working hours for each worker id
import matplotlib.pyplot as plt
plt.bar(range(len(battr_dict)), list(battr_dict.values()), align='center')
plt.xticks(range(len(battr_dict)), list(battr_dict.keys()))
plt.xlabel('No. of Hours', fontsize=16)
plt.ylabel('Percentage', fontsize=16)
plt.show()


