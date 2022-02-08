#    Copyright 2019 Atikur Rahman Chitholian
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from collections import deque

class Graph_dfs:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, True)

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def depth_first_search(self, start, setOfGoal):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current in setOfGoal:
                found = True
                goal = current;
                break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); fringe.append(node); came_from[node] = current
            print(', '.join(fringe))
        if found:
            print(); return came_from, current
        else:
            print('No path from {} to {}'.format(start, goal))

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph_dfs.print_path(came_from, parent)
        else:
            print(goal, end='');return
        print(' =>', goal, end='')

    def __str__(self):
        return str(self.edges)


# graph = Graph_dfs(directed=True)
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'S')
# graph.add_edge('S', 'G')
# graph.add_edge('S', 'C')
# graph.add_edge('C', 'F')
# graph.add_edge('G', 'F')
# graph.add_edge('C', 'D')
# graph.add_edge('C', 'E')
# graph.add_edge('E', 'H')
# graph.add_edge('G', 'H')
# start = 'A'
# setOfGoals = {"F", "B"}
# traced_path, goal = graph.deapth_first_search(start, setOfGoals)
# if (traced_path): print('Path:', end=' '); Graph_dfs.print_path(traced_path, goal);print()