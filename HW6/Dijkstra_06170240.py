
from collections import defaultdict 

class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]]
        self.kruskalgroup = [[],[],[]]
    def addEdge(self,u,v,w):
        self.kruskalgroup[0].append(u)
        self.kruskalgroup[1].append(v)
        self.kruskalgroup[2].append(w)
        return 
    def Dijkstra(self, s): 
        test1 = self.graph
        ans = test1[s]
        count = [s]
        anskey = []
        for a in range(len(self.graph)):
            anskey.append(str(a))
        for i in range(len(test1)-1):
            c = ans
            zz = []
            ss = []
            for i in count:
                ss.append(ans[i])
            for j in ans:
                if j not in ss:
                    zz.append(j)        
            e = min(zz)
            which_i_chose =ans.index(e)
            count.append(which_i_chose)
            compare = test1[which_i_chose]
            how_much_to_add = ans[which_i_chose]
            for g in range(len(compare)):
                if compare[g] != 0:
                    if g not in count:
                        compare[g] = compare[g] + how_much_to_add
                          
            for l in range(len(ans)):
                if l not in count:
                    if compare[l] != 0:
                        if ans[l] == 0:
                            ans[l] =compare[l]
                        else:
                            r = compare[l]
                            s = ans[l]
                            t = min([r,s])
                            ans[l] = t          
        anstrue = zip(anskey,ans)
        return dict(anstrue)
        
    def yesno(self,q):
        test = 0
        for i in q:
            if i == -1:
                test = test+1
        if test == 1:
            return True
        else:
            return False
        
        
    def Kruskal(self):
        src = []
        dest = []
        wei = []
        head = self.kruskalgroup[0]
        end =self.kruskalgroup[1]
        weight = self.kruskalgroup[2]
        count = []
        whdelet = []
        times = 0
        test123 = []
        whatinthis = []
        number = []
        
        for uu in range(len(head)):
            test123.append(head[uu])
            test123.append(end[uu])
            
        qqqq = set(test123)
        test456 = list(qqqq)
        for i in range(len(test456)):
            count.append(-1)
        
        for i in range(len(test456)):
            whatinthis.append(i)
        
        for i in test456:
            number.append(i)
        
        
        testtest = zip(whatinthis,number)
        testtest1 = zip(number,whatinthis)
        changetable2 = dict(testtest)
        changetable1 = dict(testtest1)
        
        
        end = [changetable1[x] if x in changetable1 else x for x in end]
        head = [changetable1[x] if x in changetable1 else x for x in head]
        
        for i in range(len(weight) - 1):
            for j in range(len(weight) - 1 - i):
                if weight[j] > weight[j + 1]:
                    weight[j], weight[j + 1] = weight[j + 1], weight[j]
                    head[j], head[j + 1] =head[j + 1], head[j]
                    end[j], end[j + 1] = end[j + 1], end[j]

        
        for a in range(len(head)):
            if self.yesno(count) == True:
                break
            if count[end[a]] == -1:
                if count[head[a]] == -1:
                    count[end[a]] = head[a]
                else:
                    count[end[a]] = count[head[a]]
            elif head[a] == count[end[a]]:
                whdelet.append(a)
            else:
                if count[head[a]] == -1:
                    cur = count[end[a]]
                    for no in range(len(count)):
                        if count[no] == cur:
                            count[no] = head[a]
                    count[cur] = head[a]
                else:
                    nu = count[end[a]]
                    for no in range(len(count)):
                        if count[no] == nu:
                            count[no] = count[head[a]]
                    count[nu] = head[head[a]]
                    
            times += 1
        
        for r in range(times):
            src.append(head[r])
            dest.append(end[r])
            wei.append(weight[r])
        
        j = 0
        for k in whdelet:
            l = k - j
            del src[l]
            del dest[l]
            del wei[l]
            j += 1
        src = [changetable2[x] if x in changetable2 else x for x in src ]
        dest= [changetable2[x] if x in changetable2 else x for x in dest]
        lesstotal = []
        for lt in range(len(src)):
            lesstotal.append(str(src[lt])+"-"+str(dest[lt]))
            
        ans = zip(lesstotal,wei)
        return dict(ans)

#
g = Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
        [4,0,8,0,0,0,0,11,0],
        [0,8,0,7,0,4,0,0,2],
        [0,0,7,0,9,14,0,0,0],
        [0,0,0,9,0,10,0,0,0],
        [0,0,4,14,10,0,2,0,0],
        [0,0,0,0,0,2,0,1,6],
        [8,11,0,0,0,0,1,0,7],
        [0,0,2,0,0,0,6,7,0]]
print("Dijkstra:", g.Dijkstra(0))

#
g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
print("Kruskal:", g.Kruskal())

'''
參考來源:
https://github.com/yang-yoa-ying/06170104/blob/master/HW6/Dijkstra_06170104.py
https://www.lfhacks.com/tech/python-list-element-replace
https://thispointer.com/python-how-to-convert-a-list-to-dictionary/
https://www.runoob.com/python3/python3-set.html
https://ithelp.ithome.com.tw/articles/10209593
https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html
http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html
http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html
'''
