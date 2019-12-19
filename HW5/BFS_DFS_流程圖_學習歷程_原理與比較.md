# BFS 與 DFS 原理，比較，流程圖與學習歷程
## BFS 原理
廣度優先搜尋法可以選擇圖形上的任意一頂點作為起始點，接下依鄰接串列的次序走訪與該頂點相鄰的其他頂點，也就是用level-by-level的方式進行。

先走訪完相同層的所有頂點後，才會走訪下一層的頂點，反覆執行，直到每層先走訪的頂點都沒有未走訪的相鄰頂點時為止。

## BFS 學習歷程
先從根本起手，因為其追蹤方式和先追蹤到的節點之後繼節點就優先追蹤的特性，跟佇列的先進先出特性吻合，所以用queue來實作此部分。

建立一個list作為queue，一個list ANS作為dequeue的值存放處，開始先將起始點enqueue，當queue非空時，將queue中第0筆值(最先進入)dequeue。

如果此時dequeue出的值尚未加進ANS中，則將其append到ANS list，並將下一走訪目標定為圖形中的此值位置，接下來，把尚未走訪的圖形之中的下一走訪點enqueue進入。以上步驟不斷重複，直至queue全空。

以上步驟全數完成並確認完畢後，回傳ANS就是廣度優先搜尋的追蹤結果了。

## BFS 流程圖
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/BFS.jpg)

## DFS 原理 
深度優先搜尋同樣的也可選擇圖形上任意一個頂點為起始點，並依照鄰接串列的次序走訪下一層的新頂點，如此反覆進行，持續直至一頂點，其沒有相鄰頂點或是其所有相鄰頂點都被走訪，是一個用最後追蹤的頂點持續走訪未追蹤的相鄰頂點的方法。

若此時最後頂點的相鄰頂點皆已走訪完畢，則退回上一層的頂點，並反覆進行，直到所有頂點走訪完畢為止。

## DFS 學習歷程
從追蹤方式開始，其走訪方視為不斷深入到最後一層先進頂點，把最後一層走訪完畢後再退回前面層的頂點走訪，與堆疊的後進先出的特性相吻合，因以stack來實作。

建立兩個list，一個ANS存放pop out的值，另一個stack則是追蹤暫存處，開始將起始點push in，當stack目前非空，將其中最後一筆值(最後進入)pop out。

當pop out的值尚未加入ANS中，則將其加入，並將下一走訪目標定為圖形中的此值位置，接下來，把尚未走訪的圖形之中下一走訪點push in。以上步驟不斷重複，同樣直至stack全空。

以上步驟全數完成並確認完畢後，回傳ANS就是深度優先搜尋的追蹤結果了。

## DFS 流程圖
接續BFS流程圖中之例子

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/DFS.jpg)

## BFS與DFS之比較

1. 基本

   BFS是基於圖形頂點的追蹤法，DFS則是基於邊的追蹤。
   
2. 存取頂點的資料結構

   BFS使用queue(佇列)存取，DFS則是使用stack(堆疊)。
   
3. 記憶體使用

   BFS消耗較記憶體高空間，為低效能的使用；DFS則消耗較低，為高效能應用。
   
4. 追蹤

   BFS率先走訪先進入之level，以及同層未走訪之頂點；DFS則是沿著邊深入至最後一層，走訪完後再倒退回上層繼續做追蹤。
   
5. 最佳性

   BFS在找尋最短路徑上擁有最佳性，但成本上並無；DFS則不是最佳的搜尋方式。
   
6. 時間複雜度

   圖形用鄰接串列表示時，BFS的時間複雜度為O(n+e) 或者O(e)，DFS同樣為O(n+e)或O(e)。n代表頂點個數，而e則是邊個數。
   
另外，DFS由於不斷深入，走訪相鄰頂點，再退回的特性，可以使用遞迴的方式不斷遞迴執行這樣的追蹤，而遞迴的時間複雜度跟非遞迴相同。BFS則無法使用遞迴，只能透過佇列與迴圈實現。

由於兩者追蹤特性，BFS追蹤出的樹圖路線會是寬並且單一路徑皆比較短，DFS則會追蹤出狹窄但單一路徑較深的圖形結構。因此當問題圖形是比較狹長的樹時適合用DFS，反之寬但短的則適合用BFS。

兩者在空間複雜度上有較大的不同，BFS必須將每個節點都存在記憶體空間，DFS花費線性空間是因為必須要存下帶有未走訪節點的單一路徑。在最壞情況下如值得量非常大，BFS存取佇列上每個節點就非常占據記憶體空間，但DFS只存取路徑長度的空間，而這通常比節點數小很多，因此BFS對空間的使用較為低效，DFS則較為高效。

## 參考資料

我參考了以下網址來幫助我進行邏輯思考：

https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

https://www.itread01.com/content/1544006352.html

https://techdifferences.com/difference-between-bfs-and-dfs.html

https://stackoverflow.com/questions/46383493/python-implement-breadth-first-search/46383689

本次作業原本我認為已完成時，被巨資三B陳昱昇同學指出程式碼中的關鍵錯誤，因此得以及時修改完畢，要不是有他指出致命問題所在真的要炸了。
