import sys
sys.path.append('..')
import line

def main():
    x0_0 = [0, 8, 16, 24, 32, 40]
    y0_0 = [0, 2, 3, 4, 5, 6]
    x0_1 = [0, 8, 16, 24, 32, 40, 48]
    y0_1 = [0, 1, 4, 4, 5, 7, 7]
    
    x1_0 = [0, 8, 16, 24, 32]
    y1_0 = [0, 4, 6, 6, 7,]
    x1_1 = [0, 8, 16, 24, 32]
    y1_1 = [0, 3, 5, 5, 6]

    x2_0 = [0, 8, 16, 24, 32, 40, 48, 56, 64]
    y2_0 = [0, 7, 7, 7, 7, 7, 8, 8, 9]
    x2_1 = [0, 8, 16, 24, 32, 40, 48, 56, 64]
    y2_1 = [0, 6, 6, 7, 7, 8, 8, 8, 9]
    
    x3_0 = [0, 8, 16, 24, 32, 40, 48, 56, 64]
    y3_0 = [0, 10, 11, 12, 12, 12, 12, 12, 12]
    x3_1 = [0, 8, 16, 24, 32, 40, 48, 56, 64]
    y3_1 = [0, 7, 8, 9, 10, 11, 12, 12, 12]
    
    x = [[x0_0, x0_1], [x1_0, x1_1], [x2_0, x2_1], [x3_0, x3_1]]
    y = [[y0_0, y0_1], [y1_0, y1_1], [y2_0, y2_1], [y3_0, y3_1]]
    yname = ['Simulated Annealing (TVM)', 'Reinforcement Learning', 'Simulated Annealing + Adaptive Sampling', 'Reinforcment Learning + Simulated Annealing (ReLeASE)']

    l = ['--', ':', '-.', ''] 
    c = ['yellow', 'red', 'green', 'blue']

    line.plot(x, y, yname, l, c, 'Physical Measurements', 'TFLOPS', xtick_interval=8, ytick_interval=4, save='line.pdf')

if __name__ == '__main__':
    main()
