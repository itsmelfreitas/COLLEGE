from maratona import *

if __name__ == "__main__":
    p = Pessoa("Drake")
    print(p)
    
    a = Aluno("Kendrick, 13, P")
    print(a)
    
    j = Juiz("Cole, jcole@gmail.com")
    print(j)
    
    a1 = Aluno("Mel", 5, "PP")
    a2 = Aluno("Livy", 8, "PP")
    a3 = Aluno("Aline", 10, "PP")
    
    alunos = [a1,a2,a3]
    try:
        time = Time("LAMAR!", alunos print(time))
    except Exception as e:
        print(e)
    
