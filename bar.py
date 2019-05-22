def plot(x, y, xlabel, ylabel, tex=False, xtick_center=False, xtick_rot=0, ytick_range=None, ytick_interval=None, unit='', geomean=False, geomean_name='long', topnum=False, topnum_rot=0, figsize=(10, 5), barwidth=0.7, fontsize=18, colorscheme='blue', title=None, title_fontsize=20, save=None, horizontal_one=False):
    # import packages
    if tex == True:
        import matplotlib
        matplotlib.rcParams['text.usetex'] = True
        matplotlib.rcParams['text.latex.unicode'] = True
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats.mstats import gmean

    # data to list
    x = list(x)
    y = list(y)

    # geomean - add data
    if geomean == True:
        if geomean_name == 'short':
            x.append('gm')
        else:
            x.append('geomean')
        y.append(gmean(y))

    # colorscheme
    if colorscheme == 'blue':
        color = (0.1, 0.1, 0.4)

    # plot
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    rects = ax.bar(x, y, color=color, width=barwidth)

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
        # tick labels
        ax.set_xticks(np.arange(0, len(x) + 1.0, 1.0))
        ax.set_xticklabels(x, rotation=xtick_rot, fontsize=fontsize)

    # x tick - limit
    plt.xlim(-0.5, len(x) - 0.5)

    y_max = 0
    for yd in y:
        if yd > y_max:
            y_max = yd
    
    # y tick - default
    if ytick_interval == None:
        ytick_interval = 1.0
    if type(ytick_range) == type(None):
        ytick_range = np.arange(0, max(y) + 1.0, ytick_interval)

    # y tick - set
    ax.set_yticks(ytick_range)
    #ax.set_yticklabels([str(n) + unit for n in list(ytick_range)], fontsize=fontsize)
    ax.set_yticklabels([str(round(n, 2)) + unit for n in list(ytick_range)], fontsize=fontsize)

    # y tick - limit
    #plt.ylim(0, max(ytick_range))
    plt.ylim(min(ytick_range), max(ytick_range))

    # number on top
    if topnum == True:
        for rect in rects:
            height = rect.get_height()
            if y_max < 3:
                ax.text(rect.get_x() + rect.get_width() / 2., height + 0.005, 
                    '%.2f' % height + unit, 
                    ha='center', va='bottom', size=fontsize, rotation=topnum_rot)
            else:
                ax.text(rect.get_x() + rect.get_width() / 2., height + 0.2, 
                    '%.2f' % height + unit, 
                    ha='center', va='bottom', size=fontsize, rotation=topnum_rot)

    # title
    if title != None:
        plt.title(title, size=20)

    # geomean - add line
    if geomean == True:
        plt.axvline(len(x) - 1.5, ymin=0, ymax=max(y) + 1.0, color=(0, 0, 0))

    # FIXME
    if horizontal_one == True:
        plt.axhline(1.0, xmin=0, xmax=len(x), linestyle='--', color=(1, 1, 1))

    # tight layout
    fig.tight_layout()

    # save
    if save != None:
        fig.savefig(save)

    # show
    plt.show()
