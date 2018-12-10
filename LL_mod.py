"""
Реализация класса Linked List и Node в шаблоне
"""
import random, unittest
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

    def find_all(self,val):
        #Поиск элементов и возвращение найденных значений
        element_result=[]
        i=0
        node=self.head
        while node is not None:
            if node.value==val:
                element_result.append(i)  
            node=node.next  
            i+=1
        return element_result

    def lenght_list(self):
        # Метод класса LL, определяющий кол-во э-в класса Node в LL (длина LL)
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l 


    def del_node(self,val,all=False):
        # Метод удаления значения из LL, при all=False удаляет 1 элемент, при all=True удаляет все искомые элементы
        node = self.head
        while node is not None:
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
            self.print_all_nodes()   
            node_pr=node
            node=node.next
        self.print_all_nodes()

    def insert_node(self,afternode,newNode):
        # Метод класса LL позволяющий вставить э-т Node в LL
        if self.head==None:
            self.tail=self.head=Node(newNode)
        elif afternode==0:
            new_node=Node(newNode)
            new_node.next=self.head
            self.head=new_node
        else:
            curr_node=self.head
            count=1
            while curr_node != None:
                if count==afternode:
                    new_node=Node(newNode)
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

    
def data_for_tests_one(self,randomnumber):
    one=Node(randomnumber)
    s_list=LinkedList()
    s_list.add_in_tail(one)
    return s_list

def random_generation_number():
    number=random.randint(1,10**9)
    return int(number) 

def List_maker(number):
    Value_for_LL=[]
    for i in range(0,number):
        Value_for_LL.append(random_generation_number())
    return Value_for_LL

