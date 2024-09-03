import matplotlib.pyplot as plt
from matplotlib import use
import numpy as np

class PlotModifiers:
    def __init__(self, xlabel=None, ylabel=None, title=None, secondary_title=None, xlim=None, ylim=None, grid=False,
                 legend=False,title_align=None, format_origin=False, scale_x=None, scale_y=None, scientific_x=False,
                 scientific_y=False):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.secondary_title = secondary_title
        self.title_align = title_align
        self.xlim = xlim
        self.ylim = ylim
        self.grid = grid
        self.legend = legend
        self.format_origin = format_origin
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.scientific_x = scientific_x
        self.scientific_y = scientific_y

    def apply(self, ax: plt.Axes):
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_title(self.title, loc=self.title_align)
        if self.secondary_title is not None:
            self._add_secondary_title(ax)
        if self.xlim is not None:
            ax.set_xlim(self.xlim)
        if self.ylim is not None:
            ax.set_ylim(self.ylim)
        if self.grid:
            ax.grid()
        if self.legend:
            ax.legend()
        if self.format_origin:
            self._format_tick_labels(ax)
        if self.scale_x is not None:
            ax.set_xscale(self.scale_x)
        if self.scale_y is not None:
            ax.set_yscale(self.scale_y)

        if self.scientific_x:
            ax.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
        if self.scientific_y:
            ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    def _add_secondary_title(self, ax):
        ax2 = ax.twinx()
        ax2.set_ylabel(self.secondary_title)
        ax2.set_yticks([])


    def _format_tick_labels(self, ax):
        # This method removes decimals from the tick label at 0.
        # Warning: This formatting is not compatible with scientific notation.
        formatted_origin_str = r'$\mathdefault{0}$'

        values = ax.get_xticks()
        labels = [item.get_text() for item in ax.get_xticklabels()]
        idx, = (np.where(values == 0))[0]
        labels[idx] = formatted_origin_str
        ax.set_xticks(values)
        ax.set_xticklabels(labels)

        values = ax.get_yticks()
        labels = [item.get_text() for item in ax.get_yticklabels()]
        idx, = (np.where(values == 0))[0]
        labels[idx] = formatted_origin_str
        ax.set_yticks(values)
        ax.set_yticklabels(labels)

        if max(abs(values)) <= 1e-4 or max(abs(values)) >= 1e6:
            print("Warning: Scientific notation is omitted, axis values may be wrong.")
