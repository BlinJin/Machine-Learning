"""
You can share the x or y axis limits for one axis with another by
passing an axes instance as a sharex or sharey kwarg.

Changing the axis limits on one axes will be reflected automatically
in the other, and vice-versa, so when you navigate with the toolbar
the axes will follow each other on their shared axes.  Ditto for
changes in the axis scaling (e.g., log vs linear).  However, it is
possible to have differences in tick labeling, e.g., you can selectively
turn off the tick labels on one axes.

The example below shows how to customize the tick labels on the
various axes.  Shared axes share the tick locator, tick formatter,
view limits, and transformation (e.g., log, linear).  But the ticklabels
themselves do not share properties.  This is a feature and not a bug,
because you may want to make the tick labels smaller on the upper
axes, e.g., in the example below.

If you want to turn off the ticklabels for a given axes (e.g., on
subplot(211) or subplot(212), you cannot do the standard trick

   setp(ax2, xticklabels=[])

because this changes the tick Formatter, which is shared among all
axes.  But you can alter the visibility of the labels, which is a
property

  setp( ax2.get_xticklabels(), visible=False)

"""
import matplotlib.pyplot as plt
import numpy as np

def getChoice(step):
    return np.random.choice(2, step, p=[0.999, 0.001]);


step = 65000
t = np.arange(start=0, stop=step, step=1)


s1 = getChoice(step)
s2 = getChoice(step)
s3 = getChoice(step)
s4 = getChoice(step)
s5 = getChoice(step)
s6 = getChoice(step)
s7 = getChoice(step)
s8 = getChoice(step)

ax1 = plt.subplot(811)
plt.step(t, s1)
plt.ylim([-0.2,1.2])

# share x only
ax2 = plt.subplot(812, sharex=ax1, sharey=ax1)
plt.step(t, s2)
plt.ylim([-0.2,1.2])
#
# share x and y
ax3 = plt.subplot(813, sharex=ax1, sharey=ax1)
plt.step(t, s3)
plt.ylim([-0.2,1.2])

ax4 = plt.subplot(814, sharex=ax1, sharey=ax1)
plt.step(t, s4)
plt.ylim([-0.2,1.2])

ax5 = plt.subplot(815, sharex=ax1, sharey=ax1)
plt.step(t, s5)
plt.ylim([-0.2,1.2])

ax6 = plt.subplot(816, sharex=ax1, sharey=ax1)
plt.step(t, s6)
plt.ylim([-0.2,1.2])

ax7 = plt.subplot(817, sharex=ax1, sharey=ax1)
plt.step(t, s7)
plt.ylim([-0.2,1.2])

ax8 = plt.subplot(818, sharex=ax1, sharey=ax1)
plt.step(t, s8)
plt.ylim([-0.2,1.2])


plt.show()