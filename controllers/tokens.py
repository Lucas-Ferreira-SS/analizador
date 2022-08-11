class Token:
    def __init__(self) -> None:
        self.num = '<NUM>'
        self.atrib = '<ATRIB>'
        self.abre_paren = '<ABRE_PAREN>'
        self.fecha_pare = '<FECHA_PAREN>'
        self.abre_col = '<FECHA_COL>'
        self.fecha_col = '<FECHA_COL>'
        self.abre_cha = '<ABRE_CHA>'
        self.fecha_cha = '<FECHA_CHA>'
        self.ident = '<IDENT>'
        self.EOF = 'EOF'