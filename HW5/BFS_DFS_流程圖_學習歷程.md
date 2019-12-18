# BFS 與 DFS 流程圖與學習歷程
## BFS 學習歷程
先從根本起手，因為其追蹤方式和先追蹤到的節點之後繼節點就優先追蹤的特性，跟佇列的先進先出特性吻合，所以用queue來實作此部分。

建立一個list作為queue，一個list ANS作為dequeue的值存放處，並且先將起點都先加入兩串列。設一個走訪確認的list，長度等同圖形長度，初值為False代表所有節點皆尚未走訪過，而走訪過的值則會被設為True。

這時可以先將起始點改為True因已被檢查了，當queue並非空的的存在狀態時，將第0筆(最先進入)值dequeue，並進行檢查確認，在圖形中下一個值，如果其為被做走訪完畢標記，則將其enqueue進入佇列中，同時標記為True(已走訪)，並在其dequeue時加進ANS中。重複進行以上步驟，直至整個圖形中所有節點都已走訪完畢。

以上步驟全數完成並確認完畢後，回傳ANS就是廣度優先搜尋的追蹤結果了。

## BFS 流程圖
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/BFS.jpg)

## DFS 學習歷程


## DFS 流程圖
接續BFS流程圖中之例子

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/DFS.jpg)
