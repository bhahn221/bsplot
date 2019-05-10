import sys
sys.path.append('..')
import stack

def main():
    y1 = [2659.821429,1765.803571,2049.464286,2101.875,2928.839286,3388.392857,3615.803571,3046.696429,4136.517857,4875.267857,2752.053571,6586.428571]
    y2 = [725.6473214,249.0401786,449.8325893,386.71875,382.4888393,495.7477679,634.8214286,477.8348214,777.7790179,625.9040179,717.6339286,947.1651786]
    
    y1 = [y/3600 for y in y1]
    y2 = [y/3600 for y in y2]
    
    xdata = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12']
    ydata = [y1, y2]
    yname = ['Physical Measurement', 'Search Algorithm']

    stack.plot(xdata, ydata, yname, '', 'Optimization Time (Hours)', unit='H', xtick_center=True, ytick_interval=0.5, geomean=False, topnum=True, topnum_type='percentage', topnum_index=[0], save='stack.pdf')

if __name__ == '__main__':
    main()
