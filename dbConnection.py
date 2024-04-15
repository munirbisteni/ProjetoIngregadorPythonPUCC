import oracledb
import os
from dotenv import load_dotenv


load_dotenv()
api_user = os.getenv("API_USER")
api_key = os.getenv("API_KEY")
string_connection = os.getenv("STRING_CONNECTION")

class oracleConnection:
    
    def __init__(self) -> None:    
        try:
            self.connection = oracledb.connect(user=api_user, password=api_key, dsn=string_connection)
            self.cursor = self.connection.cursor()
            print("Conexão bem sucedida!")
        except Exception as e:
            print("Erro ao conectar:", e)
    
    def kill(self) -> bool:
        try:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            print("erro ao fechar conexão")


