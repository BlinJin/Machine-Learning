import matplotlib.pyplot as plt
import numpy as np

t = np.arange(start=0, stop=6500, step=1)
#
s = np.random.choice(2, 6500, p=[0.99, 0.01])
# plt.plot(t, s)
plt.step(t, s, label='pre (default)')

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
# plt.savefig("test.png")
plt.ylim([0,2])
plt.show()

# print np.random.choice(2, 20)



def randProb(index):
    return index % 2



