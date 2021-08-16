from TableUtilities import *
import tkinter


class TkTable(tkinter.LabelFrame):
    """
    # TkTable: Customized simple tkinter widget Table
    has options for inserting data into
    ## Params
        @data: 2D array list
            ex: [[11,12,13],
                [21,22,23]]
        @header: header list value
            ex: ['head1', 'head2', 'head3']
        @index: index list value
            ex: [0,1,2]
        @geometrysystem: str value
            ex: 'pack' or 'grid'
        @celltype: str value
            ex: 'label' or 'entry'
        @*args: any other options for tkinter.LabelFrame Widget
            ex: bg, fg, labelanchor, text ... etc
        @**kwargs: any other options for tkinter.LabelFrame Widget in dictionary form
            ex: bg='#44ffaa', labelanchor='n' ... etc
    ## Options
        setdata   (set 2D array list data into body cells)
        setheader (set 1D array list data into header cells)
        setindex  (set 1D array list data into index cells)
        set   (modify cell data through its location row: int, column:int)
        get   (get cell data through its location row: int, column:int)
        pack  (overwritten)
        grid  (overwritten)
        place (overwritten)
        ... and all tkinter.labelframe methods
    """

    def __init__(
        self,
        master: tkinter.Widget,
        data: list,
        header: list = None,
        index: list = None,
        geometrysystem: str = "pack",
        celltype: str = "label",
        *args,
        **kwargs
    ):
        tkinter.LabelFrame.__init__(self, master, padx=5, pady=5, *args, **kwargs)

        self.geometrysystem = geometrysystem
        self.celltype = celltype
        self.index = index
        self.header = header
        self.data = data

        self.tablevariables = {
            "headers": ["index"],
            "index": [
                "",
            ],
            "data": [],
        }
        self.__loadoptions__()

    def __loadoptions__(self):
        if self.geometrysystem not in ["pack", "grid"]:
            raise ERRORS().UnknownGeometrySystem
        if self.celltype not in ["label", "entry"]:
            raise ERRORS().Unknowncelltype
        styles, options = getstyles(self.celltype, self.geometrysystem)
        self.styles = styles()
        self.options = options()

    def setheader(self, headeritems: list):
        "Create Table Headers Cells"
        variablelist = []
        if self.geometrysystem == "grid":
            master = self
        elif self.geometrysystem == "pack":
            rowframe = tkinter.LabelFrame(
                self, relief="flat", bg=self.config("background")[-1]
            )
            rowframe.pack(**self.options.row_frame, side="top")
            master = rowframe
        else:
            raise ERRORS().UnknownGeometrySystem

        for cindex, item in enumerate(headeritems):
            cellbox = cell(self.celltype, master, item, **self.styles.header)
            if self.geometrysystem == "grid":
                cellbox.grid(row=0, column=cindex + 1, **self.options.item)
            elif self.geometrysystem == "pack":
                cellbox.pack(**self.options.item)
            else:
                raise ERRORS().UnknownGeometrySystem

            variablelist.append(cellbox.ID)
        self.tablevariables["headers"].extend(variablelist)

    def setindex(self, indexitems: list):
        "Create Table Index Cells"
        if self.geometrysystem == "grid":
            variablelist = []
            for rindex, item in enumerate(indexitems):
                cellbox = cell(self.celltype, self, item, **self.styles.index)
                variablelist.append(cellbox.ID)
                cellbox.grid(row=rindex + 1, column=0, **self.options.item)
            self.tablevariables["index"].extend(variablelist)
        else:
            _ = ERRORS().NotAvailable

    def setdata(self):
        "Create Table Cells and set Data into"
        # iterate Over Rows
        for rindex, row in enumerate(self.data):
            variablelist = []
            if self.geometrysystem == "grid":
                master = self
            elif self.geometrysystem == "pack":
                rowframe = tkinter.LabelFrame(
                    self, relief="flat", bg=self.config("background")[-1]
                )
                rowframe.pack(**self.options.row_frame, side="top")
                master = rowframe
            # iterate Over Row items [ie, columns]
            for cindex, item in enumerate(row):
                cellbox = cell(self.celltype, master, item, **self.styles.item)
                variablelist.append(cellbox.ID)
                if self.geometrysystem == "grid":
                    cellbox.grid(row=rindex + 1, column=cindex + 1, **self.options.item)
                elif self.geometrysystem == "pack":
                    cellbox.pack(**self.options.item)
                else:
                    raise ERRORS().UnknownGeometrySystem
            self.tablevariables["data"].extend([variablelist])

    def set(self, row: int, col: int, info: str):
        "Method to set or edit data to cells according to r: row, c: column, info:'new data'"
        self.tablevariables["data"][row][col].set(info)

    def get(self, row: int, col: int):
        "Method to return cell variable located at r: row, c:column from the table"
        return self.tablevariables["data"][row][col]

    def __apply__(self):
        "Method to Apply Settings to Widget itself"
        if self.header is not None:
            self.setheader(self.header)
        if self.index is not None:
            self.setindex(self.index)
        self.setdata()

    def pack(self, *args, **kwargs):
        "Method to pack widget according to side"
        self.__apply__()
        super().pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        "Method to gird widget according to row, column tabled system"
        self.__apply__()
        super().grid(*args, **kwargs)

    def place(self, *args, **kwargs):
        "Method to place widget according to x,y Coordinates"
        self.__apply__()
        super().place(*args, **kwargs)
