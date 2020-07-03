# Cheatsheet

## Clustering Coefficient

- Measures the degree to which nodes in a network tendo to 'cluster' or form triangles

- Local clustering coefficient (LCC):
    
    ```    
    Assume a node "i", with degree di > 2
    We calculate the LCC(i) by solving:
        (num of EDGES between neighbors of i) / (di * (di - 1) ) / 2

    Then, it becomes:

    LCCi = 2*n / (d(i) * (d(i)−1))

    ```

    - For nodes of degree < 2, since we can't divide by zero, assume a LCCi of 0

- Global clustering coefficient: Average of LCCs

## Distance

- Path lenght: Number of edges between two nodes

- Distance: Least number of edges between two nodes

- Breadth-first search: Systematic procedure for computing distances from a node to all other nodes in a large network, by 'discovering' nodes in layers. For each leap/edge/iteration/layer, write down the nodes that were  not accounted yet.

- Diameter: Maximum possible distance between two nodes

- Eccentricity: Largest distance between a node and all others

- Radius: Smalles eccentricity of a graph

- Periphery: Set of nodes that have eccentricity equals to the diameter

- Center: Set of nodes which have eccentricity equals to the radius

## Connected Graphs

- An undirected graph is said to be connected when there's a path linking every pair of nodes

- Connected component:

- Subset of the graph, on which:

    - Every node in the subset as a path to every other node
    - No other node (from outside) has a path to any node in the subset

- Strongly connected: If for every pair of nodes (u, v) there's a directed path from u to v and vice-versa

- Weakly connected: If replacing all directed edges with undirected edges produces a connected undirected graph

## Robustness

- The ability to maintain its general structural properties when it faces failures or attacks (e.g.: removal of edges). Maintain it's connectivity, like the world wide web, or flight paths

## Network Centrality

- Identifies the most importante nodes in a network

    - Directed network: degree
    - Undirected network: in-degree and/or out-degree

## Closenesse Centrality

- Nodes that are important, will be close to other nodes

        The "closeness_centrality" method is ALREADY normalized using:

        ( (n-1) / (|G|-1) )
    
        There's no need to do it manually, like in the course!

## 