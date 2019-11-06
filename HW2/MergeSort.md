# Merge Sort
## 觀念
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/merge_sort_concept.jpg)
Merge Sort與Quick Sort一樣，皆是採用個別擊破的原理，將資料做分群後進行比較。
* 分群後的處理：
  1. 將資料值先一分為二，此時得到兩群。
  2. 這兩群分別再繼續分群，直至所有值都被分開。
  3. 兩群組成一群，然後群內進行比較並排序，這時就會得到若干兩個一群的排序完畢群。
  4. 重複進行 iii，不斷把兩群合併回來並進行排序，最後就會得到一個全部排序完成的大群，此大群也就會是排序完的資料值。
  
  
我在用程式呈現慢慢的不斷分不斷分再合回來的方式上碰到了點瓶頸，於是我從書上看到可以用遞迴來進行實現
<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/merge_sort_recursive.jpg)
花了將近20多分鐘去理解，我認知到遞迴的方式是靠著pointer來協助進行，首先設定好p和q表示前半和後半群的資料位置，並用head和tail指標來進行指向，在pq都不是空值時，兩者從各自代表的群的第0項開始，當p位置的值比q大時，指標指向q，p的值輸出，原本指著p的指標則指向p的下一個，以此類推，最後指標接地後，代表資料已輸出完，排序就完成了。

## 我的過程
為了協助自己在實現上的理解，我上網搜尋了一番，找到以下解說
* https://www.educative.io/edpresso/merge-sort-in-python
<br>  透過他的動圖解釋，我進一步搞清楚怎麼以遞迴方式實作合併排序，於是我便開始動手，非常輕鬆寫意的，開頭就錯了。我想我應該是沒有切實的理解想法或概念，找同學討論並詢問時，才發現我的類別格式寫錯了，所以不用說排序，基本就免談了，我也趕緊去看了看python的類別怎麼寫。

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/merge_sort_lessthan2.jpg)
正式開始作Merge Sort，首先判斷測值的量，如果只有一筆或空的list就根本不需要比，直接原封不動回傳就好。

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/merge_sort_partition1.jpg)
設一個divide代表測值list長度的一半，取整數，並且將第0筆值到divide(一半)存在left，將divide到最後一筆存在right，同時多建立三個integer變數m，p，q，初值皆為0代表在該list的第0筆，p為left的指向位置，q為right的，m則是存輸出值的list的指向位置。這時呼叫自己一次，將left和right也進行一樣的動作去遞迴，直至left和right也成為排序完成的list。

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/merge_sort_compare.jpg)
p < left的長度意味著當left的每個位置跑完前都會繼續執行，q亦如是。當left的第p項(從0開始)"小於"right的第q項(從0開始)時，將left的第p項輸出到nums的第m項，這時p+1指向下一位置，m+1指向下一位置，反之若是"大於"，則是輸出right的第q項，然後q+1指向下一位置。以上步驟持續至left或right的值都輸出完畢為止，此時輸出完的群的位置指向一定在最後一個。

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/merge_sort_remain.jpg)
接續上述，這時假若left還未輸出完畢，也就是說p還小於left的長度，就將值輸出，p+1，m+1，right的部分也是同樣道理，直至所有值都完成後，nums就會成為一個新的以排序完成list，因此最後回傳nums就會呈現排序完成的list了。

## 流程圖

<br>  ![image](https://github.com/Nyar8712/homework/blob/master/IMG/Merge_sort.jpg)
