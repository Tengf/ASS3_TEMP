import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from scipy import stats
%pylab inline

df = pd.read_csv('201501-citibike-tripdata.csv')

df['Dura_Subs'] = df['tripduration'][df['usertype']=='Subscriber']
df['Dura_Cust'] = df['tripduration'][df['usertype']=='Customer']

plt.figure(1, figsize = (20,8))
ax1 = plt.subplot(1,2,1)
ax1 = df[np.abs(df.Dura_Subs-df.Dura_Subs.mean())<=(3*df.Dura_Subs.std())].Dura_Subs.plot(kind='hist', alpha=0.5)
ax1.set_title('Subscriber')
ax1.set_ylabel('Count')
ax1.set_xlabel('Trip Duration (s)')
ax2 = plt.subplot(1,2,2)
ax2 = df[np.abs(df.Dura_Cust-df.Dura_Cust.mean())<=(3*df.Dura_Cust.std())].Dura_Cust.plot(kind='hist', alpha=0.5)
ax2.set_title('Customer')
ax2.set_ylabel('Count')
ax2.set_xlabel('Trip Duration (s)')
plt.show()

print 'Summary Statistics for Tripduration of Subscriber'
print df.Dura_Subs.describe()
print 'Summary Statistics for Tripduration of Customer'
print df.Dura_Cust.describe()

plt.figure(2)
ax3 = plt.subplot(1,1,1)
ax3.bar([2,6], [df.Dura_Subs.mean(), df.Dura_Cust.mean()], [2,2])
ax3.set_xlim(0,10)
ax3.set_title('Mean of Trip Duration by Subscriber vs Customer')
ax3.set_ylabel('Trip Duration (s)')
ax3.set_xticks([3,7])
ax3.set_xticklabels(('Subscriber','Customer'))

stats.ttest_ind(df.Dura_Subs.dropna(), df.Dura_Cust.dropna(), equal_var = False)