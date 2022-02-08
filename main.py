from random import randint
from time import time

adj_list = {}  # список смежности
color = []  # цвет вершины
ans = []  # ответ


def DFS(vertex):  # поиск в глубину, возвращающий True, если граф имеет цикл
    color[vertex] = 1
    for next_vertex in adj_list[vertex]:
        if color[next_vertex] == 0:
            if DFS(next_vertex):
                return True
        elif color[next_vertex] == 1:
            adj_list[vertex].remove(next_vertex)
            return True
    ans.append(vertex)
    color[vertex] = 2
    return False


def TopologicalSort(n):  # топологическая сортировка
    ans.clear()
    for vertex in range(1, n + 1):
        if color[vertex] == 0:
            cyclic = DFS(vertex)
            if cyclic:
                return 'Graph is not acyclic'
    ans.reverse()
    return ans


def Random_DAG(n):  # генерация входных данных
    global adj_list
    adj_list = {v: [] for v in range(1, n + 1)}
    for edge in range(n):
        adj_list[randint(1, n)].append(randint(1, n))
    cyclic = True
    while cyclic:
        cyclic = False
        global color
        color = [0 for i in range(n + 1)]
        for vertex in range(1, n + 1):
            if color[vertex] == 0 and not cyclic:
                cyclic = DFS(vertex)
    return adj_list


def main():
    res = []
    i = 0
    for edges in range(100, 5000, 100):
        res.append([edges, 0])
        for n in range(1000):
            min_ver = int((1 + (1 + 8 * edges) ** 0.5) / 2) + 1  # minimum number of vertices
            max_ver = 2 * edges  # maximum number of vertices
            ver = randint(min_ver, max_ver)
            Random_DAG(ver)
            global color
            color = [0 for i in range(ver + 1)]
            start = time()
            TopologicalSort(ver)
            res[i][1] += time() - start
        res[i][1] /= 1000
        i += 1
    print(res)


if __name__ == '__main__':
    main()
