notas = [
    {"bimestre": "1º", "aluno": "Lucas", "nota": 60},
    {"bimestre": "1º", "aluno": "Lucas", "nota": 70},
    {"bimestre": "1º", "aluno": "Paula", "nota": 80},
    {"bimestre": "1º", "aluno": "Rafael", "nota": 50},

    {"bimestre": "2º", "aluno": "Lucas", "nota": 90},
    {"bimestre": "2º", "aluno": "Paula", "nota": 85},
    {"bimestre": "2º", "aluno": "Rafael", "nota": 75},
    {"bimestre": "2º", "aluno": "Marina", "nota": 95},

    {"bimestre": "3º", "aluno": "Lucas", "nota": 70},
    {"bimestre": "3º", "aluno": "Paula", "nota": 60},
    {"bimestre": "3º", "aluno": "Marina", "nota": 80},
]


total_de_notas_por_aluno = {} 
aluno_maior_nota = None 
total_de_notas_por_bimestre = {} 
bimestre_campeao =None 
classificacao = {}


# TOTAL DE NOTAS POR ALUNO

for desempenho in notas:
    aluno = desempenho["aluno"]
    nota = desempenho["nota"]

    if aluno not in total_de_notas_por_aluno:
        total_de_notas_por_aluno[aluno] = 0

    total_de_notas_por_aluno[aluno] +=nota

# ALUNO MAIOR NOTA

maior_nota = 0

for aluno , total in total_de_notas_por_aluno.items():
    if total > maior_nota:
        maior_nota = total
        aluno_maior_nota = aluno 



# TOTAL DE NOTAS POR BIMESTRE
for temporada in notas:
    bimestre = temporada["bimestre"]
    nota = temporada["nota"]

    if bimestre not in total_de_notas_por_bimestre:
        total_de_notas_por_bimestre[bimestre] = 0

    total_de_notas_por_bimestre[bimestre]+=nota


# BIMESTRE CAMPEAO

maior_bimestre = 0

for bimestre , total in total_de_notas_por_bimestre.items():
    if total > maior_bimestre:
        maior_bimestre = total
        total_bimestre = {bimestre:maior_bimestre}
        bimestre_campeao = total_bimestre


for aluno , total in total_de_notas_por_aluno.items():
    if total <= 150:
        classificacao[aluno] = "baixa"

    elif 151 <= total  <=200:
        classificacao[aluno ] = "media"

    else:
        classificacao[aluno] ="excelente"

print(total_de_notas_por_aluno)
print(aluno_maior_nota)
print(total_de_notas_por_bimestre)
print(bimestre_campeao)
print(classificacao)






 






