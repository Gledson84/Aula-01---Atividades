ganho_por_hora = float(input('Digite quanto ganha por hora: '))
horas_trabalhadas = float(input('Digite quantas horas trabalha: '))
ganho_diario = ganho_por_hora * horas_trabalhadas
ganho_mensal_20dias =  ganho_diario * 20
print(f'Seu ganho mensal em 20 dias é: R$ {ganho_mensal_20dias:.2f}')
