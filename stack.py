def plot(xname, ydata, yname, xlabel, ylabel, tex=False, xtick_center=False, xtick_rot=0, ytick_range=None, ytick_interval=None, unit='', geomean=False, topnum=False, topnum_type=None, topnum_index=None, topnum_rot=90, figsize=(10, 5), barwidth=0.7, fontsize=18, colorscheme='blue', title=None, title_fontsize=20, save=None):
    # import packages
    if tex == True:
        import matplotlib
        matplotlib.rcParams['text.usetex'] = True
        matplotlib.rcParams['text.latex.unicode'] = True
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats.mstats import gmean

    # data to list
    x = list(xname)
    y = [list(yd) for yd in ydata]

    # assertions for data
    for yd in y:
        assert len(x) == len(yd), 'lengths of ydata elements need to be equal to length of xname'
    assert len(y) == len(yname), 'length of ydata needs to be equal to length of yname'

    # geomean - add data
    if geomean == True:
        x.append('geomean')
        for yd in y:
            yd.append(gmean(yd))

    # colorscheme
    if colorscheme == 'blue':
        color = (0.1, 0.1, 0.4)
        light = np.arange(1.0 / len(yname), 1.0 + 1.0 / len(yname), 1.0 / len(yname))
        light = light[::-1]

    # plot
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    bottoms_collection = []
    rects_collection = []
    for i, yd in enumerate(y):
        bottom = np.zeros(len(y[0])) if i == 0 else np.sum(y[:i], axis=0)
        rect = ax.bar(x, y[i], color=color + (light[i],), bottom=bottom, width=barwidth, label=yname[i])
        bottoms_collection.append(bottom)
        rects_collection.append(rect)

    # axis
    ax.set_xlabel(xlabel, size=fontsize)
    ax.set_ylabel(ylabel, size=fontsize)

    # x tick - set
    if xtick_center == True:
        # tick marks (major)
        ax.set_xticks(np.arange(0, len(x) + 1.0, 1.0) - 0.5)
        ax.set_xticklabels('')

        # tick labels (minor, tick marks removed)
        ax.set_xticks(np.arange(0, len(x) + 1.0, 1.0), minor=True)
        plt.tick_params(axis='x', which='minor', bottom=False, top=False)
        ax.set_xticklabels(x, rotation=xtick_rot, fontsize=fontsize, minor=True)
    else:
        # tick labels TODO
        ax.set_xticks(np.arange(0, len(x) + 1.0, 1.0))
        ax.set_xticklabels(x, rotation=xtick_rot, fontsize=fontsize)

    # x tick - limit
    plt.xlim(-0.5, len(x) - 0.5)

    # y tick - default
    if ytick_interval == None:
        ytick_interval = 1.0
    if ytick_range == None:
        y_sum = np.sum(y, axis=0)
        y_max = np.max(y_sum)
        ytick_range = np.arange(0, y_max + 1.0, ytick_interval)

    # y tick - set
    ax.set_yticks(ytick_range)
    ax.set_yticklabels([str(n) + unit for n in list(ytick_range)], fontsize=fontsize)

    # y tick - limit
    plt.ylim(0, max(ytick_range))

    # number on top
    if topnum == True:
        if topnum_type == 'percentage':
            y_sum = np.sum(y, axis=0)
            for i, rects in enumerate(rects_collection):
                if i not in topnum_index:
                    continue
                for j, rect in enumerate(rects):
                    height = rect.get_height()
                    ax.text(rect.get_x() + rect.get_width() / 2., 0.1, 
                            '%.2f' % (height / y_sum[j] * 100) + '%', 
                            ha='center', va='bottom', size=fontsize, rotation=topnum_rot, color=(1, 1, 1))
        else:
            for i, rects in enumerate(rects_collection):
                if i not in topnum_index:
                    continue
                for j, rect in enumerate(rects):
                    bottom = bottoms_collection[i][j]
                    height = bottom + rect.get_height()
                    ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, 
                            '%.2f' % height + unit, 
                            ha='center', va='bottom', size=fontsize, rotation=topnum_rot)

    # title
    if title != None:
        plt.title(title, size=20)

    # geomean - add line
    if geomean == True:
        plt.axvline(len(x) - 1.5, ymin=0, ymax=y_max + 1.0, color=(0, 0, 0))
    
    # legend
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1), ncol=2, 
              fancybox=False, edgecolor=(0, 0, 0), fontsize=fontsize)

    # tight layout
    fig.tight_layout()

    # save
    if save != None:
        fig.savefig(save)

    # show
    plt.show()
