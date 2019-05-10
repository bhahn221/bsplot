import sys
sys.path.append('..')
import scatter

import numpy as np

def main():
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [1, 2, 3, 4, 5, 6, 7, 8]
    s = [1, 1, 3, 3, 2, 2, 4, 4]
    
    scatter.plot(x, y, s, r'tile\textsubscript{x}', r'tile\textsubscript{y}', label_tex=True, xtick_range=np.arange(0, 10, 1), xtick_interval=2, ytick_range=np.arange(0, 10, 1), ytick_interval=2, save='scatter.pdf')

if __name__ == '__main__':
    main()
