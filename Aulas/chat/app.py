import modulos.banco as banco
import threading

if __name__ == "__main__":
    db =  banco.BancoMongo()
    user = input("Nickname: ")
    try:
        f = threading.Thread(target=db.visualizar)
        f.start()
    except Exception as e:
        print('falha ao criar thread {}'.format(e))
    while f.is_alive:
        mens = input()
        db.cadastrar(user, mens)