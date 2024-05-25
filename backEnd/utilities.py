class Utilities:
    @staticmethod
    def verificarPreenchido(dados):
        for item in dados.values():
            if str(item).strip() == "":
                return False
        return True
 