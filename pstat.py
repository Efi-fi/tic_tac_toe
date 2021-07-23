from txt_game.tic_tac_toe.statistics import gen_common_stat, get_seq_stat
from txt_game.visual import visualize_seq
import matplotlib
import numpy as np

from matplotlib import pyplot as plt


def main():
    common_stat = gen_common_stat()
    seq_stat = get_seq_stat(list(common_stat['Moves'].keys()), list(common_stat['Moves'].values()))
    print(seq_stat)

    x = seq_stat['xlst']
    x = np.array([x[0] - 1] + list(x) + [x[-1] + 1])
    y = seq_stat['ylst']
    y = np.array([0] + list(y) + [0])
    # print(x)
    # print(y)

    fig, ax = plt.subplots()  # Create a figure and an axes.
    dist_prob = [y[0]]
    for value in y[1:]:
        dist_prob.append(value + dist_prob[-1])
    summ = dist_prob[-1]
    dist_prob = [i * 100 / summ for i in dist_prob]
    dist_prob_dens = [i * 100 / summ for i in y]

    avg = sum([dist_prob_dens[i] * x[i] / 100 for i in range(len(dist_prob_dens))])
    dispersion = sum([dist_prob_dens[i] * ((x[i] - avg) ** 2) / 100 for i in range(len(dist_prob_dens))])
    std = dispersion ** 0.5

    print('Average:', avg)
    print('Standart deviation: ', std)
    x_ideal = np.arange(x[0], x[-1] + 1, 0.1)
    y_ideal = np.exp(-np.square(x_ideal - avg) / (2 * std ** 2)) / (np.sqrt(2 * np.pi) * std) * 100

    # print(dist_prob_dens)
    l1, = ax.plot(x, dist_prob, ls='--', lw=3, mec='blue', alpha=0.8)
    l1.set_label('Probability distribution')
    l2, = ax.plot(x, dist_prob_dens, mew=1, mec='green')
    l2.set_label('Probability density distribution')
    s1 = ax.scatter(x, dist_prob_dens, c='red')
    l3, = ax.plot(x_ideal, y_ideal)
    l3.set_label('Normal probability density')
    ax.set_xlabel('Number of moves')  # Add an x-label to the axes.
    ax.set_ylabel('Probability, %')  # Add a y-label to the axes.
    ax.set_title("Moves per game")  # Add a title to the axes.
    ax.grid()
    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()
