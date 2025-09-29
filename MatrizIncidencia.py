class MatrizIncidencia:

    def __init__(self, num_vertices, arestas):
        self.num_vertices = num_vertices
        self.arestas = arestas
        self.matriz = []
        self._criar_matriz_incidencia()

    def _criar_matriz_incidencia(self):
    # Normaliza as arestas para evitar duplicatas (ex: (1,3) == (3,1))
        arestas_normalizadas = []
        vistos = set()

        for u, v in self.arestas:
            aresta = tuple(sorted((u, v)))  # garante (menor, maior)
            if aresta not in vistos:
                vistos.add(aresta)
                arestas_normalizadas.append(aresta)

        num_arestas = len(arestas_normalizadas)
        matriz_incidencia = [[0 for _ in range(num_arestas)] for _ in range(self.num_vertices)]

        for j, (u, v) in enumerate(arestas_normalizadas):
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
                
        for g in sorted(freq):
            print(f"Grau {g}: {freq[g]} vértices")
    
    def dirac(self):
        # Teorema de Dirac
        contagens = self._contar_arestas_de_cada_vertice()
        n = self.num_vertices
        if n < 3:
            print("O grafo não possui ciclos Hamiltonianos (menos de 3 vértices).")
            return
        if all(grau >= n / 2 for grau in contagens):
            print("O grafo possui ciclos Hamiltonianos (Teorema de Dirac).")
        else:
            print("O grafo pode não possuir ciclos Hamiltonianos (Teorema de Dirac não satisfeito).")
            
    def ore(self):
        # Teorema de Ore
        contagens = self._contar_arestas_de_cada_vertice()
        n = self.num_vertices
        if n < 3:
            print("O grafo não possui ciclos Hamiltonianos (menos de 3 vértices).")
            return
        
        for i in range(n):
            for j in range(i + 1, n):
                if all(self.matriz[i][k] == 0 or self.matriz[j][k] == 0 for k in range(len(self.matriz[0]))):
                    if contagens[i] + contagens[j] < n:
                        print("O grafo pode não possuir ciclos Hamiltonianos (Teorema de Ore não satisfeito).")
                        return
        print("O grafo possui ciclos Hamiltonianos (Teorema de Ore).")
        
    def bondy(self):
        # Teorema de Bondy-Chvátal
        contagens = self._contar_arestas_de_cada_vertice()
        n = self.num_vertices
        if n < 3:
            print("O grafo não possui ciclos Hamiltonianos (menos de 3 vértices).")
            return
        
        for i in range(n):
            for j in range(i + 1, n):
                if all(self.matriz[i][k] == 0 or self.matriz[j][k] == 0 for k in range(len(self.matriz[0]))):
                    if contagens[i] + contagens[j] < n:
                        print("O grafo pode não possuir ciclos Hamiltonianos (Teorema de Bondy-Chvátal não satisfeito).")
                        return
        print("O grafo possui ciclos Hamiltonianos (Teorema de Bondy-Chvátal).")