from typing import List


class Pessoa:
    __nome :str
    
    def __init__(self, nome : str):
        self.__nome = nome
    def __str__(self):
        return f"Nome: {self.__nome}"
    def get_nome(self):
        return self.__nome
    
class Aluno(Pessoa):
    __RA : int
    tamanho_camisa : str
    
    def __init__(self, nome : str, ra : int, camisa : str):
        super().__init__(nome)
        self.__RA = ra
        self.tamanho_camisa = camisa
        
    def get_ra(self):
        return self.__ra
    
    def __str__(self):
        return f"{super().__str__()}\nRA:{self.__RA}\nCamisa: {self.tamanho_camisa}"
    
class Juiz(Pessoa):
    __email : str
    
    def __init__(self, nome : str, email :str):
        super().__init__(nome)
        self.__email = email
        
    def __str__(self):
        return f"{super().__str__()}\nEmail: {self.__email}"
    
class Time:
    __nome :str
    __alunos : List[Aluno]
    
    def __init__(self, nome : str, alunos : List[Aluno]):
        if len(alunos) != 3:
            raise Exception(f"Equipe {nome} não tem 3 alunos!")
        
        self.__nome = nome
        self.__alunos = alunos
        
    def get_nome(self):
        return self.__nome
    
    def get_alunos(self):
        return self.__alunos
    
    def __str__(self):
        info = f"EQUIPE = {self.__nome}\n"
        for aluno in self.__alunos:
            info += f"{aluno}\n"
        return info
    
class Maratona:
    __ano : int
    times : List[Time]
    juiz : Juiz
    
    def __init__(self, ano : int, time : List[Time], juiz : Juiz):
        self.__ano = ano
        self.__juiz = juiz
        self.__time = []
        
    def add_time(self, t : Time):
        self.times.append(t)
        
    def get_ano(self):
        return self.__ano
    
    def __str__(self):
        info = f"MARATONA ANO {self.__ano}\n"
        for time in self.__time:
            info += f"{time}\n"
        return info
    