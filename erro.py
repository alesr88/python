from models import *
    arquivo = None
try:
    valores = arquivo.readline().split(':')
    Perfil(*valores)
    print('arquivo foi aberto')
    arquivo.close()
except IOError as erro:
    prin('Deu IOErros %s' % erro)
except TypeError as erro:
    print('Deu TypeError %s' % erro)
finally:
    if(arquivo is not None):
        print('fechando arquivo')
        arquivo.close()