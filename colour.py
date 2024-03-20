class Colour():
    def __init__(self):
        self.BLACK = "\033[30m"
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.YELLOW = "\033[33m"
        self.BLUE = "\033[34m"
        self.PURPLE = "\033[35m"
        self.CYAN = "\033[36m"
        self.WHITE = "\033[37m"

        self.BOLDON = "\033[1m"
        self.BOLDOFF = "\033[22m"

        self.ITALON = "\033[3m"
        self.ITALOFF = "\033[23m"

        self.UNDERON = "\033[4m"
        self.UNDEROFF = "\033[24m"

        self.INVERTON = "\033[7m"
        self.INVERTOFF = "\033[27m"

        self.RESET = "\033[0m"

    def get_colour(self, colour):
        match colour:
            case "black":
                return self.BLACK
            case "green":
                return self.GREEN
            case "yellow":
                return self.YELLOW
            case "red":
                return self.RED
            case "blue":
                return self.BLUE
            case "purple":
                return self.PURPLE
            case "cyan":
                return self.CYAN
            case "white":
                return self.WHITE
            case _:
                return self.WHITE

    def col_print(self, text:str, colour:str, bold=False, italics=False, underline=False, reset=True):
        c_start = ""
        c_end = ""
        if bold:
            c_start += self.BOLDON
            c_end += self.BOLDOFF
        if italics:
            c_start += self.ITALON
            c_end += self.ITALOFF
        if underline:
            c_start += self.UNDERON
            c_end += self.UNDEROFF
        if reset:
            c_end += self.RESET
        c_start += self.get_colour(colour.lower())

        print(f"{c_start}{text}{c_end}")
    
    def string(self, text, colour, bold=False, italics=False, underline=False, reset=True):
        c_start = ""
        c_end = ""
        if bold:
            c_start += self.BOLDON
            c_end += self.BOLDOFF
        if italics:
            c_start += self.ITALON
            c_end += self.ITALOFF
        if underline:
            c_start += self.UNDERON
            c_end += self.UNDEROFF
        if reset:
            c_end += self.RESET
        text_col = self.get_colour(colour.lower())
        c_start += text_col if text_col != None else self.WHITE
        return f"{c_start}{text}{c_end}"