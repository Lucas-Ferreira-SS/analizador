from analizador import Analizador
from tokens import Token
from constantes import Constantes
from error import ErrorLexico

class AnalizadorLexico:
    def __init__(self) -> None:
        self.token = Token()
        self.constantes = Constantes()
        self.analizador = Analizador()
        self.tokens_lidos = []
        self.carac_encontrado = ''
        self.carac_esperado = f'{self.constantes.ident}'
    
    def S0(self, exp):
        while exp:
            if self.analizador.verifica_indice(exp[0], self.constantes.num):
                self.S1(exp)

            elif self.analizador.verifica_indice(exp[0], self.constantes.atrib):
                self.S2(exp)

            elif self.analizador.verifica_indice(exp[0], self.constantes.ident):
                self.S3(exp)

            elif self.analizador.verifica_indice(exp[0], self.constantes.abre_col):
                self.S4(exp)

            elif self.analizador.verifica_indice(exp[0], self.constantes.fecha_col):
                self.S5(exp)

            elif self.analizador.verifica_indice(exp[0], self.constantes.abre_cha):
                self.S6(exp)

            elif self.analizador.verifica_indice(exp[0], self.constantes.fecha_cha):
                self.S7(exp)

            elif self.analizador.verifica_indice(exp[0], self.constantes.abre_paren):
                self.S8(exp)

            elif self.analizador.verifica_indice(exp[0], self.constantes.fecha_pare):
                self.S9(exp)

            else:
                self.carac_encontrado = exp[0]
                raise ErrorLexico


    def S1(self, exp):
        if self.analizador.verifica_indice(exp[0], self.constantes.num):
            while exp and self.analizador.verifica_indice(exp[0], self.constantes.num):
                exp.pop(0)
            print(self.token.num)

    def S2(self, exp):
        if self.analizador.verifica_indice(exp[0], self.constantes.atrib):
            exp.pop(0)
        print(self.token.atrib)
    
    def S3(self, exp):
        if self.analizador.verifica_indice(exp[0], self.constantes.ident):
            while exp and self.analizador.verifica_indice(exp[0], self.constantes.ident):
                exp.pop(0)
            print(self.token.ident)

    def S4(self, exp):
        print(self.token.abre_col)
        exp.pop(0)

    def S5(self, exp):
        print(self.token.fecha_col)
        exp.pop(0)

    def S6(self, exp):
        print(self.token.abre_cha)
        exp.pop(0)

    def S7(self, exp):
        print(self.token.fecha_cha)
        exp.pop(0)

    def S8(self, exp):
        print(self.token.abre_paren)
        exp.pop(0)

    def S9(self, exp):
        print(self.token.fecha_pare)
        exp.pop(0)
  
    
    def run(self):
        try:
            for i in self.analizador.expressoes:
                self.S0(list(i.replace(" ", "")))
        except:
            print(f'Erro Lexico: caractere encontrado: {self.carac_encontrado}\nEram esperados: {self.carac_esperado}')
        

if __name__ == '__main__':
    analise = AnalizadorLexico()
    analise.run()