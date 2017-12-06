
class Node(object):
    """docstring for Node"""
    def __init__(self,elem):
        #存放节点元素
        self.elem = elem
        #存放下一节点标识
        self.next = None
        
        



class SingleLinkList(object):
    """单链表"""
    def __init__(self,node_tmp = None):
        #私有属性存放头节点
        self._head = node_tmp
 

    """链表是否为空"""
    def is_empty(self):
        return self._head == None

    """链表长度"""
    def length(self):
        #cur 游标，用来移动遍历节点
        cur = self._head
        # count 记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    """遍历整个链表"""
    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next


    #链表头部添加元素
    def add(self,item_t):
        pass

    """链表尾部添加元素"""
    def append(self,item_t):
        node = Node(item_t)
        if self.is_empty() :
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    """指定位置插入元素"""
    def insert(self,pos,item_t):
        pass

    """删除节点"""
    def remove(self,item_t):
        pass

    """查找节点是否存在"""
    def search(self):
        pass


def main():
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.travel()

if __name__ == '__main__':
    main()