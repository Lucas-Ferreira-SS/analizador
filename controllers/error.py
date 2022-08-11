class ErrorLexico(Exception):
    
    @classmethod
    def __str__(self,a, b):
        print(f'caractere encontrado: {a}\nCaractere esperado: {b}')
