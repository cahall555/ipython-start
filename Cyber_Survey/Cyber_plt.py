import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

data = pd.read_csv('Cybersecurity_survey.csv')

web = np.array(data['INTERNET'])

plt.hist(web)
plt.title('Time Spent Online')
plt.xlabel('Answer')
plt.ylabel('Number')

plt.show()

