# DSA 



Week1(9/9-9/13)
===============
Week2(9/16-9/20): Designed Linked List
=======================================
Week3(9/23-9/27): Stack and Queue
==================================
Week4(9/30-10/04): Set, Insertion Sort, Quick Sort
===================================================
* Quick Sort時空複雜度: 
   1. Best case: 
      pivot的選擇恰巧是中間值，可以把剩餘測值分成兩等量群，花在分群的時間為O(n)，因每個值都必須跑過一次。而分群後對群再重複進行分群就是原本的一半
      ，直到全部完成為止，總共的花費時間即為  
      -      T(n)=cn+T(⌊(n-1)/2⌋)+T(⌈(n-1)/2⌉)  
                 ≤cn+2T(n/2)
                 ≤cn+2[c*n/2+2T(n/2²)]
                 ≤2cn+2²T(n/2²)
                 ≤(log2 n)cn+nT(1)
             T(n)=O(nlogn)
   2. Worst case: 
      pivot選擇都選到了極值(最大值或最小值)，導致分群無法成功一分為二，每次分群都變成pivot跟剩下一整群比。分群時間仍然是O(n)，但之後的每次進行則是
      n-1，n-2，n-3...到最後一次，因此花費時間為  
      -      T(n)=cn+T(n-1)
                 =cn+c(n-1)+T(n-2)
                 =cn+c(n-1)+c(n-2)+...+c*2+T(1)
                 =c*((n(n-1))/2)
                 =θ(n²)
   3. Average case: 
      我從書上讀到T. Cormen推導平均時間的方式
    	   令資料值為x1<x2<x3<...<xn，排序過程中任兩項資料xi跟xj(i<j)之比較次數可能是0或1次。在partition時，pivot選到xi-xj之外的值，他們兩個就有
      機會比較；pivot選到xi-xj之間(xi<pivot<xj)，這兩個就會被分開而不比較；pivot選到xi或xj，他們兩個就會剛好比較一次。因此，任兩資料值互相比較一
      次的機率是2/(j-i+1)，說明快速排序的比較次數期望值為
      -      ∑_(i=1)^(n-1)∑_(j=i+1)^n2/(j-i+1)= ∑_(i=1)^(n-1)∑_(k=1)^(n-i)2/(k+1)< ∑_(i=1)^(n-1)∑_(k=1)^n2/k
					                               = ∑_(i=1)^(n-1)O(logn)
					                               = O(nlogn)
   4. 空間複雜度: 
      -      best case和average case都是O(logn)
             2*(n/2)+2*(n/4)+2*(n/8)+...+1=n+n/2+n/4+...+1 
             取log，logn+1/2logn+1/4logn+...+log1=clogn，常數c可被忽略
             因此額外空間為O(logn)
             worst case則為O(n)
             因為都取最大或最小，導致每次比的資料量都只少一筆
             (n-1)+(n-2)+(n-3)+...+n-k，n-k為1，也就是次數為k=n-1次
             因此額外空間為O(n)
   5. 結論: 
      可以看到，平均時間複雜度僅為線性對數時間，比許多排序法如合併排序(merge sort)，插入排序(insertion sort)，氣泡排序(bubble sort)等，都要來的
      少，而worst case的發生機率非常的低，因此以速度來說可以說是很好的排序法。
![Alt text](/C:/Users/Hp/Desktop/QuickSort_Partition.jpg "Quick sort")
  * [QuickSort homework](https://github.com/Nyar8712/homework/blob/master/Week4/QuickSort.ipynb "my quick sort homework")

Week5(10/07-10/11)
==================
Week6(10/14-10/18):
===================

