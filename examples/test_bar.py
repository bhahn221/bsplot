import sys
sys.path.append('..')
import bar

def main():
    x = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6']
    y = [2.293, 3.132, 2.623, 2.766, 3.006, 2.152]
    
    bar.plot(x, y, '', 'Improvement over\nsimulated annealing (TVM)', unit='x', xtick_center=True, geomean=True, topnum=True, save='bar.pdf')

if __name__ == '__main__':
    main()
