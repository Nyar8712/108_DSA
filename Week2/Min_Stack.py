class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # 用串列實作
        self.size = 0    # 設定初始堆疊高度

    def push(self, x: int) -> None:
        self.stack.append(x)  #將資料值push進stack
        self.size += 1        #堆疊高度+1
    def pop(self) -> None:
        self.stack.pop()      #將堆疊頂端資料pop出
        self.size -= 1        #堆疊高度-1
    def top(self) -> int:
        return self.stack[self.size - 1]  #回傳堆疊頂端值

    def getMin(self) -> int:    #取堆疊中的最小值
        return min(self.stack)
