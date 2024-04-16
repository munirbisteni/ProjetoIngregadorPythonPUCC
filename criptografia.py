import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

class criptografia():
    def criptografar_dado(criptografar:str):
        return criptografar
    
    def decriptografar_dado(criptografado:str):
        return criptografado    