import numpy as np

num_train = 50000
num_valid = 10000
num_test = 5000
num_time_steps = 49
num_time_steps_test = 99
num_balls = 2
box_lim_down = -5
box_lim_up = 5
suffix = "_synthetic"


edges_train = np.ones([num_balls, num_balls])
edges_train = edges_train - np.eye(2)
e_train = np.zeros([num_train, num_balls, num_balls])
for i in np.arange(num_train): e_train[i, :, :] = edges_train

edges_valid = np.ones([num_balls, num_balls])
edges_valid = edges_valid - np.eye(2)
e_valid = np.zeros([num_valid, num_balls, num_balls])
for i in np.arange(num_valid): e_valid[i, :, :] = edges_valid

edges_test = np.ones([num_balls, num_balls])
edges_test = edges_test - np.eye(2)
e_test = np.zeros([num_test, num_balls, num_balls])
for i in np.arange(num_test): e_test[i, :, :] = edges_test



loc_train = np.zeros([num_train, num_time_steps, num_balls, 2])
y_ax_steps = np.arange(start=box_lim_down, stop=box_lim_up,
                       step=(box_lim_up-box_lim_down)/num_time_steps)
for i in np.arange(49):
    loc_train[:, i, 1, :] = y_ax_steps[i]
for i in np.arange(num_train):
    start = 10 * np.random.random_sample(2,) - 5
    loc_train[i, :, 0, :] = start

loc_valid = np.zeros([num_valid, num_time_steps, num_balls, 2])
y_ax_steps = np.arange(start=box_lim_down, stop=box_lim_up,
                       step=(box_lim_up-box_lim_down)/num_time_steps)
for i in np.arange(49):
    loc_valid[:, i, 1, :] = y_ax_steps[i]
for i in np.arange(num_valid):
    start = 10 * np.random.random_sample(2,) - 5
    loc_valid[i, :, 0, :] = start

loc_test = np.zeros([num_test, num_time_steps_test, num_balls, 2])
y_ax_steps = np.arange(start=box_lim_down, stop=box_lim_up,
                       step=(box_lim_up-box_lim_down)/num_time_steps)
for i in np.arange(49):
    loc_test[:, i, 1, :] = y_ax_steps[i]
for i in np.arange(num_test):
    start = 10 * np.random.random_sample(2,) - 5
    loc_test[i, :, 0, :] = start


vel_train = np.ones([num_train, num_time_steps, num_balls, 2])
vel_train[:, :, 0, :] = 0
vel_train[:, 0, 1, 0] = 1.1

vel_valid = np.ones([num_valid, num_time_steps, num_balls, 2])
vel_valid[:, :, 0, :] = 0
vel_valid[:, 0, 1, 0] = 1.1

vel_test = np.ones([num_test, num_time_steps_test, num_balls, 2])
vel_test[:, :, 0, :] = 0
vel_test[:, 0, 1, 0] = 0.9

np.save('loc_train' + suffix + '.npy', loc_train)
np.save('vel_train' + suffix + '.npy', vel_train)
np.save('edges_train' + suffix + '.npy', e_train)

np.save('loc_valid' + suffix + '.npy', loc_valid)
np.save('vel_valid' + suffix + '.npy', vel_valid)
np.save('edges_valid' + suffix + '.npy', e_valid)

np.save('loc_test' + suffix + '.npy', loc_test)
np.save('vel_test' + suffix + '.npy', vel_test)
np.save('edges_test' + suffix + '.npy', e_test)