class Linked_List_2_Tests(unittest.TestCase):
   
    def test_zero(self):
        #Тест проверяет связанный список с нулем элементов
        number=1
        list_for_first_test=List_maker(number)
        self.Linked_List_for_zero_test=LinkedList()
        for i in range(0,len(list_for_first_test)):
            self.Linked_List_for_zero_test.add_in_tail(Node(list_for_first_test[i]))
        node_1=self.Linked_List_for_zero_test.head
        for i in range(0,self.Linked_List_for_zero_test.lenght_list()):
            print(node_1.value)
            self.assertEqual(list_for_first_test[i],node_1.value)
            node_1=node_1.next

    def test_one(self):
        #Тест для связанного списка из 1 эл-та
        number=2
        index_for_delete=random.randint(0,number)
        value_for_insert=random_generation_number()
        position_for_insert=1
        list_for_second_test=List_maker(number)        
        self.Linked_List_for_second_test=LinkedList()
        #Добавление эл-та в конец 
        for i in range(0,len(list_for_second_test)):
            self.Linked_List_for_second_test.add_in_tail(Node(list_for_second_test[i]))
        node_2=self.Linked_List_for_second_test.head
        for i in range(0,self.Linked_List_for_second_test.lenght_list()):
            print(node_2.value)
            self.assertEqual(list_for_second_test[i],node_2.value)
            node_2=node_2.next
        print(list_for_second_test)
        #Вставка элемента
        list_for_second_test.insert(position_for_insert,value_for_insert)
        self.Linked_List_for_second_test.insert_node(position_for_insert,value_for_insert)
        node_2=self.Linked_List_for_second_test.head
        for i in range(0,self.Linked_List_for_second_test.lenght_list()):
            print(node_2.value)
            self.assertEqual(list_for_second_test[i],node_2.value)
            node_2=node_2.next
        print(list_for_second_test)
        #Поиск элемента который вставили
        find_node=self.Linked_List_for_second_test.find(value_for_insert)
        self.assertEqual(find_node.value,value_for_insert)
        #Поиск элемента по значению
        index_for_find=random.randint(0,number)
        value_for_find=list_for_second_test[index_for_find]
        find_element=self.Linked_List_for_second_test.find(value_for_find)
        self.assertEqual(value_for_find,find_element.value)
        #Удаление элемента
        value_for_delete=list_for_second_test[index_for_delete]
        list_for_second_test.remove(value_for_delete)
        print(list_for_second_test)
        self.Linked_List_for_second_test.del_node(value_for_delete)
        self.Linked_List_for_second_test.print_all_nodes()
        node_2=self.Linked_List_for_second_test.head
        print(self.Linked_List_for_second_test.lenght_list())
        for i in range(0,self.Linked_List_for_second_test.lenght_list()):
            self.assertEqual(list_for_second_test[i],node_2.value)
            node_2=node_2.next

    def test_big_LL(self):
        #Тест для большого кол-ва элементов
        number=random.randint(10,30)
        index_for_delete=random.randint(0,number)
        value_for_insert=random_generation_number()
        position_for_insert=random.randint(0,number)
        list_for_third_test=List_maker(number)        
        self.Linked_List_for_third_test=LinkedList()
        #Добавление эл-та в конец
        for i in range(0,len(list_for_third_test)):
            self.Linked_List_for_third_test.add_in_tail(Node(list_for_third_test[i]))
        node_3=self.Linked_List_for_third_test.head
        for i in range(0,self.Linked_List_for_third_test.lenght_list()):
            print(node_3.value)
            self.assertEqual(list_for_third_test[i],node_3.value)
            node_3=node_3.next
        #Вставка элемента
        list_for_third_test.insert(position_for_insert,value_for_insert)
        self.Linked_List_for_third_test.insert_node(position_for_insert,value_for_insert)
        node_3=self.Linked_List_for_third_test.head
        for i in range(0,self.Linked_List_for_third_test.lenght_list()):
            print(node_3.value)
            self.assertEqual(list_for_third_test[i],node_3.value)
            node_3=node_3.next
        print(list_for_third_test)
        #Поиск элемента который вставили
        find_node=self.Linked_List_for_third_test.find(value_for_insert)
        print(find_node.value,value_for_insert)
        self.assertEqual(find_node.value,value_for_insert) 
        #Поиск элемента по значению
        index_for_find=random.randint(0,number)
        value_for_find=list_for_third_test[index_for_find]
        find_element=self.Linked_List_for_third_test.find(value_for_find)
        self.assertEqual(value_for_find,find_element.value)
        #Удаление элемента
        value_for_delete=list_for_third_test[index_for_delete]
        list_for_third_test.remove(value_for_delete)
        print(list_for_third_test)
        self.Linked_List_for_third_test.del_node(value_for_delete)
        self.Linked_List_for_third_test.print_all_nodes()
        node_3=self.Linked_List_for_third_test.head
        print(self.Linked_List_for_third_test.lenght_list())
        for i in range(0,self.Linked_List_for_third_test.lenght_list()):
            self.assertEqual(list_for_third_test[i],node_3.value)
            node_3=node_3.next
        #Сложение двух списков
        self.Linked_List_for_third_1_test=LinkedList()
        self.Linked_List_for_third_2_test=LinkedList()
        list_for_third_1_test=List_maker(number) 
        list_for_third_2_test=List_maker(number)
        sum_list=[] 
        for i in range(0,len(list_for_third_1_test)):
            sum_list.append(list_for_third_1_test[i]+list_for_third_2_test[i])
        for i in range(0,len(list_for_third_1_test)):
            self.Linked_List_for_third_1_test.add_in_tail(Node(list_for_third_1_test[i]))
        for i in range(0,len(list_for_third_2_test)):
            self.Linked_List_for_third_2_test.add_in_tail(Node(list_for_third_2_test[i]))
        Sum_LL=add_linked_lists(self.Linked_List_for_third_1_test,self.Linked_List_for_third_2_test)
        Sum_Node=Sum_LL.head
        for i in range(0,Sum_LL.lenght_list()):
            self.assertEqual(Sum_Node.value,sum_list[i])
            Sum_Node=Sum_Node.next


if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()
