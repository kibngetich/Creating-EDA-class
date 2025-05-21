import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        pass

    def histogram(self, x, bins=None, range=None, density=False, weights=None,
                  cumulative=False, bottom=None, histtype='bar', align='mid',
                  orientation='vertical', rwidth=None, log=False, color=None,
                  label=None, stacked=False, xlabel="Value", ylabel="Frequency",
                  title="Histogram", figsize=(15, 10), alpha=1.0, edgecolor='black',
                  linewidth=1, label_fontsize=12, title_fontsize=14, grid=True,
                  save_path=None, show=True, *, data=None, **kwargs):

        plt.figure(figsize=figsize)
        plt.hist(x, bins=bins, range=range, density=density, weights=weights,
                 cumulative=cumulative, bottom=bottom, histtype=histtype,
                 align=align, orientation=orientation, rwidth=rwidth,
                 log=log, color=color, label=label, stacked=stacked,
                 alpha=alpha, edgecolor=edgecolor, linewidth=linewidth,
                 data=data, **kwargs)

        plt.xlabel(xlabel, fontsize=label_fontsize)
        plt.ylabel(ylabel, fontsize=label_fontsize)
        plt.title(title, fontsize=title_fontsize)
        if label:
            plt.legend()
        if grid:
            plt.grid(True)
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        if show:
            plt.show()

    def line(self, x, y, xlabel="X-axis", ylabel="Y-axis", title="Line Plot",
             figsize=(15, 10), color='blue', linestyle='-', linewidth=2,
             label=None, label_fontsize=12, title_fontsize=14, grid=True,
             save_path=None, show=True, **kwargs):

        plt.figure(figsize=figsize)
        plt.plot(x, y, color=color, linestyle=linestyle, linewidth=linewidth, label=label, **kwargs)
        plt.xlabel(xlabel, fontsize=label_fontsize)
        plt.ylabel(ylabel, fontsize=label_fontsize)
        plt.title(title, fontsize=title_fontsize)
        if label:
            plt.legend()
        if grid:
            plt.grid(True)
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        if show:
            plt.show()

    def scatter(self, x, y, xlabel="X-axis", ylabel="Y-axis", title="Scatter Plot",
                figsize=(15, 10), color='blue', alpha=1.0, edgecolor='black',
                label=None, label_fontsize=12, title_fontsize=14, grid=True,
                save_path=None, show=True, **kwargs):

        plt.figure(figsize=figsize)
        plt.scatter(x, y, color=color, alpha=alpha, edgecolor=edgecolor, label=label, **kwargs)
        plt.xlabel(xlabel, fontsize=label_fontsize)
        plt.ylabel(ylabel, fontsize=label_fontsize)
        plt.title(title, fontsize=title_fontsize)
        if label:
            plt.legend()
        if grid:
            plt.grid(True)
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        if show:
            plt.show()

    def bar(self, x, height, xlabel="X-axis", ylabel="Height", title="Bar Plot",
            figsize=(15, 10), color='blue', edgecolor='black', alpha=1.0,
            label=None, label_fontsize=12, title_fontsize=14, grid=True,
            save_path=None, show=True, **kwargs):

        plt.figure(figsize=figsize)
        plt.bar(x, height, color=color, edgecolor=edgecolor, alpha=alpha, label=label, **kwargs)
        plt.xlabel(xlabel, fontsize=label_fontsize)
        plt.ylabel(ylabel, fontsize=label_fontsize)
        plt.title(title, fontsize=title_fontsize)
        if label:
            plt.legend()
        if grid:
            plt.grid(True)
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        if show:
            plt.show()
