import sys
sys.path.append('..')
import group

def main():
    y1 = [2.300, 2.155, 2.206, 2.259, 2.149, 2.641]
    y2 = [2.841, 2.907, 2.953, 2.885, 2.232, 3.151]
    
    xdata = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6']
    ydata = [y1, y2]
    yname = ['SA + Adaptive Sampling', 'RL + Adaptive Sampling']

    group.plot(xdata, ydata, yname, '', 'Improvement over\nsimulated annealing (TVM)', unit='x', xtick_center=True, geomean=True, topnum=True, save='group.pdf')

if __name__ == '__main__':
    main()
