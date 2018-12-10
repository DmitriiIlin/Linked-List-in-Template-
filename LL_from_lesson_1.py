#python 3.5.2
import random
class Node:
    def __init__(self,value):
        # Инициализация класса Node
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        # Инициализация класса LinkedList
        self.head=None
        self.tail=None
        
    def add_in_tail(self,item):
        # Метод класса LL позволяющий добавить элемент класса Node в конец списка
        if self.head is None:
            self.head=item
        else:
            self.tail.next=item
        self.tail=item
        
    def print_all_nodes(self):
        # Метод класса LL, позволяющий вывести LL 
        node=self.head
        while node!=None:
            print(node.value,'вывод print all nodes')
            node=node.next
            
    def del_node(self,val,parametr=0):
        # Метод удаления значения из LL, при parametr=1 удаляет 1 элемент, при parametr=0 удаляет все искомые элементы
       node = self.head
       while node is not None:
           if (node.value==self.head.value) and (node.value==val):
               new_head=node.next
               self.head=new_head
           elif (node.value==self.tail.value) and (node.value==val):
               self.tail=node_pr.value
           elif node.value == val:
               node_pr.next=node.next
           if parametr==1:
               break
           node_pr=node
           node=node.next 
                            
    def clean_list(self):
        # Удаление всех элементов LL
        node=self.head
        while node is not None:
            node.value=None
            node_pr=node
            node=node.next
            node_pr.next=None
        self.head=None
        self.tail=None
        
    def find_all_in_list(self,val):
        #Поиск элементов и возвращение найденных значений
        result=[]
        element_result=[]
        node=self.head
        while node is not None:
            if node.value==val:
                element_result.append(node.value)  
            node=node.next  
        return element_result   
                
    def lenght_list(self):
        # Метод класса LL, расчитывающий кол-во э-в класса Node в LL (длина LL)
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l 

    def insert_node(self,number,val):
        # Метод класса LL позволяющий вставить э-т Node в LL
        if self.head==None:
            self.tail=self.head=Node(val)
        elif number==0:
            new_node=Node(val)
            new_node.next=self.head
            self.head=new_node
        else:
            curr_node=self.head
            count=1
            while curr_node != None:
                if count==number:
                    new_node=Node(val)
                    new_node.next=curr_node.next
                    curr_node.next=new_node
                    break
                count+=1    
                curr_node=curr_node.next

def add_linked_lists(list_1,list_2):
    # Функция складывающая значения двух LL при условии равенства длин и равенства содержания знач.==int
    if list_1.lenght_list()==list_2.lenght_list():
        sum_linked_list=LinkedList()
        sum_node=None
        node_1=list_1.head
        node_2=list_2.head
        val=None
        for i in range(0,list_1.lenght_list()):
            if (int(node_1.value)==node_1.value) and (int(node_2.value)==node_2.value):
                val=node_1.value+node_2.value
                sum_node=Node(val)
                sum_linked_list.add_in_tail(sum_node)
                node_1=node_1.next
                node_2=node_2.next
        return sum_linked_list     
    else:
        return None
            
def test_1(q,w,e,r,t,y):
    #Вводим 5 значений для списка, 6 значение для удаления
    print('***Создание связанного списка Tect_1***')
    first_list=LinkedList()
    number=Node(int(q))
    first_list.add_in_tail(number)
    number=Node(int(w))
    first_list.add_in_tail(number)
    number=Node(int(e))
    first_list.add_in_tail(number)
    number=Node(int(r))
    first_list.add_in_tail(number)
    number=Node(int(t))
    first_list.add_in_tail(number)
    first_list.print_all_nodes()   
    print('**************************')
    print('***Удаление значения Tect_1***')
    first_list.del_node(y)
    first_list.print_all_nodes()
    print('**************************')
    print('***Очистка списка Тест_1***')
    first_list.clean_list()
    first_list.print_all_nodes()
    print('**************************')
def test_2(q,w,e,r,t,y,u,p):
    #Вводим 5 значений для списка, y значение для поиска элемента, u значение номер э-та после которого вставляем новый элемент p
    print('***Создание связанного списка Тест_2***')
    first_list=LinkedList()
    number=Node(int(q))
    first_list.add_in_tail(number)
    number=Node(int(w))
    first_list.add_in_tail(number)
    number=Node(int(e))
    first_list.add_in_tail(number)
    number=Node(int(r))
    first_list.add_in_tail(number)
    number=Node(int(t))
    first_list.add_in_tail(number)
    first_list.print_all_nodes()
    print('***Поиск значения Тест 2***')
    print(first_list.find_all_in_list(y))
    print('**************************')
    print('***Длина списка Тест2***')
    print(first_list.lenght_list())
    print('**************************')
    print('***Вставка элемента Тест2***')
    first_list.insert_node(u,p)
    first_list.print_all_nodes()
    print('**************************')
def test_3(q,w,e,r,i):
    print('***Тест_3***')
    first_list=LinkedList()
    number=Node(int(q))
    first_list.add_in_tail(number)
    number=Node(int(w))
    first_list.add_in_tail(number)
    number=Node(int(e))
    first_list.add_in_tail(number)
    number=Node(int(r))
    first_list.add_in_tail(number)
    first_list.print_all_nodes()
    print('**************************')
    second_list=LinkedList()
    number=Node(int(q*i))
    second_list.add_in_tail(number)
    number=Node(int(w*i))
    second_list.add_in_tail(number)
    number=Node(int(e*i))
    second_list.add_in_tail(number)
    number=Node(int(r*i))
    second_list.add_in_tail(number)  
    second_list.print_all_nodes()
    sum_list=LinkedList()
    sum_list=add_linked_lists(first_list,second_list)
    print('**************************')
    print('***Если списки одинаковых размеров то суммируем, Тест3***')
    sum_list.print_all_nodes()
    print('**************************')
#K=test_1(56,56,56,56,56,56)
#Z=test_2(34,56,23,12,12,100,100,100)
D=test_3(10,3,6,25,2)

        
        
        
