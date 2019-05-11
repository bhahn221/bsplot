def plot(x, y, s, g, c, xlabel, ylabel, s_scale=50, tex=False, xtick_range=None, xtick_interval=None, ytick_range=None, ytick_interval=None, figsize=(7, 7), fontsize=18, title=None, title_fontsize=20, save=None):
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
    s = list(s)

    # s - scale
    s = [sp * s_scale for sp in s]
    
    # c - default
    from color_chart import color_chart
    color_list = [color_chart[c[gi]] for gi in g]

    # plot
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.scatter(x, y, s, c=color_list, alpha=0.5)

    # axis
    ax.set_xlabel(xlabel, size=fontsize)
    ax.set_ylabel(ylabel, size=fontsize)

    # y tick - default
    if xtick_interval == None:
        xtick_interval = 1.0
    if type(xtick_range) == type(None) and xtick_range == None:
        xtick_range = np.arange(0, max(y) + 1.0, xtick_interval)
    
    # x tick - set
    ax.set_xticks(xtick_range)
    ax.set_xticklabels(xtick_range, fontsize=fontsize)
    plt.ylim(0, max(xtick_range))

    # y tick - default
    if ytick_interval == None:
        ytick_interval = 1.0
    if type(ytick_range) == type(None) and ytick_range == None:
        ytick_range = np.arange(0, max(y) + 1.0, ytick_interval)

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
