"""定义链表中的一个节点"""
class ListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

"""实现一个单向链表"""
class SingleLinkList(object):
    def __init__(self):
        self.head = None

    # 判断链表是否为空
    def is_empty(self):
        return self.head is None
    
    # 获取链表长度
    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next

        return count

    # 遍历链表
    def items(self):
        cur = self.head
        while cur:
            yield cur.item
            cur = cur.next

    # 从头部添加元素
    def add(self, item):
        node = ListNode(item)
        node.next = self.head
        self.head = node
    
    # 从尾部添加元素
    def append(self, item):
        node = ListNode(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    
    # 指定位置插入元素
    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > self.length() - 1:
            self.append(item)
        else:
            node = ListNode(item)
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
    
    # 删除节点
    def remove(self, item):
        cur = self.head
        # 有两种情况，第一个元素就是要删除的，那么直接让head指向第一个节点的下个节点；
        # 第二种情况就是要删除的节点在中间，需要该节点前一个节点的next指向该节点后一个节点，需要一个变量记录当前节点的前一个节点
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
    
    # 判断某元素是否存在
    def find(self, item):
        return item in self.items()

"""实现一个循环链表，最后一个节点的next指向第一个节点"""
class SingleCycleList(object):
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def length(self):
        if self.is_empty():
            return 0
        
        count = 1
        cur = self.head
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count
    
    def items(self):
        cur = self.head

        if self.is_empty():
            return

        while cur.next != self.head:
            yield cur.item
            cur = cur.next
        yield cur.item

    def add(self, item):
        node = ListNode(item)

        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            node.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
        
        self.head = node

    def append(self, item):
        node = ListNode(item)

        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > self.length() - 1:
            self.append(item)
        else:
            node = ListNode(item)
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        
        cur = self.head
        pre = None

        if cur.item == item:
            if cur.next == self.head:
                self.head = None
            else:
                while cur.next != self.head:
                    cur = cur.next
                
                cur.next = self.head.next
                self.head = self.head.next
                return True
        else:
            while cur.next != self.head:
                if cur.item == item:
                    pre.next = cur.next
                    return True
                else:
                    pre = cur
                    cur = cur.next
        
        if cur.item == item:
            pre.next = self.head
            return True
    
    def find(self, item):
        return item in self.items()

"""实现一个双向链表"""
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class BilateralLinkList(object):
    def __init__(self):
        self.head = None
    
    