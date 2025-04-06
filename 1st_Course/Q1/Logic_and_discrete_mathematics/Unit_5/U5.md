## **Unit 5: Graphs**

A **graph** is a fundamental data structure in mathematics and computer science used to model relationships between objects. A graph consists of vertices (also called nodes) and edges (also called arcs) that connect pairs of vertices. Graphs are used to represent networks, relationships, and various structures in fields such as computer science, social networks, biology, transportation systems, and more. This unit explores the basic concepts of graphs, their types, representations, and key algorithms associated with them.

---

### 📌 **1. Introduction to Graphs**

A **graph** is a collection of vertices (or nodes) and edges (or arcs) that connect pairs of vertices. More formally, a graph `G` is defined as:

```plaintext
G = (V, E)
```

where:

- `V` is the set of vertices (or nodes).
- `E` is the set of edges, where each edge is an unordered or ordered pair (depending on whether the graph is undirected or directed) of vertices.

### 1.1 **Types of Graphs**

- **Undirected Graph**: An undirected graph is a graph in which the edges do not have a direction. The edge `(u, v)` is the same as the edge `(v, u)`, meaning that if there is an edge between two vertices `u` and `v`, the relationship is bidirectional.
    
    **Example**: A graph representing friendships, where if person A is friends with person B, then person B is also friends with person A.
    
- **Directed Graph (Digraph)**: A directed graph has edges with a direction, meaning an edge from vertex `u` to vertex `v` is different from an edge from vertex `v` to vertex `u`. Each edge is represented as an ordered pair `(u, v)`.
    
    **Example**: A graph representing web pages and hyperlinks, where a link from page A to page B is not necessarily reciprocated.
    
- **Weighted Graph**: In a weighted graph, each edge has a weight or cost associated with it, representing a value such as distance, time, or cost. The weight is typically a numerical value.
    
    **Example**: A graph representing a road network, where the edges represent roads and the weights represent the distance or travel time between cities.
    
- **Unweighted Graph**: In an unweighted graph, all edges are equal, meaning there is no specific weight or cost associated with the edges.

---

### 📌 **2. Graph Representation**

Graphs can be represented in several ways. The choice of representation depends on the graph’s characteristics and the type of algorithms used to process the graph.

### 2.1 **Adjacency Matrix**

An **adjacency matrix** is a square matrix used to represent a graph, where each element `A[i][j]` represents the presence (or absence) of an edge between vertex `i` and vertex `j`.

- In an **undirected graph**, the adjacency matrix is symmetric (i.e., `A[i][j] = A[j][i]`).
- In a **directed graph**, the matrix may not be symmetric.
- For a **weighted graph**, the matrix elements represent the weights of the edges. If there is no edge, the element may be set to infinity or a specific value indicating no connection.

**Example**: For a graph with vertices `A, B, C` and edges `(A, B)`, `(B, C)`, the adjacency matrix might look like this:

```plaintext
    A B C
A [ 0 1 0 ]
B [ 1 0 1 ]
C [ 0 1 0 ]
```

### 2.2 **Adjacency List**

An **adjacency list** is a collection of lists or arrays, where each list corresponds to a vertex in the graph and contains all the vertices that are adjacent to it. This representation is more space-efficient than an adjacency matrix for sparse graphs (graphs with fewer edges).

- In an **undirected graph**, each edge is represented twice (once for each vertex it connects).
- In a **directed graph**, each edge is represented once from the source vertex to the destination vertex.
- For **weighted graphs**, each list item can store the destination vertex and the weight of the edge.

**Example**: For a graph with vertices `A, B, C` and edges `(A, B)`, `(B, C)`, the adjacency list might look like this:

```plaintext
A: {B}
B: {A, C}
C: {B}
```

---

### 📌 **3. Basic Graph Terminology**

Understanding the terminology of graphs is crucial for graph theory and its algorithms.

