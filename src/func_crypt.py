from cryptography.fernet import Fernet
# from model import SysConfig, CONN, Base,engine,session

# Gera uma chave para o Fernet
def generate_key():
    return Fernet.generate_key()


# def get_key():
#     query = session.query(SysConfig).filter_by(id=1).all()
#     for i in query:
#         return i.chart_p    


# Função para encriptar a senha
def encrypt(password, key, salt):
    # Adiciona um valor de sal à senha (aqui você pode fazer o que quiser com o salt)
    salted_password = password + salt
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(salted_password.encode())
    return encrypted_password

# Função para decriptar a senha
def decrypt(encrypted_password, key, salt):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    # Remove o valor de sal
    original_password = decrypted_password.replace(salt, '', 1)
    return original_password

# Exemplo de uso
if __name__ == "__main__":
    # Gera uma chave (você deve armazenar essa chave de forma segura)
    # key = generate_key()
    # print(f" key utilizada : {key}")
    key ='get_key()'
    
   
    # Define a senha e um valor de sal
    password = "minha_senha_segura"
    salt = "06919904179"  # Exemplo de salt
    # Encripta a senha
    encrypted = encrypt(password, key, salt)
    print("Senha encriptada:", encrypted)
    # Decripta a senha
    decrypted = decrypt(encrypted, key, salt)
    print("Senha decriptada:", decrypted)

    