import matplotlib.pyplot as plt
from matplotlib import use
import numpy as np

from PlotModifiers import PlotModifiers

class MultiPlotModifiers:
    def __init__(self, plot_modifiers: list[list[PlotModifiers]], has_same_x_axes=False, has_same_y_axes=False,
                 has_extra_titles=False, has_extra_secondary_titles=False):
        """
        @param plot_modifiers: a matrix of PlotModifier objects that correspond to axes in the multiplot
        @param has_same_x_axes: removes unneeded x-tick labels if True
        @param has_same_y_axes: removes unneeded y-tick labels if True
        @param has_extra_titles: removes unneeded internal titles if True
        @param has_extra_secondary_titles: removes unneeded internal secondary titles if True
        """
        self.plot_modifiers = plot_modifiers
        self.n_rows = len(plot_modifiers)
        self.n_cols = len(plot_modifiers[0])

        self.has_same_x_axes = has_same_x_axes
        self.has_same_y_axes = has_same_y_axes

        self.has_extra_titles = has_extra_titles
        self.has_extra_secondary_titles = has_extra_secondary_titles

    def apply(self, axes):
        """
        @param axes: an axes object, or a 1D or 2D list of Axis objects, the dimension of which must match plot_modifiers
        @return: void
        """

        if self.has_extra_titles:
            self._remove_extra_titles()

        if self.has_extra_secondary_titles:
            self._remove_extra_secondary_titles()

        for row_idx in range(self.n_rows):
            for col_idx in range(self.n_cols):
                self.plot_modifiers[row_idx][col_idx].apply(self._get_ax(axes, row_idx, col_idx))

        if self.has_same_x_axes:
            self._remove_internal_x_tick_labels(axes)
            if not self._check_columns_have_similar_limits():
                print("WARNING: Columns do not have similar limits")

        if self.has_same_y_axes:
            self._remove_internal_y_tick_labels(axes)
            if not self._check_rows_have_similar_limits():
                print("WARNING: Rows do not have similar limits")

    def _remove_internal_x_tick_labels(self, axes: plt.Axes):
        for row_idx in range(self.n_rows-1):
            for col_idx in range(self.n_cols):
                ax = self._get_ax(axes, row_idx, col_idx)
                ax.set_xticklabels([])
                ax.set_xlabel(None)

    def _remove_internal_y_tick_labels(self, axes: plt.Axes):
        for row_idx in range(self.n_rows):
            for col_idx in range(1, self.n_cols):
                ax = self._get_ax(axes, row_idx, col_idx)
                ax.set_yticklabels([])
                ax.set_ylabel(None)

    def _remove_extra_titles(self):
        for row_idx in range(1, self.n_rows):
            for col_idx in range(self.n_cols):
                self.plot_modifiers[row_idx][col_idx].title = None

    def _remove_extra_secondary_titles(self):
        for row_idx in range(self.n_rows):
            for col_idx in range(self.n_cols-1):
                self.plot_modifiers[row_idx][col_idx].secondary_title = None

    def _get_ax(self, axes, row_idx: int, col_idx:int ) -> plt.Axes:
        if self.n_rows == 1:
            return axes[col_idx]
        elif self.n_cols == 1:
            return axes[row_idx]
        else:
            return axes[row_idx][col_idx]

    def _check_columns_have_similar_limits(self):
        for col_idx in range(self.n_cols):
            limit_list = list()
            for row_idx in range(self.n_rows):
                limit_list.append(self.plot_modifiers[row_idx][col_idx].xlim)

            for i in range(1, len(limit_list)):
                if limit_list[i] is None or limit_list[i] != limit_list[i-1]:
                    return False

        return True

    def _check_rows_have_similar_limits(self):
        for row_idx in range(self.n_rows):
            limit_list = list()
            for col_idx in range(self.n_cols):
                limit_list.append(self.plot_modifiers[row_idx][col_idx].ylim)

            for i in range(1, len(limit_list)):
                if limit_list[i] is None or limit_list[i] != limit_list[i - 1]:
                    return False

        return True



def main():
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "Helvetica",
        "font.size": 6,
        'figure.autolayout': True
    })

    n_rows, n_cols = 5, 5
    plot_modifiers = [[PlotModifiers(title="Primary", secondary_title="Secondary", xlim=[-1,5], ylim=[-1,5], xlabel="$x$")
                       for _ in range(n_cols)] for _ in range(n_rows)]

    mpm = MultiPlotModifiers(plot_modifiers, has_same_x_axes=True, has_same_y_axes=True,
                             has_extra_titles=True, has_extra_secondary_titles=True)

    fig, axes = plt.subplots(n_rows, n_cols)
    for i in range(n_rows):
        for j in range(n_cols):
            axes[i][j].plot(np.linspace(-1,i), np.linspace(-1,j))

    mpm.apply(axes)
    plt.show()
    print(mpm.n_rows, mpm.n_cols)

    return 0

if __name__ == '__main__':
    main()

