class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_str = ""
        for node, neighbors in self.adj_list.items():
            graph_str += f"{node} -> {neighbors}\n"
        return graph_str

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")

    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError("Node doesn't exist")
        for neighbors in self.adj_list.values():
            neighbors.discard(node)
        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)
        # Weighted or unweighted
        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def remove_edge(self, from_node, to_node):
        if from_node not in self.adj_list or to_node not in self.adj_list:
            raise ValueError("One or both nodes do not exist")
        # Remove weighted and unweighted edges
        neighbors = self.adj_list[from_node]
        found = False
        for edge in list(neighbors):
            if edge == to_node or (isinstance(edge, tuple) and edge[0] == to_node):
                neighbors.remove(edge)
                found = True
        if not found:
            raise ValueError("Edge doesn't exist")
        if not self.directed:
            neighbors = self.adj_list[to_node]
            for edge in list(neighbors):
                if edge == from_node or (isinstance(edge, tuple) and edge[0] == from_node):
                    neighbors.remove(edge)

    def get_neighbors(self, node):
        return self.adj_list.get(node, set())

    def has_node(self, node):
        return node in self.adj_list

    def has_edge(self, from_node, to_node):
        for edge in self.adj_list.get(from_node, []):
            if edge == to_node or (isinstance(edge, tuple) and edge[0] == to_node):
                return True
        return False

    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adj_list.items():
            for to_node in neighbors:
                edges.append((from_node, to_node))
        return edges

    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    # Handle weighted edge case
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                node_neighbors = []
                for neighbor in neighbors:
                    node_name = neighbor[0] if isinstance(neighbor, tuple) else neighbor
                    node_neighbors.append(node_name)
                for neighbor in sorted(node_neighbors, reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order



if __name__ == "__main__":
    # Create undirected graph
    G = Graph()
    G.add_edge('A', 'B')
    G.add_edge('A', 'C')
    G.add_edge('B', 'D')
    G.add_edge('C', 'D')
    G.add_edge('C', 'E', weight=3)
    G.add_edge('E', 'F', weight=2)
    print("Graph adjacency list:\n", G)

    print("Nodes:", G.get_nodes())
    print("Edges:", G.get_edges())

    print("Neighbors of C:", G.get_neighbors('C'))

    print("BFS from 'A':", G.bfs('A'))
    print("DFS from 'A':", G.dfs('A'))

    print("Does edge C→E exist?", G.has_edge('C', 'E'))
    print("Does node 'F' exist?", G.has_node('F'))
    G.remove_edge('C', 'E')
    print("After removing edge C→E, neighbors of C:", G.get_neighbors('C'))
    G.remove_node('F')
    print("After removing node 'F', nodes:", G.get_nodes())
