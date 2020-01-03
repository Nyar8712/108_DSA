# Dijkstra 與 Kruskal 原理，流程圖，學習歷程
## Dijkstra 原理
從最近的點開始，依照非遞減順序找出每個點的最短路徑。

由指定的原點作為初始點開始，計算其與其他頂點的直接距離，若無法到達者則皆先記為無限大。

接下來，從直線距離中找出最短者，將其加入已找到最短的路徑的集合中，並繼續計算與剩餘頂點的距離，仍無法到達者皆先記為無限大。

以上步驟持續至所有頂點都納入已找到最短的路徑的集合中後，便完成並可得到該初始點到所有其餘頂點的最短路徑了。

## Dijkstra 流程圖

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/Dijkstra.jpg)

## Dijkstra 學習歷程

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/Dijkstra_learn_code.jpg)

幾乎全是看著外部參考資料和別人的連結學和寫的，外觀大多是啃pseudo code來的。

在理解末段時產生極大的困境，最後仍然理解的未到很全面。

==================================my name la 分隔線==================================

### Kruskal 原理
先從圖中找到最短的邊長(權重最小)，並把其加入minimum spanning tree的圖之中。

接下來依序由權重越小，到權重最大的邊來處理，依序加入圖中。

若是進行過程中，有任何一條邊的加入會導致圖形中出現迴路(cycle)，則該邊不加入，並接續至下一權重的邊，也就是說捨棄當前權重最重的邊。

以上重複進行，直至所有點都被連接在一起形成一個圖形後，就完成了一棵最小生成樹了。

## Kruskal 流程圖

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/Kruskal.jpg)

## Kruskal 學習歷程

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/Kruskal_learn_code.jpg)

幾乎全是看著外部參考資料和別人的連結學和寫的，外觀連啃pseudo code都啃不出個勁來。

雖然學習到觀念和想法，但實作的部分還是太弱。

## 參考資料
以下是本次作業的參考資料，這次的資料來源比起之前多了非常多，也感謝巨資三A楊曜寧幫助我理解及實現。

他的github: https://github.com/yang-yoa-ying/06170104

https://www.lfhacks.com/tech/python-list-element-replace

https://thispointer.com/python-how-to-convert-a-list-to-dictionary/

https://www.runoob.com/python3/python3-set.html

https://ithelp.ithome.com.tw/articles/10209593

https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html

http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html

http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html
