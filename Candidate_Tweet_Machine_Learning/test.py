import matplotlib.pyplot as plt

D = {'HA':25, 'JA':5}
plt.bar(range(len(D)), D.values(), align='center')
plt.xticks(range(len(D)), D.keys())

plt.show()