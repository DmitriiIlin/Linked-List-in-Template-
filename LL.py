#python 3.5.2
import random, unittest, LL_mod 

def data_for_tests_one(self,randomnumber):
    one=LL_mod.Node(randomnumber)
    s_list=LL_mod.LinkedList()
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
        self.Linked_List_for_zero_test=LL_mod.LinkedList()
        for i in range(0,len(list_for_first_test)):
            self.Linked_List_for_zero_test.add_in_tail(LL_mod.Node(list_for_first_test[i]))
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
        self.Linked_List_for_second_test=LL_mod.LinkedList()
        #Добавление эл-та в конец 
        for i in range(0,len(list_for_second_test)):
            self.Linked_List_for_second_test.add_in_tail(LL_mod.Node(list_for_second_test[i]))
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
        self.Linked_List_for_third_test=LL_mod.LinkedList()
        #Добавление эл-та в конец
        for i in range(0,len(list_for_third_test)):
            self.Linked_List_for_third_test.add_in_tail(LL_mod.Node(list_for_third_test[i]))
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
        self.Linked_List_for_third_1_test=LL_mod.LinkedList()
        self.Linked_List_for_third_2_test=LL_mod.LinkedList()
        list_for_third_1_test=List_maker(number) 
        list_for_third_2_test=List_maker(number)
        sum_list=[] 
        for i in range(0,len(list_for_third_1_test)):
            sum_list.append(list_for_third_1_test[i]+list_for_third_2_test[i])
        for i in range(0,len(list_for_third_1_test)):
            self.Linked_List_for_third_1_test.add_in_tail(LL_mod.Node(list_for_third_1_test[i]))
        for i in range(0,len(list_for_third_2_test)):
            self.Linked_List_for_third_2_test.add_in_tail(LL_mod.Node(list_for_third_2_test[i]))
        Sum_LL=LL_mod.add_linked_lists(self.Linked_List_for_third_1_test,self.Linked_List_for_third_2_test)
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
        
        
        
