import os
from dotenv import load_dotenv
import random
import numpy as np


class Criptografia():   
    _matrizChave = np.array([[3.7, 1.9],
                        [-2.4, 0.8]])
    def __init__(self):
        pass
    
    def criptografar(self,mensagem:str) -> str:
        vetorCriptografar = self.converterMensagemParaVetorNumeros(mensagem)
        produtoCriptografado = np.dot(self._matrizChave, vetorCriptografar)
        mensagemCriptografada = ""
        for linha in produtoCriptografado:
            for numero in linha:
                mensagemCriptografada += str(int(round(numero))) + " "
        return mensagemCriptografada

    def decriptografar(self, numerosEmString:str)  -> str:  
        matrizDecriptografia = self.converterNumerosParaVetor(numerosEmString)
        matrizInvertidaChave = matriz_inversa = np.linalg.inv(self._matrizChave)
        produtoDecriptografado = np.dot(matrizInvertidaChave, matrizDecriptografia)
        mensagemDecriptografada = ""
        for linha in produtoDecriptografado:
            for numero in linha:
                mensagemDecriptografada += chr(int(round(numero)))
        return mensagemDecriptografada
    
    def converterNumerosParaVetor(self, numerosEmString:str) -> np.array:
        numeros =  list(map(float, numerosEmString.split()))
        matrizDecriptografia = [[],[]]

        for indice,numero in enumerate(numeros):
            linha = 0
            if indice >= len(numeros)/2:
                linha = 1
            matrizDecriptografia[linha].append(numero)
        return np.array(matrizDecriptografia)
  

    def converterMensagemParaVetorNumeros(self,mensagem:str) -> np.array:
        matrizCriptografia = [[],[]]
        for indice,letra in enumerate(mensagem):
            linha = 0
            if indice >= len(mensagem)/2:
                linha = 1
            matrizCriptografia[linha].append(ord(letra))
        if len(mensagem) % 2 == 1:
            matrizCriptografia[1].append(0)
        return np.array(matrizCriptografia)
    

















#bmarix

# load_dotenv()
# cripto_key = os.getenv("CRIPTO_KEY")
# vetor_criptografia = {}

# class criptografia():
#     def criar_vetor_criptografia(letras):
#         for letra in letras:
#             vetor_criptografia[letra] = random.randint(0, 1000)
#         return vetor_criptografia
    
#     def criptografar_dado(criptografar:str):
#         if criptografar // 2 == 1:
#             criptografar = criptografar + " "
        
#         quebra = len(criptografar)/2     
        
#         vetor_criptografar = [[],[]]
#         for letra,index in len(criptografar):
#             for i in range(0, len(criptografar)):
#                 if letra == vetor_criptografia.keys[0]:
#                         if index >= quebra: 
#                             vetor_criptografar.append(vetor_criptografia.value[0][i])
#                         else:
#                             vetor_criptografar.append(vetor_criptografia.value[1][i])
#         return criptografar
    
#     def decriptografar_dado(criptografado:str):
#         return criptografado    
    
#     def converter_letra_para_numero(frase:str):
#         return frase