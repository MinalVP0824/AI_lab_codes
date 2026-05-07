#--TSP----
import matplotlib.pyplot as plt
import networkx as nx

def get_nearest_neighbor(cost):
  num_nodes=len(cost)
  path=[0]
  current=0
  path_cost=0
  visited=[False]*num_nodes
  visited[0]=True
  for _ in range(num_nodes-1):
    next_node=min((j for j in range(num_nodes)if not visited[j]) ,key=lambda j:cost[current][j])
    path.append(next_node)
    path_cost+=cost[current][next_node]
    visited[next_node]=True
    current=next_node
  path_cost+=cost[current][0]
  path.append(0)
  return path_cost,path

def visualize_graph(cost,path):
  G=nx.DiGraph()
  num_nodes=len(cost)
  for i in range(num_nodes):
    for j in range(i+1,num_nodes):
      G.add_edge(i,j,weight=cost[i][j])
  pos=nx.circular_layout(range(num_nodes))
  edge_list=list(zip(path,path[1:])) if path else []
  plt.figure(figsize=(8,6))
  nx.draw(G,pos,with_labels=True,node_color='lightblue',node_size=2000,font_size=15,font_weight='bold')
  nx.draw_networkx_edges(G,pos,edgelist=edge_list,edge_color='red',width=3)
  plt.title("Travelling Salesman Problem")
  plt.show()

cost = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

res_cost,res_path=get_nearest_neighbor(cost)
print("the path cost is:",res_cost)
print("the path is:")
print(*res_path,sep="->")
visualize_graph(cost,res_path)

