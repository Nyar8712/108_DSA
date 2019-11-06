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
<br>  ![image]()
https://www.educative.io/edpresso/merge-sort-in-python