- **Vertex (Node)**: The fundamental unit of a graph, representing an object or entity.
- **Edge (Arc)**: The connection between two vertices in the graph.
- **Degree of a Vertex**: The degree of a vertex is the number of edges connected to it. In an undirected graph, it is the number of edges incident to the vertex. In a directed graph, the degree is divided into:
    - **Indegree**: The number of incoming edges to the vertex.
    - **Outdegree**: The number of outgoing edges from the vertex.
- **Path**: A sequence of edges that connect a sequence of vertices. A **simple path** is one where no vertex is repeated.
- **Cycle**: A path that starts and ends at the same vertex, with no other repeated vertices or edges.
- **Connected Graph**: A graph is connected if there is a path between every pair of vertices.
- **Disconnected Graph**: A graph is disconnected if there is at least one pair of vertices with no path between them.

---

### 📌 **4. Graph Traversal Algorithms**

Graph traversal refers to the process of visiting all vertices and edges in a graph in a systematic manner. The two most common traversal algorithms are **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**.

### 4.1 **Depth-First Search (DFS)**

- **Description**: DFS explores as far as possible along each branch before backtracking. It starts at a source vertex and explores the deepest vertices first, using a stack data structure (or recursion).
- **Applications**: DFS is used in tasks such as topological sorting, solving mazes, and detecting cycles in a graph.
- **Algorithm**:
    1. Start from the source vertex and mark it as visited.
    2. Recursively visit all unvisited adjacent vertices.
    3. Backtrack when all adjacent vertices have been visited.

### 4.2 **Breadth-First Search (BFS)**

- **Description**: BFS explores all vertices at the present depth level before moving on to vertices at the next depth level. It uses a queue data structure to keep track of vertices to visit.
- **Applications**: BFS is used for finding the shortest path in unweighted graphs, checking graph connectivity, and exploring social networks.
- **Algorithm**:
    1. Start from the source vertex and mark it as visited.
    2. Use a queue to explore all adjacent vertices.
    3. Continue the process for each unvisited vertex.

---

### 📌 **5. Shortest Path Algorithms**

One of the most important problems in graph theory is finding the shortest path between vertices. Several algorithms have been developed for this purpose.

### 5.1 **Dijkstra’s Algorithm**

Dijkstra’s algorithm is used to find the shortest path from a source vertex to all other vertices in a **weighted graph** with non-negative edge weights.

- **Algorithm**:
    1. Assign a tentative distance value to every vertex: 0 for the initial vertex and infinity for all other vertices.
    2. Set the initial vertex as current. For each unvisited neighbor of the current vertex, calculate its tentative distance and update it if smaller.
    3. Mark the current vertex as visited. Select the unvisited vertex with the smallest tentative distance as the new current vertex, and repeat the process.

### 5.2 **Bellman-Ford Algorithm**

The Bellman-Ford algorithm is similar to Dijkstra's algorithm but can handle **negative weight edges**. It works by repeatedly relaxing edges and updating the shortest path estimate.

---

### 📌 **6. Graph Algorithms: Advanced Topics**

- **Minimum Spanning Tree (MST)**: An MST of a weighted graph is a tree that connects all the vertices together with the minimum possible total edge weight. Two common algorithms for finding the MST are **Kruskal’s algorithm** and **Prim’s algorithm**.
- **Topological Sorting**: Topological sorting is used in directed acyclic graphs (DAGs). It arranges the vertices in a linear order such that for every directed edge `(u, v)`, vertex `u` comes before vertex `v`.
- **Graph Coloring**: Graph coloring is the process of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color. This is used in scheduling problems, register allocation in compilers, and map coloring.

---

### 📌 **7. Applications of Graphs**

Graphs have widespread applications in various fields:

- **Computer Networks**: Representing the topology of networks and finding the shortest path for data transmission.
- **Social Networks**: Modeling relationships between users, friendships, and interactions.
- **Web Graphs**: Representing the structure of the World Wide Web, where web pages are vertices and hyperlinks are edges.
- **Transportation**: Modeling road networks, flight paths, and transportation systems for route planning.
- **Biology**: Representing biological networks such as protein-protein interaction networks or genetic networks.