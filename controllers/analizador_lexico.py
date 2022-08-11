from ast import expr
from analizador import Analizador
from tokens import Token
from constantes import Constantes
from error import ErrorLexico

class AnalizadorLexico:
    def __init__(self) -> None:
        self.token = Token()
        self.constantes = Constantes()
        self.analizador = Analizador()
    
    
    def S0(self):
        if self.analizador.verifica_indice(self.constantes.num):
            self.analizador.le_proximo_caractere()
            self.S1()

        elif self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S2()
    
        elif self.analizador.verifica_indice(self.constantes.ident):
            self.analizador.le_proximo_caractere()
            self.S3()

        elif self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S4()

        elif self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S5()

        elif self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S6()

        elif self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S7()

        elif self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S8()

        elif self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S9()

        elif self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S10()

        elif self.analizador.verifica_indice(self.constantes.EOF):
            exit()

        else:
            raise ErrorLexico

    def S1(self):
        print(self.token.num)
        if self.analizador.verifica_indice(self.constantes.num):
            self.analizador.le_proximo_caractere()
            self.S1()
    
    def S2(self):
        print(self.token.atrib)
        if self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S2()
    
    def S3(self):
        print(self.token.ident)
        if self.analizador.verifica_indice(self.constantes.ident):
            self.analizador.le_proximo_caractere()
            self.S3()

    def S4(self):
        print(self.token.atrib)
        if self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S4()

    def S5(self):
        print(self.token.atrib)
        if self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S5()

    def S6(self):
        print(self.token.atrib)
        if self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S6()

    def S7(self):
        print(self.token.atrib)
        if self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S7()

    def S8(self):
        print(self.token.atrib)
        if self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S8()

    def S9(self):
        print(self.token.atrib)
        if self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S9()

    def S10(self):
        print(self.token.atrib)
        if self.analizador.verifica_indice(self.constantes.atrib):
            self.analizador.le_proximo_caractere()
            self.S10()

    def run(self):
        try:
            for i in self.analizador.expressoes:
                self.S0()
                if self.analizador.prox_caractere == 'EOF':
                    break

        except ErrorLexico:
            ErrorLexico.__str__(self.analizador.prox_caractere, self.analizador.prox_caractere)

if __name__ == '__main__':
    analise = AnalizadorLexico()
    analise.run()