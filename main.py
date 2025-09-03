import MatrizIncidencia as MI

estados_brasil = {
    0: "Acre (AC)",
    1: "Alagoas (AL)",
    2: "Amapá (AP)",
    3: "Amazonas (AM)",
    4: "Bahia (BA)",
    5: "Ceará (CE)",
    6: "Distrito Federal (DF)",
    7: "Espírito Santo (ES)",
    8: "Goiás (GO)",
    9: "Maranhão (MA)",
    10: "Mato Grosso (MT)",
    11: "Mato Grosso do Sul (MS)",
    12: "Minas Gerais (MG)",
    13: "Pará (PA)",
    14: "Paraíba (PB)",
    15: "Paraná (PR)",
    16: "Pernambuco (PE)",
    17: "Piauí (PI)",
    18: "Rio de Janeiro (RJ)",
    19: "Rio Grande do Norte (RN)",
    20: "Rio Grande do Sul (RS)",
    21: "Rondônia (RO)",
    22: "Roraima (RR)",
    23: "Santa Catarina (SC)",
    24: "São Paulo (SP)",
    25: "Sergipe (SE)",
    26: "Tocantins (TO)"
}
arestas = [
    (0, 3), (0, 21),
    (1, 4), (1, 16), (1, 25),
    (2, 13),
    (3, 10), (3, 13), (3, 21), (3, 22),
    (4, 7), (4, 8), (4, 12), (4, 16), (4, 17), (4, 25), (4, 26),
    (5, 14), (5, 16), (5, 17), (5, 19),
    (6, 8), (6, 12),
    (7, 12), (7, 18),
    (8, 10), (8, 11), (8, 12), (8, 26),
    (9, 13), (9, 17), (9, 26),
    (10, 11), (10, 13), (10, 21), (10, 26),
    (11, 12), (11, 15), (11, 24),
    (12, 18), (12, 24),
    (13, 22), (13, 26),
    (14, 16), (14, 19),
    (15, 23), (15, 24),
    (16, 17),
    (18, 24),
    (20, 23),
    (23, 24),
    (25, 26)
]

matrizIncidencia = MI.MatrizIncidencia(len(estados_brasil), arestas)
matrizIncidencia.criar_matriz_incidencia()
# matrizIncidencia.apresentar_matriz()
matrizIncidencia.maior_ocorrencia(estados_brasil)
matrizIncidencia.menor_ocorrencia(estados_brasil)