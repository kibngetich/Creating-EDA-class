
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


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
     
    def boxplot(self, data, x=None, y=None, hue=None, title="Box Plot",
                xlabel=None, ylabel=None, figsize=(15, 10), palette='Set2',
                title_fontsize=14, label_fontsize=12, grid=True, save_path=None, show=True, **kwargs):

        plt.figure(figsize=figsize)
        sns.boxplot(data=data, x=x, y=y, hue=hue, palette=palette, **kwargs)
        plt.title(title, fontsize=title_fontsize)
        if xlabel: plt.xlabel(xlabel, fontsize=label_fontsize)
        if ylabel: plt.ylabel(ylabel, fontsize=label_fontsize)
        if grid: plt.grid(True)
        if save_path: plt.savefig(save_path, bbox_inches='tight')
        if show: plt.show()

    def violinplot(self, data, x=None, y=None, hue=None, title="Violin Plot",
                   xlabel=None, ylabel=None, figsize=(15, 10), palette='Set2',
                   title_fontsize=14, label_fontsize=12, grid=True, save_path=None, show=True, **kwargs):

        plt.figure(figsize=figsize)
        sns.violinplot(data=data, x=x, y=y, hue=hue, palette=palette, **kwargs)
        plt.title(title, fontsize=title_fontsize)
        if xlabel: plt.xlabel(xlabel, fontsize=label_fontsize)
        if ylabel: plt.ylabel(ylabel, fontsize=label_fontsize)
        if grid: plt.grid(True)
        if save_path: plt.savefig(save_path, bbox_inches='tight')
        if show: plt.show()

    def heatmap(self, data, annot=True, cmap='coolwarm', title="Heatmap",
                figsize=(15, 10), title_fontsize=14, cbar=True, save_path=None, show=True, **kwargs):

        plt.figure(figsize=figsize)
        sns.heatmap(data, annot=annot, cmap=cmap, cbar=cbar, **kwargs)
        plt.title(title, fontsize=title_fontsize)
        if save_path: plt.savefig(save_path, bbox_inches='tight')
        if show: plt.show()

    def pairplot(self, data, hue=None, palette='Set2', diag_kind='kde',
                 title=None, save_path=None, show=True, **kwargs):

        g = sns.pairplot(data=data, hue=hue, palette=palette, diag_kind=diag_kind, **kwargs)
        if title:
            g.fig.suptitle(title, y=1.02)
        if save_path:
            g.savefig(save_path, bbox_inches='tight')
        if show:
            plt.show()

    def countplot(self, data, x, hue=None, title="Count Plot",
                  xlabel=None, ylabel="Count", figsize=(15, 10),
                  palette='Set2', title_fontsize=14, label_fontsize=12,
                  grid=True, save_path=None, show=True, **kwargs):

        plt.figure(figsize=figsize)
        sns.countplot(data=data, x=x, hue=hue, palette=palette, **kwargs)
        plt.title(title, fontsize=title_fontsize)
        if xlabel: plt.xlabel(xlabel, fontsize=label_fontsize)
        if ylabel: plt.ylabel(ylabel, fontsize=label_fontsize)
        if grid: plt.grid(True)
        if save_path: plt.savefig(save_path, bbox_inches='tight')
        if show: plt.show()