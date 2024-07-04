import copy
from geopy import distance

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        # Creo grafo
        self.grafo = nx.Graph()
        # Creo dizionario per nodi
        self.diz_vertici = {}
        self.costo_max = None
        self.percorso_migliore = []

    def crea_grafo(self, anno, xg):
        self.grafo.clear()
        # Cancello diz o liste se le ho inizializzate se uno schiacca due volte pulsante non ci sono problemi
        self.diz_vertici.clear()
        nodi = DAO.get_vertici()
        for n in nodi:
            self.diz_vertici[n.id] = n
            self.grafo.add_node(n)
        archi = DAO.get_archi(anno, xg)
        for a in archi:
            self.grafo.add_edge(self.diz_vertici[a[0]], self.diz_vertici[a[1]], weight=a[2])

    # Ritorno lunghezza nodi e archi
    def num_nodi(self):
        return len(self.grafo.nodes)

    def num_archi(self):
        return len(self.grafo.edges)

    def get_peso_nodi(self):
        diz = {}
        for v in self.diz_vertici.values():
            somma = 0
            for vicino in self.grafo.neighbors(v):
                somma += self.grafo[v][vicino]["weight"]
            diz[v] = somma
        return diz

    def get_ciclo_max(self):
        pass

    def ricorsione(self, lista_nodi_tutti):
        pass



    # Lo uso nella ricorsione per calcolarmi il costo del ciclo
    def costo_tot(self, lista_nodi_tutti):
        pass

    def get_archi(self, lista):
        pass

    def get_distanza(self, a1, a2):
        pass