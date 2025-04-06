import networkx as nx

import matplotlib.pyplot as plt

class BinaryRelationSimulator:
    def __init__(self, elements):
        self.elements = elements
        self.relations = set()
        self.graph = nx.DiGraph()

    def add_relation(self, a, b):
        if a in self.elements and b in self.elements:
            self.relations.add((a, b))
            self.graph.add_edge(a, b)
        else:
            raise ValueError("Elements must belong to the defined set.")

    def is_reflexive(self):
        for e in self.elements:
            if (e, e) not in self.relations:
                return False
        return True

    def is_symmetric(self):
        for a, b in self.relations:
            if (b, a) not in self.relations:
                return False
        return True

    def is_transitive(self):
        for a, b in self.relations:
            for c, d in self.relations:
                if b == c and (a, d) not in self.relations:
                    return False
        return True

    def is_equivalence(self):
        return self.is_reflexive() and self.is_symmetric() and self.is_transitive()

    def is_irreflexive(self):
        for e in self.elements:
            if (e, e) in self.relations:
                return False
        return True

    def is_antisymmetric(self):
        for a, b in self.relations:
            if a != b and (b, a) in self.relations:
                return False
        return True

    def is_partial_order(self):
        return self.is_irreflexive() and self.is_antisymmetric() and self.is_transitive()

    def visualize(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        plt.title("Binary Relation Graph")
        plt.show()

    def connected_components(self):
        undirected_graph = self.graph.to_undirected()
        return list(nx.connected_components(undirected_graph))

    def topological_sort(self):
        if nx.is_directed_acyclic_graph(self.graph):
            return list(nx.topological_sort(self.graph))
        else:
            raise ValueError("Graph is not a Directed Acyclic Graph (DAG).")


# Example usage
if __name__ == "__main__":
    elements = {1, 2, 3, 4}
    simulator = BinaryRelationSimulator(elements)

    simulator.add_relation(1, 2)
    simulator.add_relation(2, 3)
    simulator.add_relation(3, 4)
    simulator.add_relation(1, 1)

    print("Is Reflexive:", simulator.is_reflexive())
    print("Is Symmetric:", simulator.is_symmetric())
    print("Is Transitive:", simulator.is_transitive())
    print("Is Equivalence Relation:", simulator.is_equivalence())
    print("Is Partial Order:", simulator.is_partial_order())

    simulator.visualize()

    print("Connected Components:", simulator.connected_components())
    try:
        print("Topological Sort:", simulator.topological_sort())
    except ValueError as e:
        print(e)