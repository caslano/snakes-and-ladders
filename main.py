import numpy as np
import matplotlib.pyplot as plt

ladders = []
snakes = []
trans = [[1, 38], [4, 14], [9, 31], [21, 42], [28, 84], [36, 44], [51, 67], [71, 91], [80, 100], [16, 6], [47, 26],
         [49, 11], [56, 53], [62, 19], [64, 60, ], [87, 24], [93, 73], [95, 75], [98, 78]]

for pair in trans:
    if pair[0] < pair[1]:
        ladders.append(pair)
    else:
        snakes.append(pair)

print(ladders)
print(snakes)

# Set up the transition matrix
T = np.zeros((101, 101))
for i in range(1, 101):
    T[i - 1, i:i + 6] = 1 / 6

for [i1, i2] in trans:
    iw = np.where(T[:, i1] > 0)
    T[:, i1] = 0
    T[iw, i2] += 1 / 6

# You need to land on 100
for i in range(1, 6):
    T[100 - 6 + i, 100 - 6 + i] += i / 6

for snake in snakes:
    T[snake[0], 100] = 0

# The player starts at position 0.
v = np.zeros(101)
v[0] = 1

n, P = 0, []
cumulative_prob = 0
expectation = 0
proba = 0
# Update the state vector v until the cumulative probability of winning
# is "effectively" 1
while cumulative_prob < 0.999999999:
    n += 1
    v = v.dot(T)
    proba = v[100]
    P.append(proba)
    cumulative_prob += proba
    expectation += proba * n

mode = np.argmax(P) + 1
print('Modal number of moves:', mode)
print('Expected number of moves:', expectation)

# Plot the probability of winning as a function of the number of moves
# fig, ax = plt.subplots()
# ax.plot(np.linspace(1, n, n), P, 'g-', lw=2, alpha=0.6, label='Markov')
# ax.set_xlabel('Number of moves')
# ax.set_ylabel('Probability of winning')
#
# plt.show()
