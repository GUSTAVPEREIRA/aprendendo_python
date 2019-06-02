from Funcionario import Alura, Caelum, Funcionario, Hipster


class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass


jose = Junior("José")
jose.busca_perguntas_sem_resposta()

luan = Pleno("Luan")
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()
print(luan)
