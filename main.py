
import networkx as nx
import pandas as pd

from pyvis.network import Network

SHOW_LABEL = False

if __name__ == "__main__":

    G = nx.Graph()

    df = pd.read_excel("input.xlsx")

    df["Dev Name"] = df["Dev Name"].astype(str)
    df["Neighbor Name"] = df["Neighbor Name"].astype(str)
    df["Local Int"] = df["Local Int"].astype(str)

    G = nx.from_pandas_edgelist(df, source="Dev Name", target="Neighbor Name", edge_attr="label")

    net = Network(width=1000,height=1000)

    net.from_nx(G)

    for edge in net.edges:

        if SHOW_LABEL:
            edge.update({"title":edge["label"]})
        else:
            edge.update({"title": edge["label"]})
            edge.pop('label',None)

    net.save_graph("output.html")