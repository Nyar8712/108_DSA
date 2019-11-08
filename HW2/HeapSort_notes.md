#  Heap Sort
## 觀念
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/heap_sort_concept.jpg)
Heap Sort排序的方式主要是透過建立一個堆積(為一完全二元樹)，並藉由最大堆積或最小堆積來進行排序輸出。
* 排序流程(以最大堆積為例子)：
  1. 將原始資料照順序放入一棵完全二元樹中。
  2. 接下來建立堆積，檢查最底下的子樹(樹葉)，若其比父節點來的大，則和父節點交換。
  3. 在整棵樹內重複執行 ii直至整棵樹保持唯一最大堆積的狀態。
  4. 進行排序，將樹根(最大值)和最後一片樹葉交換，並把原樹根輸出。
  5. 執行 iii以使樹保持在最大堆積狀態，再執行 iv。
  6. 重複進行 v直到資料值全數輸出後，會發現從資料中的最大值一路輸出到最小值，排序便完成了。
  
  
概念理解不是難題，但程式碼的組成和架構讓我看了頭腦打結，因此我循規蹈矩去找了最基本的模式來閱讀理解(C語言我掌握度不夠，因此僅參考其架構助自己了解)
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/heap_sort_frame.jpg)
有稍微好懂一些，先建構一個堆積，從位置來定論，節點的位置由1到n，而每個節點的左子樹位置必定是2 * 自己的位置，右子樹為2 * 自己的位置+1，而父節點則是(自己的位置/2)取floor。透過這樣的方式節點的尋找會變相對清楚，當左子樹還未超過第n項時，同時左子樹小於右子樹，代表兄弟間是毫無問題的，就繼續往下。當自己小於自己的左或右子樹時，則必須跟他交換，兄弟間如果左大於右也要交換，持續直至全部完成，這時就會呈現一個最大堆積的樹了。

接下來就是對堆積作排序，當i的位置還沒到第1項，就進行排序至保持最大堆積，而若現在位置正是第n項，便把其與樹根(位置第1項)交換，原樹根會跑到第n位置並輸出，這時最大堆積可能已經被破壞，所以再重複進行前面提及的i的位置還未到第1項時進行排序，以上流成就如此一般反覆進行，直到最後，所有資料值都從最後一片葉子輸出完後，排序也就完成了。

## 我的過程
為了開始在實作中的起步，我參照了以下網址來協助
* http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html
<br>  透過此我了解堆積排序的實質進行，而程式碼的部分則瀏覽了
* https://repl.it/@kcsommers/Heap-Sort-Python
* https://www.sanfoundry.com/python-program-implement-heapsort/
<br>  來摸熟架構和建立的方式。在跟同學討論時，發現到大部分人參考來源給出的寫法都差不了太多，而不少人都有解讀和理解上的困難，我自己也一樣，因此我打算把程式碼剖開來，分多一點部分讓自己能個別解讀。

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/heap_sort_sortcall.jpg)
正式開始實作，首先資料值如果僅有1筆或0筆就直接丟出去就好。這個是Heap Sort的執行部分，可以看到進行呼叫build_max_heap函式，這個函式是用來不斷維護最大堆積的，呼叫後便會使資料值成為最大堆積，再來就是第一步，把樹根和最後一片樹葉做交換，接下來檢查堆積內，有沒有任何節點違反最大堆積，有的話便呼叫heapify函式來進行排序調整，其位置會從0開始。再來就反覆執行到堆積資料都空了，整個串列就排完了，此時便回傳以排序完之資料。到這可能有些突兀，詳細函式部份且待下方分曉。

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/heap_sort_build_max_heap.jpg)
如同前面觀念部分定義的父節點，左子樹以及右子樹，在此用函式定義好當前位置，並回傳其左右子樹的位置點，以及父節點的位置，接著便要來說明剛剛提及的build_max_heap函式了。首先指定一個變數存放父節點位置資訊，當其還不到0，就會呼叫heapify函式以進行調整，直至全部調整完到位置到樹根，此時堆積便已維護完畢成一最大堆積。

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/heap_sort_heapify.jpg)
建立heapify函式，判定其左子樹所在位置如果當前節點位置，則將其設為最大值，反之則為當前節點，而若右子樹大於最大值則右子樹為最大值，持續進行下去，會找到最終的最大值，這時若其不是當前節點，則將當前節點與最大值交換，並呼叫自身函式重複進行。

## 流程圖
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/heap_sort.jpg)