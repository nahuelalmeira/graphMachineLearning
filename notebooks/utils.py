import networkx as nx

def get_CI_nx(g: nx.Graph):
    """
    Compute Collective Influence of each node at length 1.
    """
    ci_values = []
    for i, v in enumerate(g.nodes()):
        nn_influence = sum([g.degree(w) - 1 for w in g.neighbors(v)])
        ci = (g.degree(v) - 1) * nn_influence
        ci_values.append(ci)
    return ci_values