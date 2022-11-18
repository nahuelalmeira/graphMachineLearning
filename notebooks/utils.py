import igraph as ig
import networkx as nx


def get_CI_nx(g: nx.Graph) -> list:
    """
    Compute Collective Influence of each node at length 1.
    """
    ci_values = []
    for i, v in enumerate(g.nodes()):
        nn_influence = sum([g.degree(w) - 1 for w in g.neighbors(v)])
        ci = (g.degree(v) - 1) * nn_influence
        ci_values.append(ci)
    return ci_values

def get_CI_ig(g: ig.Graph()) -> list:
    """
    Compute Collective Influence of each node at length 1.
    """
    ci_values = []
    for v, k in enumerate(g.degree()):
        nn_influence = sum([g.degree()[w] - 1 for w in g.neighbors(v)])
        #print(g.neighborhood(v))
        ci = (k - 1) * nn_influence
        ci_values.append(ci)
    return ci_values
