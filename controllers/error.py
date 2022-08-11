class ErrorLexico(Exception):
    
    @classmethod
    def __str__(self,a, b):
        print(f'error: {a}, {b}')
