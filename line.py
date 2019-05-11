def merge_data(xdatas, ydatas):
    # x - find longest
    xlist_concat = [x for xdata in xdatas for x in xdata]
    x_max = max(xlist_concat)

    # y - fill middle values
    ylist_new = []
    for i, ydata in enumerate(ydatas): 
        ydata_new = []
        for j, y in enumerate(ydata):
            if j+1 == len(ydata):
                break
            ydata_new = ydata_new + [y] * (xdatas[i][j+1] - len(ydata_new))
        ylist_new.append(ydata_new)

    # y - pad to longest
    import numpy as np
    for i in range(x_max):
        y_index = [j for j, ydata in enumerate(ylist_new) if i >= len(ydata)]
        y_new = np.mean([ydata[i] for ydata in ylist_new if i < len(ydata)])
        for yi in y_index:
            ylist_new[yi] = ylist_new[yi] + [y_new]

    return range(0, x_max), ylist_new

def plot(xlist, ylist, l, c, xlabel, ylabel, tex=False, xtick_range=None, xtick_interval=None, ytick_range=None, ytick_interval=None, figsize=(10, 5), fontsize=18, title=None, title_fontsize=20, save=None):
    # import packages
    if tex == True:
        import matplotlib
        matplotlib.rcParams['text.usetex'] = True
        matplotlib.rcParams['text.latex.unicode'] = True
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats.mstats import gmean

    # data to list
    xlist = [list(xd) for xd in xlist]
    ylist = [list(yd) for yd in ylist]

    # assertion for data
    assert len(xlist) == len(ylist), 'length of x needs to be equal to length of y'

    # c - default
    from color_chart import color_chart
    color_list = [color_chart[ci] for ci in c]

    # plot
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    for i, (xdatas, ydatas) in enumerate(zip(xlist, ylist)):
        xdata_new, ydata_new = merge_data(xdatas, ydatas)
        ydata_mean = np.mean(ydata_new, axis=0)
        ydata_max = np.max(ydata_new, axis=0)
        ydata_min = np.min(ydata_new, axis=0)

        ax.plot(xdata_new, ydata_mean, 'k'+l[i])
        ax.fill_between(xdata_new, ydata_max, ydata_min,
                        color=color_list[i], alpha=0.3)

    # axis
    ax.set_xlabel(xlabel, size=fontsize)
    ax.set_ylabel(ylabel, size=fontsize)
    
    # x/y tick - find range
    xlist_concat = [x for xdatas in xlist for xdata in xdatas for x in xdata]
    ylist_concat = [y for ydatas in ylist for ydata in ydatas for y in ydata]

    # x tick - default
    if xtick_interval == None:
        xtick_interval = 1.0
    if type(xtick_range) == type(None) and xtick_range == None:
        # TODO make datatype for xticklabel an option
        xtick_range = np.arange(0, max(xlist_concat) + 1.0, xtick_interval).astype(int)
    
    # x tick - set
    ax.set_xticks(xtick_range)
    ax.set_xticklabels(xtick_range, fontsize=fontsize)
    plt.xlim(0, max(xtick_range))

    # y tick - default
    if ytick_interval == None:
        ytick_interval = 1.0
    if type(ytick_range) == type(None) and ytick_range == None:
        ytick_range = np.arange(0, max(ylist_concat) + 1.0, ytick_interval)

    # y tick - set
    ax.set_yticks(ytick_range)
    ax.set_yticklabels(ytick_range, fontsize=fontsize)
    plt.ylim(0, max(ytick_range))
    
    # title
    if title != None:
        plt.title(title, size=20)

    # tight layout
    fig.tight_layout()

    # save
    if save != None:
        fig.savefig(save)

    # show
    plt.show()
