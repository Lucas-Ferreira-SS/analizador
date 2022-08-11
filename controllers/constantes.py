class Constantes:
    def __init__(self) -> None:
        self.num = '0123456789'
        self.atrib = ['-', '+', '/', '*']
        self.abre_paren = '('
        self.fecha_pare = ')'
        self.abre_col = '['
        self.fecha_coL = ']'
        self.abre_cha = '{'
        self.fecha_cha = '}'
        self.ident = 'abcdefghijklmnopqrstuvwxyz'+self.num
        self.EOF = 'EOF'