import collections

class Table:

    def __init__(self):
        self.rows = []
        self.rows_str = []
        self.header_row = []
        self.number_of_rows = 0

    def create_header(self, *argv):
        for arg in argv:
            self.header_row.append(arg)
    
    def add_row(self, *argv):
        row = []
        for arg in argv:
            row.append(arg)
        self.rows.append(row)

    def remove_duplicates_from_list(self, arg_list):
        return list(OrderedDict.fromkeys(arg_list))

    def collapse_col(self, col):

        unique_elements = {}
        new_rows = []
        new_rows_str = []

        if col in self.header_row:
            
            col_index = self.header_row.index(col)

            for row_number in number_of_rows:

                col_value = self.rows[row_number][col_index]

                if col_value not in unique_elements:                  
                    unique_elements[col_value] = []

                unique_elements[col_value].append(row_number)

            for key in unique_elements.keys():
                
                row = []
                row_str = []
                for temp_col in len(self.header_row) - 1:
                    cell        = []
                    cell_str    = ""
                    for duplicate_id in unique_elements[key]:
                        cell.append(self.rows[duplicate_id][temp_col])
                        cell = self.remove_duplicates_from_list(cell)
                    row.append(cell)

                    for value in cell:
                        cell_str += ", " + str(value) 

                    row_str.append(cell_str)
                
                new_rows.append(row)
                new_rows_str.append(rows_str)
        
            self.rows = new_rows
            self.rows_str = new_rows_str


                

            
