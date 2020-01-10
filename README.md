# Data Structure and Algorithms 
## 自介

我叫劉濬綸，是東吳巨資的學生，現居新北。

這裡大致上是本人的資結演算學習歷程，請隨意逛逛。

## 本學期課程心得

本學期課程很確實的讓我認清自己的能力極為不足，這些東西卻都是基本中的基本，因此是一個很花費課後和平時時間的事，無論是自己的努力理解學習，或是和同儕的討論，雖多少會有幫助，但都很有限。

畢竟每次作業都感受的到老師的大刀抵在脖子上，一不認真就直接要被送下去，每兩周都要緊張一次。

感謝老師和助教本學期的教學，不過如果明年本課程仍是老師和助教負責，煩請助教在作業格式和規範上盡量的統一和提早講清楚，多次的突然更改而且都在deadline前一天或當天，並且幾乎沒有收到通知，若非平常會緊張而頻繁去檢查簡報有無更新真的會措手不及。

老師自學院會議後的教學方式稍作修改後，我認為改善課程非常多，基本上所有概念和觀念都能在一堂課內快速理解了，至於老師原本堅持以及硬的部分，我支持老師繼續堅持和硬下去，畢竟生於憂患死於安樂，好過和舒服卻無實質學習的課程並不是對學生真正的好。

### 課程作業

