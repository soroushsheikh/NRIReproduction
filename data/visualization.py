import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# e_train_me = np.load('./edges_train_springs5.npy')
# loc_train_me = np.load('./loc_train_springs5.npy')
# vel_train_me = np.load('./vel_train_springs5.npy')

e_train_me = np.load('./edges_train_synthetic_2.npy')
loc_train_me = np.load('./loc_train_synthetic_2.npy')
vel_train_me = np.load('./vel_train_synthetic_2.npy')

num_balls = 3

print(e_train_me.shape)
print(loc_train_me.shape)
print(vel_train_me.shape)

# # This part is addition for test of synthetic dataset
# num_train = 50000
# num_time_steps = 49
# num_balls = 2
# box_lim_down = -5
# box_lim_up = 5
# loc = np.zeros([num_train, num_time_steps, num_balls, 2])
# y_ax_steps = np.arange(start=box_lim_down, stop=box_lim_up,
#                        step=(box_lim_up-box_lim_down)/(num_time_steps))
# for i in np.arange(49):
#     loc[:, i, 1, :] = y_ax_steps[i]
# for i in np.arange(50000):
#     start = 10 * np.random.random_sample(2,) - 5
#     loc[i, :, 0, :] = start
#
#
#
# loc_train_me=loc

########################
num = 90

def _update_plot(i, fig, scat):
    update = np.c_[loc_train_me[num, i, 0, :], loc_train_me[num, i, 1, :]]
    scat.set_offsets(update)
    print('Frames: %d' % i)
    return scat

fig = plt.figure(1)

ax = fig.add_subplot(111)
ax.grid(True, linestyle='-', color='0.75')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
scat = plt.scatter(loc_train_me[num, 0, 0, :], loc_train_me[num, 0, 1, :], c=np.arange(num_balls))
plt.legend(*scat.legend_elements(),
                    loc="lower left", title="Points")
scat.set_alpha(0.8)
anim = animation.FuncAnimation(fig, _update_plot, fargs=(fig, scat),
                               frames=loc_train_me.shape[1], interval=50)
#
plt.figure(2)
edgemat = plt.matshow(e_train_me[num, :, :])
plt.colorbar()
plt.show(block=True)