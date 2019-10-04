class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = [] # 用串列實作queue
        self.size = 0   # 初始串列長度為 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x) # 新增資料值到佇列中
        self.size += 1       # 串列長度增加1
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size -= 1          # 串列長度-1
        return self.queue.pop(0) # 從佇列中將最前面的資料值pop出
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]    # 回傳佇列最前面的資料值

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size == 0:      #如果串列長度為0 回傳True表示佇列是空的 反之亦然
            return True
        else:
            return False
