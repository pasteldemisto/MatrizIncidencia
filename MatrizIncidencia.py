class MatrizIncidencia:

    def __init__(self, num_vertices, arestas):
        self.num_vertices = num_vertices
        self.arestas = arestas
        self.matriz = []

    def criar_matriz_incidencia(self):
        num_arestas = len(self.arestas)
        matriz_incidencia = [[0 for _ in range(num_arestas)] for _ in range(self.num_vertices)]

        for j, aresta in enumerate(self.arestas):
            u, v = aresta
            matriz_incidencia[u][j] = 1
            matriz_incidencia[v][j] = 1

        self.matriz = matriz_incidencia
    
    def apresentar_matriz(self):
        for linha in self.matriz:
            print(linha)

    def _contar_arestas_de_cada_vertice(self):
        return [sum(linha) for linha in self.matriz]
    
    def _vizinhanca(self, v):
        vizinhos = []
        for j, val in enumerate(self.matriz[v]):
            if val == 1:
                for u in range(self.num_vertices):
                    if u != v and self.matriz[u][j] == 1:
                        vizinhos.append(u)
        return sorted(set(vizinhos))

    def maior_ocorrencia(self, dicionario):
        contagens = self._contar_arestas_de_cada_vertice()
        maior = max(contagens)
        vertices = [i for i, c in enumerate(contagens) if c == maior]

        for v in vertices:
            fronteiras = self._vizinhanca(v)
            print(f"(Grau Máximo) Vértice {dicionario[v]} tem {maior} arestas: ")
            for chave in fronteiras:
                print("- " + dicionario[chave])


    def menor_ocorrencia(self, dicionario):
        contagens = self._contar_arestas_de_cada_vertice()
        menor = min(contagens)
        vertices = [i for i, c in enumerate(contagens) if c == menor]

        for v in vertices:
            fronteiras = self._vizinhanca(v)
            print(f"(Grau Mínimo) Vértice {dicionario[v]} tem {menor} arestas: ")
            for chave in fronteiras:
                print("- " + dicionario[chave])
                
    def frequencia_graus(self):
        contagens = self._contar_arestas_de_cada_vertice()
        freq = {}
        for grau in contagens:
            if grau in freq:
                freq[grau] += 1
            else:
                freq[grau] = 1
                
        print(freq)
        return freq