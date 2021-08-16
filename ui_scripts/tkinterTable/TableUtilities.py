import tkinter

"TableUtilities Contain all TkTable Required Data to make things Available and Stylish !"


class LabelStyles:
    "Label Widget Styles"

    def __init__(self):
        self.item = {
            "padx": 5,
            "pady": 3,
            "relief": "solid",
            "bd": 1,
            "width": 12,
            "anchor": "w",
        }
        self.header = {
            "padx": 5,
            "pady": 3,
            "relief": "solid",
            "bd": 1,
            "width": 12,
            "anchor": "w",
            "font": ("Segoe UI", 9, "bold"),
            "foreground": "black",
            "background": "#dddddd",
        }
        self.index = {
            "padx": 5,
            "pady": 3,
            "relief": "solid",
            "bd": 1,
            "width": 12,
            "anchor": "w",
            "font": ("Segoe UI", 9, "bold"),
            "foreground": "black",
            "background": "#dddddd",
        }


class EntryStyles:
    "Entry Widget Styles"

    def __init__(self):
        self.item = {
            "relief": "solid",
            "bd": 1,
            "width": 12,
            "disabledforeground": "black",
            "state": "normal",
            "justify": "left",
        }

        self.header = {
            "relief": "solid",
            "bd": 1,
            "width": 12,
            "justify": "left",
            "font": ("Segoe UI", 9, "bold"),
            "disabledforeground": "black",
            "disabledbackground": "#dddddd",
            "foreground": "black",
            "background": "#dddddd",
            "state": "disabled",
        }
        self.index = {
            "relief": "solid",
            "bd": 1,
            "width": 12,
            "justify": "left",
            "font": ("Segoe UI", 9, "bold"),
            "disabledforeground": "black",
            "disabledbackground": "#dddddd",
            "foreground": "black",
            "background": "#dddddd",
            "state": "disabled",
        }


class PackOptions:
    "Required Style Options for Pack System"

    def __init__(self):
        self.item = {
            "side": "left",
            "expand": 1,
            "fill": "x",
            "padx": 2,
        }
        self.row_frame = {
            "expand": 1,
            "fill": "x",
        }


class GridOptions:
    "Required Style Options for Grid System"

    def __init__(self):
        self.item = {
            "sticky": "nesw",
            "padx": 2,
            "pady": 2,
        }


class ERRORS:
    "## Class Contain Errors and Warning For TkTables"

    @property
    def UnknownGeometrySystem(self):
        "unknown Gemoetry System Name Raised Value Error"
        return ValueError('Unknown Geometry System, please use ["grid" or "pack"]')

    @property
    def NotAvailable(self):
        "Not Available Option Warning for Geometry Systems"
        print(
            "[WARNING](Given index wont be Applied)",
            "Indexing is Only Available for Grid System!",
        )

    @property
    def UnknownWidgetType(self):
        "Unown Widget Type Value Error"
        return ValueError('Unkown Widget Type, plase use ["label" or "entry"]')


def labelcell(master, item, **styles):
    "label cell template"
    tempvar = tkinter.Variable(value=str(item))
    cellbox = tkinter.Label(master, textvariable=tempvar, **styles)
    cellbox.ID = tempvar
    tempvar.master = cellbox

    return cellbox


def entrycell(master, item, **styles):
    "entry cell template"
    tempvar = tkinter.Variable(value=str(item))
    cellbox = tkinter.Entry(master, textvariable=tempvar, **styles)
    cellbox.ID = tempvar
    tempvar.master = cellbox
    return cellbox


def cell(widgettype, master, item, **styles):
    "create cells according to its type ['label', 'entry']"
    if widgettype == "label":
        return labelcell(master, item, **styles)
    elif widgettype == "entry":
        return entrycell(master, item, **styles)
    else:
        raise ERRORS().UnknownWidgetType


def getstyles(widgettype, geometrysystem):
    "Load Default Styles"
    if widgettype == "label":
        style = LabelStyles
    elif widgettype == "entry":
        style = EntryStyles
    if geometrysystem == "grid":
        geometry = GridOptions
    elif geometrysystem == "pack":
        geometry = PackOptions

    return style, geometry
