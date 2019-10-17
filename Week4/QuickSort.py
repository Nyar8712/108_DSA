#!/usr/bin/env python
# coding: utf-8

#     有關於快速排序，我先去找書讀以理解其排序方式：
#     1. 採用個別擊破(Divide-and-Conquer)的原理來進行，將資料先做分群(partition)
#        ，再分別對兩群資料做處理。
#     2. partition的做法：
#         (1) 從資料值裡面，挑一個基準點(pivot)。
#         (2) 將所有資料值與pivot去做比較，小於pivot的值歸類在一群，大於的則歸類在另一群。
#         (3) 把pivot置放在兩群中間，如此資料值會排成「小於pivot的群」+pivot+「大於pivot的群」。
#         (4) 接下來，對兩群資料本身也重複做(1)~(3)，直至全部資料值排序完成。

# In[24]:


import random                   
def QuickSort(alist):
    if len(alist) <= 1:    #測值只有一個或無資料值
        return alist
    left = []             #先建出三個空串列
    mid = []
    right = []
    pivot = random.choice(alist)    #從alist測值中隨機挑選一個值做為基準點
    print(pivot)                    #將每次分群時挑選的pivot印出
    for element in alist:           #開始挑值來進行分群
        if element == pivot:            #將測值分成三群
            mid.append(element)
        elif element < pivot:
            left.append(element)
        else:
            right.append(element)
            
    return QuickSort(left) + mid + QuickSort(right)  #最後對left和right兩群重複進行排序


#     這邊就開始做排序了，根據我在老師提供的程式碼和閱讀書得到的了解，基準點可以任意挑選不受限制，所以我先import random套件進來，做隨機選資料值。我打算用陣列來做，因此先建了三個list，然後把不需要排序的可能先找出來，也就是測值僅有一筆或根本沒資料時，這時就直接回傳測值內容就好了。

#     用判斷式來進行分群，當測值小於基準時會被加入left中，大於則會加入right，相等的值加入mid。如此一來，在迴圈進行完後，會得到三組群，如同上面partition第(3)所說的"小於基準值的群"+"等於基準值的群"+"大於基準值的群"，接下來只要再對left和right反覆做相同的事情，不斷分群然後排序，直到全部排序完成，在將這三個list內的值回傳，就完成快速排序了。

# In[25]:


alist= [23,14,7,91,0,7,12,54,7]
QuickSort(alist)


#     以一筆測值為例
