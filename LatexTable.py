from tabulate import tabulate


class LatexTable:
    def __init__(self, table: list[list], header: list = None, first_col: list = None):
        """
        @param table: The table content, a 2D list.
        @param header: The table header.
        @param first_col: A 1D list specifying values of the leftmost column.
        """
        self.table = table
        self.header = header
        self.first_col = first_col
        self._validate()

    def print(self):
        out_table = self.generate_out_table()
        if self.header is not None:
            print(tabulate(out_table[1:], headers=self.header, tablefmt="fancy_grid"))
        else:
            print(tabulate(out_table, tablefmt="fancy_grid"))

    def print_latex(self, add_dollars=False) -> None:
        """
        @param add_dollars: Adds $ symbols to each cell
        """
        out_table = self.generate_out_table()
        if add_dollars:
            out_table = [[f"${col}$" for col in row] for row in out_table]
        else:
            out_table = [[str(col) for col in row] for row in out_table]


        print(" \\\ \n".join(" & ".join(row) for row in out_table))

    def generate_out_table(self):
        out_table = list()
        if self.header is not None:
            out_table.append(self.header)
        for idx, row in enumerate(self.table):
            if self.first_col is not None:
                row.insert(0, self.first_col[idx])
                out_table.append(row)
            else:
                out_table.append(row)

        return out_table

    def round(self, decimal_places: int = 0):
        for row_idx, col in enumerate(self.table):
            for col_idx, value in enumerate(col):
                try:
                    self.table[row_idx][col_idx] = round(value, decimal_places)
                except:
                    pass

    def _validate(self) -> None:
        if self.first_col is None and self.header is None:
            return
        elif self.first_col is None and (len(self.table[0]) != len(self.header)):
            raise ValueError(f"Table is invalid. Header has {len(self.header)} columns and table has"
                             f" {len(self.table[0])}.")
        elif self.first_col is not None and len(self.table[0]) + 1 != (len(self.header)):
            raise ValueError(f"Table is invalid. Header has {len(self.header)} columns and table has"
                             f" {len(self.table[0]) + 1}, including the extra column.")
