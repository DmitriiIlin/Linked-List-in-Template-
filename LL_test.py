import random, unittest, LL_mod 

def random_number():
    i=random.randint(0,100)
    return i

def Node_create(i):
    Node=LL_mod.Node(i)
    return Node


class Linked_List_2_Tests(unittest.TestCase):
    
    def test_insert_in_empty_list(self):
        # Проверка ф-ции insert при пустом списке
        LL_1=LL_mod.LinkedList()
        i=random_number()
        Node=Node_create(i)
        if LL_1.len()==0:
            LL_1.insert(None,Node)
        Node_LL_1=LL_1.head
        self.assertEqual(LL_1.head.value,i)
        for j in range (0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,i)

    def test_insert_with_one_element(self):
        #Проверка ф-ции insert для списка с 1 элементом. Вставка э-та после первого
        #э-та, далее вставка после предварительно вставленного эл-та. 
        LL_1=LL_mod.LinkedList()
        Q_ty=3
        data=[]
        for i in range (0,Q_ty):
            j=random_number()
            data.append(j)
        LL_1.add_in_tail(Node_create(data[0]))
        LL_1.insert(data[0],Node_create(data[1]))
        LL_1.insert(data[1],Node_create(data[2]))
        Node_LL_1=LL_1.head
        for i in range (0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next


    def test_insert_in_last_position(self):
        #Вставка в конец списка
        LL_1=LL_mod.LinkedList()
        data=[]
        for i in range(0,10):
            data.append(random_number())
        for i in range(0,10):
            RN=random_number()
            if i==9:
                LL_1.insert(data[i],Node_create(RN))
                data.append(i)
            else:
                LL_1.add_in_tail(Node_create(data[i]))
        Node_LL_1=LL_1.head
        for i in range(0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next

    def test_insert_in_random_position(self):
       #Вставка в случайную позицию, случайного значения
        LL_1=LL_mod.LinkedList()
        data=[]
        random_position=random.randint(1,8)
        random_value=random.randint(1,100)
        for i in range(0,10):
            data.append(random_number())    
        for i in range(0,len(data)):
            LL_1.add_in_tail(Node_create(data[i]))
        data.insert(random_position,random_value)
        LL_1.insert(data[random_position-1],Node_create(random_value))    
        Node_LL_1=LL_1.head
        for i in range(0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,data[i])
            Node_LL_1=Node_LL_1.next    

        

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()