HW1: [快速排序(Quick Sort)](https://github.com/Nyar8712/homework/tree/master/HW1)
<br>  HW2: [合併排序(Merge Sort) && 堆積排序(Heap Sort)](https://github.com/Nyar8712/homework/tree/master/HW2)
<br>  HW3: [二元搜尋樹(Binary Search Tree)](https://github.com/Nyar8712/homework/tree/master/HW3)
<br>  HW4: [雜湊表(Hash Table)](https://github.com/Nyar8712/homework/tree/master/HW4)
<br>  HW5: [廣度優先搜尋(Breath First Search) && 深度優先搜尋(Depth First Search)](https://github.com/Nyar8712/homework/tree/master/HW5)
<br>  HW6: [戴克斯特拉(Dijkstra Algorithm) && 克魯斯克爾演算法(Kruskal Algorithm)-最小生成樹及最短路徑問題](https://github.com/Nyar8712/homework/tree/master/HW6)

### Leetcode練習

課程以及自我練習: [Leetcode題目](https://github.com/Nyar8712/homework/tree/master/Leetcode)

### CS50

課程影片講解: [CS50](https://github.com/Nyar8712/homework/tree/master/CS50)

### Codesignal練習

自我課後練習: [Codesignal題目](https://github.com/Nyar8712/homework/tree/master/Codesignal)

Week1(9/9-9/15): 課程介紹
===============
講解上課方式以及計分方式。

從此開始，練習codesignal和leetcode的題目讓自己醒來，因在接下來的課程中不可能從基礎手把手教，因此透過刷題讓自己之前的所學趕快回神。

Codesignal以及Leetcode的連結在上方。

Week2(9/16-9/22): 鏈結串列(Linked List)
=======================================
linked list是一種資料儲存結構，透過一個array作為索引，並用一個指標接在後方，以此不斷接續，最後一個則接地(null)。每個node都帶有儲存的資料，以及一個link作為指向的指標。

鏈結串列與陣列的比較:

    1. 單一節點占用
       array僅需儲存資料，因此較少，而linked list由於需儲存資料以及指標，因此較大
    2. 整體記憶體使用率
       array由於建立時必須先給定整體大小，因此在無法確定資料量的情形下，預估錯誤導致資料過大爆掉或是過少導致浪費太多，因此整體空間利用率較低。
       linked list則只需要透過指標來做新增，不需要一個非常大的初始大小，需要就加不需要就刪，所以整體空間利用率較高，浪費較少。但有overhead所以每配一次節點都需呼叫一次。
    3. 新增與刪除
       array比較費時，每加或刪一筆都須檢視整個陣列來確認，需O(n)。
       linked list較為簡單，只須根據索引和指標來加或刪，費時O(1)。
    4. 串列合併和分解
       array需要完整檢視兩方的資料，需費時O(n)。
       linked list只需要將兩串列欲合併或分解部分的link接上或分開就好，費時O(1)。
    5. 循序存取及隨機存取
       array透過位址計算來存取，因此速度較快，O(1)。
       linked list在循序存取時要透過記憶體讀取鏈結欄位，才能到下一個節點，因此較為費時，而隨機存取時需透過串列開頭循序搜尋，費時O(n)。
       
本周練習: 
<br>  [Design Linked list](https://github.com/Nyar8712/homework/blob/master/Leetcode/707%23_Design%20Linked%20List_06170240.py)
       
Week3(9/23-9/29): 堆疊(Stack) && 佇列(Queue)
==================================
stack是一種有序串列的資料結構，其新增和刪除都在同一端進行，該端稱之為top，而另一端稱之為bottom。堆疊採用後進先出(LIFO, Last-in-First-out)的方式，在需要從堆疊中取出資料(pop up)時，會從最後新增(push down)的資料開始進行。

queue是一種有序的線性串列，新增和刪除在兩不同端，新增端稱之為後端(rear/tail)，刪除端則是前端(front/head)。佇列採用先進先出(FIFO, First-in-First-out)的方式，在需要從佇列中取出資料(dequeue)時，會從最初新增(enqueue)的資料開始進行。

佇列有1. Deque(Double-Ended-Queue), 2. Input-Restricted Deque, 3. Output-Restricted Deque三個變化，1者為兩端皆可以作為新增或刪除端的有序串列，2者為兩端皆可做為刪除端，但新增只能由固定一端進行，3者為兩端皆可做為新增端，但刪除只能由固定一端進行的有序串列。

本周練習: 
<br>  [Min Stack](https://github.com/Nyar8712/homework/blob/master/Leetcode/155%23_Min%20Stack_06170240.py)
<br>  [Implement Queue using Stacks](https://github.com/Nyar8712/homework/blob/master/Leetcode/232%23_Implement%20Queue%20using%20Stacks_06170240.py)

Week4(9/30-10/06): 集合(Set) && 新增排序(Insertion Sort)
==================
set是一個無序的資料型態，內部的資料值不重複，可以進行重複數據刪除，也可計算交集，聯集，差集等。set裡面的資料必須可以進行疊代。

Insertion Sort的原理非常單純，即是將資料一筆一筆逐一照順序的新增到以排序完成的序列中。
![image](https://github.com/Nyar8712/homework/blob/master/IMG/insertion.jpg)

如上圖所示，依序將值新增並進行排序，最後變完成該資料的排序。

本周練習: 
<br>  [Set Mismatch](https://github.com/Nyar8712/homework/blob/master/Leetcode/645%23_Set%20Mismatch_06170240.py)

Week5(10/07-10/13): 雙十國慶周
==================
國慶日所以停課了這樣，先開始預習下次要寫的作業！

Week6(10/14-10/20): 快速排序(Quick Sort) && 堆積排序(Heap Sort)提及
===================
本周在第4周開啟排序的課程之路後，立刻跟上兩個新的東西，快速排序的實作作業以及堆積排序的概念提及。

本周練習:
<br>  HW1: [快速排序(Quick Sort)](https://github.com/Nyar8712/homework/tree/master/HW1)

Week7(10/21-10/27): 堆積排序(Heap Sort)實作 && 合併排序(Merge Sort)
===================
補全上次提及的堆積排序，並且開始透過實作作業來確認學習，增加一個新的合併排序，並透過兩者的比較看出不同case下的差異。

本周練習:
<br>  HW2: [合併排序(Merge Sort) && 堆積排序(Heap Sort)](https://github.com/Nyar8712/homework/tree/master/HW2)

Week8(10/28-11/03): 二元樹(Binary Tree)
===================
二元樹是一棵可以為空(empty tree)，或者有一個樹根(root)與兩子樹(subtree)的樹，分別為左右子樹，而左右子樹也都是二元樹，並且子樹具有順序性。

當樹根設為第1層時，二元樹的第i層所有的節點最多為2^(i-1)個。

高度為k的二元樹節點數最多有(2^k)-1個。而完整符合此條件者稱之為完滿二元數(Full Binary Tree)。
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/fullB.jpg)

高度為k，從第一層到第k-1層節點全滿，但第k層只缺少最右側些許節點(也可以都不缺)，稱為完全二元樹(Complete Binary Tree)，其節點數介於2^(k-1)到(2^k)-1之間。
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/completeB.jpg)

若一顆二元樹，除了leaf以外，每個內部節點皆具有非empty的左右子樹，稱為嚴格二元樹(Strictly Binary Tree)，也就是說每個內部節點的子節點樹不是2就是0。
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/strictlyB.jpg)

若一棵二元樹，除了leaf以外，每個節點都只有其中同一個子樹，則稱之歪斜樹(Skewed Binary Tree)。
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/skewedB.jpg)

Week9(11/04-11/10): 二元搜尋樹(Binary Search Tree)
===================
二元搜尋樹也是一棵二元樹，是二元樹的延伸運用，其左子樹的後代皆小於樹根，右子樹的後代則都大於樹根，左右子樹本身也是二元搜尋樹。

如果建立出來的二元搜尋樹是一棵完全二元樹或完滿二元樹時，為best case，時間花費為O(nlogn)。

還有一種情況，若該BST的每個節點的左右子樹所含節點個數最多只差距1個節點，其也擁有高度最小的等性，比較次數也會是最少的，也是一個best case。

若建立出來的二元搜尋樹是一棵歪斜樹，則為worst case，花費時間為O(n^2)。

本周練習:
<br>  HW3: [二元搜尋樹(Binary Search Tree)](https://github.com/Nyar8712/homework/tree/master/HW3)

Week10(11/11-11/17): 紅黑樹(Red Black Tree)
===================
紅黑樹是一種二元搜尋樹，其必須滿足以下條件: 

    1. 每個節點非黑即紅
    2. 每個leaf都是黑
    3. 如果一個節點為紅，那他的兩個子節點都是黑
    4. 每個節點到所有leaf的路徑上的黑節點數目都相同
    5. 樹根一定是黑
紅黑樹的新增與刪除與二元搜尋樹相同，但其必須透過變色和旋轉(rotation)來維持樹，其旋轉的方式與AVL樹相似。
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/left-ro.jpg)
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/right-ro.jpg)
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/LR-ro.jpg)
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/RL-ro.jpg)

Week11(11/18-11/24): 雜湊表(Hash Table)
===================
本周老師介紹了一些文字加密的套件，並教了雜湊表和給予實作作業，在作業上鍵入資料值必須透過該加密方式進行。

本周練習:
<br>  HW4: [雜湊表(Hash Table)](https://github.com/Nyar8712/homework/tree/master/HW4)

Week12(11/25-12/01): 廣度優先搜尋(Breadth First Search)
===================
終於，在此開始進入了圖形的範疇，老師先從BFS開始著手，教導BFS的概念和原理。

至於實作部分，且待下周分曉。

差點忘了，本周進行了第一次Pair programmimg，意即兩人協力進行程式撰寫，一個人做領航員，負責提供想法和指揮，思索出程式碼擔任大腦，另一個則是駕駛員，負責實現想法及撰寫。

而我也清楚認知到我比較偏向駕駛員，我常常可以理解並迅速分析出概念和想法，但思考到以程式時做面時就死當，所以我比較傾向做駕駛員幫忙實現的分工。

兩個人的頭腦多少還是大於一個人，在進行時我們雙方都會互相闡述認知和想法，無論誰是什麼員，多少都會參與到雙方的範疇，也成功加深雙方的學習認知。

Week13(12/02-12/08): 深度優先搜尋(Depth First Search)
===================
接續著上次的BFS，這周則提及並探討DFS，並進行兩者的比較以及實作。

本周練習: 
<br>  HW5: [廣度優先搜尋(Breath First Search) && 深度優先搜尋(Depth First Search)](https://github.com/Nyar8712/homework/tree/master/HW5)

Week14(12/09-12/15): 最小生成樹(Minimum Spanning Tree) && 克魯斯克爾演算法(Kruskal Algorithm)
===================
加大力度探討圖形，除了搜尋以外，介紹了如何將圖形以最少的成本全數相連同時不出現cycle的Kruskal演算法，以生成一棵minimum spanning tree。

至於實作部分，同樣的且待下周分曉。

Week15(12/16-12/22): 最短路徑(Shortest Path) && 戴克斯特拉演算法(Dijkstra Algorithm)
===================
除了上次介紹的可以透過最小生成樹的圖形找到最短的路徑外，本次介紹了另一個找尋圖形上任一點到其他點的最短路徑走訪方式以及長度的Dijkstra演算法。同時本次作業也必須進行Kruskal和Dijkstra的實作。

本周練習:
<br>  HW6: [戴克斯特拉(Dijkstra Algorithm) && 克魯斯克爾演算法(Kruskal Algorithm)-最小生成樹及最短路徑問題](https://github.com/Nyar8712/homework/tree/master/HW6)

Week16(12/23-12/29): 總複習以及期末考規範
===================
本周老師將本學習課程中的重點全部進行了一次複習，並交代和陳述期末考的規範和題型。

原定計畫為第18周期末考，不過老師決定改為17周考，讓期末周的我們各科考試日期不要過度擁擠。

Week17(12/30-1/05): 期末考
===================
緊張已久的期末考終究降臨，班上大部分人都挺慎重的，我有點腦袋放空的走進教室。

題目難度出乎我意料的沒到那麼高，看的出來老師並非想要考倒我們或是要我們花費一堆時間埋頭苦寫，而是純粹要測試我們有沒有真正理解觀念和做法，並且學會用快速且有效率的方法來進行處理問題。

雖說如此，我感覺我的期末還是在危險邊緣，感覺隨時會掉到陷坑中，畢竟平時都是用notebook在寫作業和學習，很少動手撰寫程式，即便有讀pseudo code也很難用手來實現自己的想法，臨時抱佛腳的人絕對死得很慘，我也看到不少人退選了，甚至也有人直接放棄治療給當。

Week18(1/06-1/12): 寒假
===================
本周原定的期末考改為上周進行，因此本學期課程到此真正完全結束了，我也不確定我是否生還，至少收穫還是很多。

除了課程內容以外，更多時候感覺學的是態度和習慣的養成，如平時開始去接觸資訊相關的新聞或知識內容，開始願意更加深入加深自己的認知，寫程式和做事的好習慣的養成，這些都改善了不少，雖說仍因為分數而有汲汲營營的態度，不過此種狀況隨著學期的進行越來越少，更多的時候會希望自己學越多越好而非能過就好。

在此感謝老師本學期的課程教學。
