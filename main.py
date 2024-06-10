from operaçoes import calcular_media, verificar_rep, indetificar_aluno_rep

dados_alunos = {
    '26': {'nome': 'Maria', 'notas': [8, 7, 5, 9]},
    '101': {'nome': 'Ana', 'notas': [9, 9, 8, 9]},
    '13': {'nome': 'João', 'notas': [6, 5, 5, 5]},
    '37': {'nome': 'Agatha', 'notas': [8, 6, 7.5, 9]},
    '72': {'nome': 'Joaquim', 'notas': [6, 5.5, 5, 7]},
    '5': {'nome': 'Félix', 'notas': [10, 8, 8, 8]}
}

for matricula, aluno in dados_alunos.items():
    media = calcular_media(aluno['notas'])
    print(f'Média do aluno {aluno["nome"]}: {media}')

for matricula, aluno in dados_alunos.items():
    media = calcular_media(aluno['notas'])
    if verificar_rep(media):
        print(f'O aluno {aluno["nome"]} foi reprovado.')

matriculas_reprovadas = [matricula for matricula, aluno in dados_alunos.items() if verificar_rep(calcular_media(aluno['notas']))]
indetificar_aluno_rep(dados_alunos, matriculas_reprovadas)



