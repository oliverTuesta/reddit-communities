import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community

# In case is loaded from a local file
path_to_dataset = './soc-redditHyperlinks-title-5000.tsv'
# In case is loaded from a remote file
# path_to_dataset = 'https://raw.githubusercontent.com/oliverTuesta/reddit-communities/main/soc-redditHyperlinks-title-5000.tsv'

data = pd.read_csv(path_to_dataset, delimiter='\t')
# Display the first few rows of the dataset
data.head()

# Create a directed graph from the dataset
G = nx.from_pandas_edgelist(data, source='SOURCE_SUBREDDIT', target='TARGET_SUBREDDIT', edge_attr=True, create_using=nx.DiGraph())

# Basic analysis
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

# Community detection using the Louvain method for directed graph
partition = community.best_partition(G.to_undirected())

# Add the community as a node attribute
nx.set_node_attributes(G, partition, 'community')

# Create a new graph with the community information
G_comm = G.subgraph(partition.keys())

# Basic analysis
print(f"Number of nodes: {G_comm.number_of_nodes()}")
print(f"Number of edges: {G_comm.number_of_edges()}")
print(f"Number of communities: {len(set(partition.values()))}")

# show the communities
for com in set(partition.values()):
    print(f"Community {com}")
    members = list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
    print(members)
    print()
