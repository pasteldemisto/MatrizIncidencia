import MatrizIncidencia as MI

dic_vertices = {
    0: "Vértice 0",
    1: "Vértice 1",
    2: "Vértice 2",
    3: "Vértice 3",
    4: "Vértice 4",
    5: "Vértice 5",
    6: "Vértice 6"
}

grafoA = [
    (0, 1), (0, 2), (0, 5), (0, 6),
    (1, 0), (1, 2), (1, 3), (1, 5),
    (2, 0), (2, 1), (2, 3), (2, 4),
    (3, 1), (3, 2), (3, 4), (3, 6),
    (4, 2), (4, 3), (4, 5), (4, 6),
    (5, 0), (5, 1), (5, 4), (5, 6),
    (6, 0), (6, 3), (6, 4), (6, 5)
]

grafoB = [
    (0, 1), (0, 2), (0, 5), (0, 6),
    (1, 0), (1, 2), (1, 3), (1, 5),
    (2, 0), (2, 1), (2, 3),
    (3, 1), (3, 2), (3, 4), (3, 6),
    (4, 3), (4, 5), (4, 6),
    (5, 0), (5, 1), (5, 4), (5, 6),
    (6, 0), (6, 3), (6, 4), (6, 5)
]

grafoC = [
    (0, 1), (0, 2), (0, 5), (0, 6),
    (1, 0), (1, 2),
    (2, 0), (2, 1), (2, 3),
    (3, 2), (3, 4),
    (4, 3), (4, 5), (4, 6),
    (5, 0), (5, 4), (5, 6),
    (6, 0), (6, 4), (6, 5)
]

grafoD = [
    (0, 1), (0, 2), (0, 5), (0, 6),
    (1, 0), (1, 2),
    (2, 0), (2, 1), (2, 3),
    (3, 2), (3, 4),
    (4, 3), (4, 5),
    (5, 0), (5, 4), (5, 6),
    (6, 0), (6, 5)
]

matrizGrafoA = MI.MatrizIncidencia(len(dic_vertices), grafoA)
matrizGrafoB = MI.MatrizIncidencia(len(dic_vertices), grafoB)
matrizGrafoC = MI.MatrizIncidencia(len(dic_vertices), grafoC)
matrizGrafoD = MI.MatrizIncidencia(len(dic_vertices), grafoD)

for grafo in [matrizGrafoA, matrizGrafoB, matrizGrafoC, matrizGrafoD]:
    grafo.apresentar_matriz()
    print()
    grafo.frequencia_graus()
    print()
    grafo.maior_ocorrencia(dic_vertices)
    print()
    grafo.ciclos_Hamiltonianos()
