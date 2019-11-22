# Binary Search Tree
## 原理
二元搜尋樹本身可以是空的。
* 非空的二元搜尋樹則必須滿足4個條件：
  1. 每個節點儲存一個值(識別碼)
  2. 每個節點的左子樹之中，所有節點存的值都會比該節點的來的小
  3. 每個節點的右子樹之中，所有節點存的值都會比該節點的來的大
  4. 每一節點之左右子樹本身也是二元搜尋樹
## 學習歷程
樹的結構，基礎是一棵二元樹，可以為空，有序性，差別在於左右子樹的規定不同，與二元樹擁有相同的三種追蹤(traversal)方式。

1. 前序追蹤(Preorder)

    (1). 先追蹤樹根
  
    (2). 以遞迴方式追蹤左子樹的節點
  
    (3). 以遞迴方式追蹤右子樹的節點
  
2. 中序追蹤(Inorder)

    (1). 先以遞迴追蹤左子樹的節點
  
    (2). 再追蹤樹根
  
    (3). 以遞迴方式追蹤右子樹的節點
  
3. 後序追蹤(Postorder)

    (1). 先以遞迴追蹤左子樹的節點
  
    (2). 再以遞迴追蹤右子樹的節點
  
    (3). 最後再追蹤樹根
  
在設計上根據值的案例，所花費時間也不一樣。

1. Best case 最佳案例

    情況發生在完全二元樹時，平均比較次數為(1/n)Σ(logk取floor | k from i to n)= O(logn)
    
2. Worst case 最糟情況

    當此二元搜尋樹是歪斜樹時，由於每次成功搜尋都必須不斷往下找，每個節點都會跑過一遍，因此平均比較次數為
    
    ((n(n-1)/2) * 1/n)+1=((n-1)/2)+1=(n+1)/2=O(n)
    
3. Average case 平均情況

    新增，刪除和搜尋子節點部分所花的時間都是logn，因此平均次數為O(logn)，即便是最糟情況下，由於關係到樹的高度，可以藉由樹的高度將時間複雜度降至O(logn)。
    
越是高度平衡的樹，花費的時間也會越少，相同key值也可能會有很多不同排列的樹型(如下圖)，因此要預測其樹型是不可能的。
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/sametree.jpg)
以下則為圖解追蹤部分，可以清楚了解到各種追蹤的方式順序，越往下的節點之間的分支越短，中序甚至可以將樹壓扁來看出追蹤順序。
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/bst_travaersal.jpg)

## 流程圖

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/bst.jpg)
    

## 參照來源

我主要參考以下三個影片來進行設計：

https://www.youtube.com/watch?v=Zaf8EOVa72I

https://www.youtube.com/watch?v=f5dU3xoE6ms

https://www.youtube.com/watch?v=YlgPi75hIBc&t=

本次作業以及學習歷程部分，巨資三B(06170225)陳昱昇教導了我非常多，從最一開始BST邏輯卡住都是問他來開通大腦理解，到後來自己程式碼的邏輯不正確也是他替我解答，幫助我認知問題在何處，並解決錯誤，因此本次作業真要說，一定有部分的邏輯和想法是參考詢問他的想法，在此附上他的github網址。

https://github.com/samuel871211/My-python-code
