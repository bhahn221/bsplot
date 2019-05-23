# TODO change this with more elegant method
# line options: solid, dash, dot, mix
class LegendObject(object):
    def __init__(self, color, line):
        import numpy as np
        self.color = (np.array(color) + np.array((1.0, 1.0, 1.0))) * 0.5
        self.line = line

    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        # import packages
        import matplotlib.patches as mpatches

        # draw default box for solid line
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        height = height / 2
        patch = mpatches.Rectangle(
            [x0, y0+2*height/3], width, height, facecolor=(0, 0, 0),
            edgecolor=self.color, lw=4)
        handlebox.add_artist(patch)

        if self.line == '--':
            patch1 = mpatches.Rectangle(
                [x0 + 6*width/13, y0+2*height/3],  width/13, height, facecolor=self.color,
                transform=handlebox.get_transform())
            handlebox.add_artist(patch1)
        elif self.line == ':':
            patch1 = mpatches.Rectangle(
                [x0 + 2*width/13, y0+2*height/3],  width/13, height, facecolor=self.color,
                transform=handlebox.get_transform())
            patch2 = mpatches.Rectangle(
                [x0 + 4*width/13, y0+2*height/3],  width/13, height, facecolor=self.color,
                transform=handlebox.get_transform())
            patch3 = mpatches.Rectangle(
                [x0 + 6*width/13, y0+2*height/3],  width/13, height, facecolor=self.color,
                transform=handlebox.get_transform())
            patch4 = mpatches.Rectangle(
                [x0 + 8*width/13, y0+2*height/3],  width/13, height, facecolor=self.color,
                transform=handlebox.get_transform())
            patch5 = mpatches.Rectangle(
                [x0 + 10*width/13, y0+2*height/3],  width/13, height, facecolor=self.color,
                transform=handlebox.get_transform())
            handlebox.add_artist(patch1)
            handlebox.add_artist(patch2)
            handlebox.add_artist(patch3)
            handlebox.add_artist(patch4)
            handlebox.add_artist(patch5)
        elif self.line == '-.':
            patch1 = mpatches.Rectangle(
                [x0 + 5*width/13, y0+2*height/3],  width/13, height, facecolor=self.color,
                transform=handlebox.get_transform())
            patch2 = mpatches.Rectangle(
                [x0 + 7*width/13, y0+2*height/3],  width/13, height, facecolor=self.color,
                transform=handlebox.get_transform())
            handlebox.add_artist(patch1)
            handlebox.add_artist(patch2)
        else:
            assert self.line == '', 'line should be either \'\', \'--\', \':\', or \'-.\''

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

def plot(xlist, ylist, yname, l, c, xlabel, ylabel, legend=None, tex=False, xtick_range=None, xtick_interval=None, ytick_range=None, ytick_interval=None, figsize=(10, 5), fontsize=18, title=None, title_fontsize=20, save=None):
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
        # draw lines
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
    
    # set line shape
    handler_map = {}
    for i in range(len(yname)):
        handler_map[i] = LegendObject(color_list[i], l[i])

    # legend
    if legend != None:
        plt.legend(range(len(yname)), yname, handler_map=handler_map, 
               fontsize=fontsize, fancybox=False, edgecolor=(0, 0, 0))

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
