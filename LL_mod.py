"""
Реализация класса Linked List и Node в шаблоне
"""
class Node:

    def __init__(self, v):
        #Инициализация класса Node
        self.value = v
        self.next = None
    
class LinkedList:  

    def __init__(self):
        #Инициализация класса Linked List
        self.head = None
        self.tail = None
        
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        
    def print_all_nodes(self):
        # Метод класса LL, позволяющий вывести LL 
        node=self.head
        while node!=None:
            print(node.value,'вывод print all nodes')
            node=node.next

    def find(self, val):
        # Метод класса LL, реализующий поиск по значению
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def clean(self):
        # Удаление всех элементов LL
        node=self.head
        while node is not None:
            node.value=None
            node_pr=node
            node=node.next
            node_pr.next=None
        self.head=None
        self.tail=None

    def find_all(self,val):
        #Поиск элементов и возвращение найденных значений
        element_result=[]
        i=0
        node=self.head
        while node is not None:
            if node.value==val:
                element_result.append(node)  
            node=node.next  
            i+=1
        return element_result

    def len(self):
        # Метод класса LL, определяющий кол-во э-в класса Node в LL (длина LL)
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l 


    def delete(self,val,all=False):
        # Метод удаления значения из LL, при all=False удаляет 1 элемент, при all=True удаляет все искомые элементы
        node = self.head
        while node is not None:
            if (self.head==self.tail) and (self.head.value==self.tail.value==val):
                node=None
                self.head=None
                self.tail=None
                break
            if (node.value==self.head.value) and (node.value==val):
                new_head=node.next
                self.head=new_head
                if all==False:
                    break
            elif (node.value == val) and (self.tail!=node):
                node_pr.next=node.next
                if all==False:
                    break
            elif (node.value==self.tail.value) and (node.value==val):
                self.tail=node_pr
                node_pr.next=None
                self.next=node_pr.next
                if all==False:
                    break
            if node.value!=val:
                node_pr=node
            node=node.next

    def insert(self,afterNode,newNode):
        # Метод класса LL позволяющий вставить э-т newNode в LL
        # после эл-та afterNode, где afterNode указывается как параметр value
        if  (self.head==None) and (afterNode==None):
            newNode.next=None
            self.head=newNode
            self.tail=newNode
        elif (self.head!=None):
            curr_node=self.head
            while curr_node != None:
                if (curr_node.value==afterNode.value):
                    newNode.next=curr_node.next
                    curr_node.next=newNode
                    break
                elif (curr_node==self.tail) and (curr_node.value==afterNode.value):
                    curr_node.next=newNode
                    self.tail=newNode
                    break    
                curr_node=curr_node.next
    
def add_linked_lists(list_1,list_2):
# Функция складывающая значения двух LL при условии равенства длин и равенства содержания знач.==int
    if list_1.len()==list_2.len():
        sum_linked_list=LinkedList()
        sum_node=None
        node_1=list_1.head
        node_2=list_2.head
        val=None
        for i in range(0,list_1.len()):
            if (int(node_1.value)==node_1.value) and (int(node_2.value)==node_2.value):
                val=node_1.value+node_2.value
                sum_node=Node(val)
                sum_linked_list.add_in_tail(sum_node)
                node_1=node_1.next
                node_2=node_2.next
        return sum_linked_list     
    else:
        return None


