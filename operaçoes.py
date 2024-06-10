def calcular_media (notas):
    return sum(notas)/len(notas)

def verificar_rep(media):
    return media<6
def indetificar_aluno_rep(dados_alunos,matriculas_reprovadas):
     for matricula in matriculas_reprovadas:
        aluno = dados_alunos.get(matricula)
        if aluno:
            media_final = calcular_media(aluno['notas'])
            print(f'Aluno Reprovado: {aluno["nome"]} - Matrícula: {matricula} - Média Final: {media_final}')

