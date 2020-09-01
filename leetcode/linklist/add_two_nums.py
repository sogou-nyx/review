"""给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    思路：在循环中依次取两个链表相同位置的数字做加法，把加完的结果的各位存在新链表的相同位置，如果有进位则保存，用于下一个位置的加法运算。
    一直到两个链表都遍历完成并且没有进位为止（如果链表遍历完，但是有一个进位，还是需要在新链表中增加一个节点保存进位值）
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        # 创建新的节点，从此节点开始生成新的链表存储结果，temp为节点，cur用于遍历
        temp = cur = ListNode(None)
        # 初始进位值
        s = 0

        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(s % 10)
            cur = cur.next
            # 求进位
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return temp.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    print(s.addTwoNumbers(l1, l2))