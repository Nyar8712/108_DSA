from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
        
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    def BFS(self, s): 
        queue, ans = [], []
        queue.append(s)
        while queue:
            dequeue = queue.pop(0)
            if dequeue not in ans:
                ans.append(dequeue)
                unvisited = self.graph[dequeue]
                for i in unvisited:
                    queue.append(i)
        return ans
    
    def DFS(self, s):
        stack, ans= [], []
        stack.append(s) 
        while stack:
            pop_out = stack.pop(-1)
            if pop_out not in ans:
                ans.append(pop_out)
                unvisited = self.graph[pop_out]
                for i in unvisited:
                    stack.append(i)
        return ans

'''
a = Graph()
a.addEdge(1,5)
a.addEdge(2,4)
a.addEdge(3,9)
a.addEdge(3,10)
a.addEdge(4,2)
a.addEdge(4,5)
a.addEdge(4,7)
a.addEdge(5,4)
a.addEdge(6,7)
a.addEdge(6,5)
a.addEdge(6,1)
a.addEdge(6,3)
a.addEdge(7,12)
a.addEdge(7,4)
a.addEdge(8,9)
a.addEdge(9,8)
a.addEdge(10,8)
a.addEdge(10,3)
a.addEdge(11,5)
a.addEdge(11,2)
a.addEdge(11,8)
a.addEdge(12,1)
a.addEdge(12,11)
a.addEdge(12,6)

print(a.BFS(11))    #[11, 5, 2, 8, 4, 9, 7, 12, 1, 6, 3, 10]
print(a.DFS(11))    #[11, 8, 9, 2, 4, 7, 12, 6, 3, 10, 1, 5]
'''

'''
a = Graph()
a.addEdge("E","C")
a.addEdge("E","F")
a.addEdge("E","B")

a.addEdge("C","E")
a.addEdge("C","F")
a.addEdge("C","G")
a.addEdge("C","H")
a.addEdge("C","A")

a.addEdge("F","E")
a.addEdge("F","C")
a.addEdge("F","I")

a.addEdge("B","E")
a.addEdge("B","A")

a.addEdge("H","C")
a.addEdge("H","G")
a.addEdge("H","D")

a.addEdge("D","H")
a.addEdge("D","A")

a.addEdge("G","C")
a.addEdge("G","H")
a.addEdge("G","I")

a.addEdge("A","C")
a.addEdge("A","D")
a.addEdge("A","B")

a.addEdge("I","F")
a.addEdge("I","G")

print(a.BFS("E"))    #[E,C,F,B,G,H,A,I,D]
print(a.DFS("E"))    #[E,B,A,D,H,G,I,F,C]
'''      

# 參考來源
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# https://www.itread01.com/content/1544006352.html
# https://techdifferences.com/difference-between-bfs-and-dfs.html
# https://stackoverflow.com/questions/46383493/python-implement-breadth-first-search/46383689
