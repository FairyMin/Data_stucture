
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
        self.__head = node_tmp
 

    """链表是否为空"""
    def is_empty(self):
        return self.__head == None

    """链表长度"""
    def length(self):
        #cur 游标，用来移动遍历节点
        cur = self.__head
        # count 记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    """遍历整个链表"""
    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem,end = " ")
            cur = cur.next


    """链表头部添加元素,头插法"""
    def add(self,item_t):
        node = Node(item_t)
        node.next = self.__head
        self.__head = node

    """链表尾部添加元素,尾插法"""
    def append(self,item_t):
        node = Node(item_t)
        if self.is_empty() :
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    """指定位置插入元素"""
    def insert(self,pos,item_t):
        node = Node(item_t)
        pre = self.__head
        #特殊情况的考虑要多注意！！pos输入超出范围
        if pos <=0:
            self.add(item_t)
        elif pos>(self.length()-1):
            self.append(item_t)
        else:
            count = 0
            while count+1 < pos:
                pre = pre.next
                count += 1

            node.next = pre.next
            #此处 的pre.next 与 前一句的pre.next？？！！
            pre.next = node

    """删除节点--用两个游标"""
    def remove(self,item_t):
        cur = self.__head
        pre = None

        while cur != None:
            if cur.elem == item_t:
                #判断此节点是否为头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    """查找节点是否存在"""
    def search(self,item_t):
        cur = self.__head

        while cur != None:
            if cur.elem == item_t:
                return True
            else:
                cur = cur.next
        return False


def main():
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.add(9)
    ll.append(4)
    ll.insert(3,7)
    ll.insert(-99,99)
    ll.insert(100,88)
    ll.remove(7)
    ll.travel()

if __name__ == '__main__':
    main()