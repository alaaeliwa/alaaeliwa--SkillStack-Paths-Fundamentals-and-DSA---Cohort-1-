import heapq
from collections import deque

class CityMap:
    def __init__(self):
        self.graph = {}  # {location: {neighbor: travel_time}}

    def add_location(self, name):
        if name not in self.graph:
            self.graph[name] = {}

    def remove_location(self, name):
        if name in self.graph:
            self.graph.pop(name)
            for loc in self.graph:
                self.graph[loc].pop(name, None)

    def add_road(self, from_loc, to_loc, time):
        if from_loc in self.graph and to_loc in self.graph:
            self.graph[from_loc][to_loc] = time

    def remove_road(self, from_loc, to_loc):
        if from_loc in self.graph and to_loc in self.graph[from_loc]:
            del self.graph[from_loc][to_loc]

    def shortest_path(self, start, target):
        """Dijkstra's Algorithm"""
        distances = {loc: float('inf') for loc in self.graph}
        distances[start] = 0
        pq = [(0, start)]  # (distance, location)
        previous = {loc: None for loc in self.graph}

        while pq:
            current_dist, current_loc = heapq.heappop(pq)
            if current_dist > distances[current_loc]:
                continue
            for neighbor, weight in self.graph[current_loc].items():
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_loc
                    heapq.heappush(pq, (distance, neighbor))

        # استعادة المسار
        path = []
        loc = target
        while loc is not None:
            path.append(loc)
            loc = previous[loc]
        path.reverse()

        return distances[target], path

    def reachable_locations(self, start):
        """BFS Traversal"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        reachable = []

        while queue:
            loc = queue.popleft()
            reachable.append(loc)
            for neighbor in self.graph[loc]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return reachable


# ==== تجربة الكود ====
city = CityMap()

# إضافة مواقع
for location in ["Hospital", "School", "Store", "Park", "Library", "Mall"]:
    city.add_location(location)

# إضافة طرق (من → إلى ، الوقت)
roads = [
    ("Hospital", "School", 5),
    ("Hospital", "Store", 10),
    ("School", "Park", 3),
    ("School", "Library", 7),
    ("Store", "Mall", 2),
    ("Mall", "Library", 1),
    ("Park", "Mall", 6),
    ("Library", "Hospital", 8),
    ("Library", "Store", 4),
    ("Park", "Hospital", 9)
]

for frm, to, t in roads:
    city.add_road(frm, to, t)

# أقصر مسار من Hospital إلى Mall
dist, path = city.shortest_path("Hospital", "Mall")
print(f"Shortest path from Hospital to Mall: {path} (Time: {dist})")

# جميع المواقع الممكن الوصول لها من School
reachable = city.reachable_locations("School")
print("Reachable from School:", reachable)
