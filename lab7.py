import csv
import os


class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False


def get_minimum_cable_length(file_path: str) -> int:
    if not os.path.exists(file_path):
        return -1

    edges = []
    vertices = set()

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 3:
                    continue
                u, v = row[0].strip(), row[1].strip()
                weight = int(row[2].strip())
                edges.append((weight, u, v))
                vertices.add(u)
                vertices.add(v)
    except Exception:
        return -1

    if not vertices:
        return 0

    dsu = DSU(vertices)
    edges.sort()

    mst_weight = 0
    edges_used = 0

    for weight, u, v in edges:
        if dsu.union(u, v):
            mst_weight += weight
            edges_used += 1

    if edges_used == len(vertices) - 1:
        return mst_weight
    else:
        return -1
