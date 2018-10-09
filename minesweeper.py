import numpy as np
import matplotlib.pyplot as plt


def simple_spread(n, m, p):
    s = set()
    while len(s) != p:
        s.add(np.random.randint(0, n * m))
    print(s)
    minesweeper = [[0 for i in range(n)] for j in range(m)]
    for i in s:
        r, c = divmod(i, n)
        minesweeper[r][c] = 1
    #print(minesweeper)
    plt.matshow(minesweeper)
    #plt.show()

def solve_endless_loop_spread(n, m, p):
    s = set()
    my_list = [(0,0) for x in range(n*m)]
    for x in range(n*m):
        r, c = divmod(x, n)
        my_list[x] = (r, c)

    while len(s) != p:
        current_p = np.random.randint(0, len(my_list))
        s.add(my_list[current_p])
        del my_list[current_p]

    print(s)
    minesweeper = [[0 for i in range(n)] for j in range(m)]
    for i in s:
        r,c = i[0],i[1]
        minesweeper[r][c] = 1
    #print(minesweeper)
    plt.matshow(minesweeper)
    plt.show()


def minesweeper_main():
    for x in range(5):
        n = 10#np.random.randint(1, 10)
        m = 10#np.random.randint(1, 10)
        p = np.random.randint(1, (n * m)/2)
        print (n,m,p)
        #simple_spread(n, m, p)
        solve_endless_loop_spread(n, m, p)


minesweeper_main()