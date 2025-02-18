#!/usr/bin/env python3
# -*- coding: utf-8 -*

from collections import defaultdict, deque, Counter
from itertools import combinations
from collections import deque
import sys


class Node:
    "Узел в дереве поиска"

    def __init__(self, state, parent=None, action=None, path_cost=0.0):
        self.__dict__.update(state=state, parent=parent, action=action,
                             path_cost=path_cost)

    def __repr__(self): return '<{}>'.format(self.state)

    def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))

    def __lt__(self, other): return self.path_cost < other.path_cost

    def cost_calc(self, matrix):
        return matrix[self.action[len(self.action) - 2]][self.action[len(self.action) - 1]]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.value}>"


def expand(node, max_depth=10 ** 27, finish=5):
    "Раскрываем узел, создав дочерние узлы."
    s = node.state
    last_node = node.action
    # print(last_node)
    # print(tree[int(last_node)])
    if node.path_cost <= max_depth:
        lst_nodes = [n for n in last_node.children if n != None]
        result = []
        for item in lst_nodes:
            temp = s.copy()
            if item not in s:
                temp.append(item)
                dist = node.path_cost + 1
                result.append(Node(temp, node, item, dist))

        return result
    else:
        return []


if __name__ == '__main__':
    # Построение дерева

    root = TreeNode("dir")
    root.add_child(TreeNode("dir2"))
    root.add_child(TreeNode("dir3"))
    root.children[0].add_child(TreeNode("file4"))
    root.children[1].add_child(TreeNode("file5"))
    root.children[1].add_child(TreeNode("file6"))

    start = root.value
    max_depth = 1
    finish = "file5"
    paths = []
    find = False
    while max_depth < sys.maxsize and find != True:
        print(f"Максимальная глубина поиска: {max_depth}")
        first = Node([root], None, root, 0)
        paths = []
        q = deque()
        q.appendleft(first)
        counter = 0
        while q:
            counter += 1
            temp = expand(q.popleft(), max_depth - 1)
            for i in temp:
                if i.action.value != finish:
                    q.appendleft(i)
                    # print(counter, i.state)
                else:
                    paths.append(i)
                    find = True
                    break

        if find == False: print("Цель не найдена")
        max_depth += 1
    if len(paths) == 0:
        print("Цель не найдена")

    else:
        print(f"Цель найдена: {finish}")
        mn = [100000000000000000000, []]
        result = []
        counter = 0
        for i in paths:
            if i.path_cost < mn[0]:
                mn[0] = i.path_cost
                mn[1] = i.state
                # print(i.state,i.path_cost,counter)
                counter += 1

        print(f"Количество возможных путей из вершины {start} в вершину {finish}: {len(paths)}")
        print(f"Длина маршрута: {mn[0]}")
        print(f"Маршрут:")
        for id in mn[1]:
            if id.value != finish:
                print(id.value, end=" --> ")
            else:
                print(id.value)
