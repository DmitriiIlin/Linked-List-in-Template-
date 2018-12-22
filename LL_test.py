import random, unittest, LL_mod 

def random_number():
    i=random.randint(0,100)
    return i

def Node_create(i):
    return LL_mod.Node(i)

class Linked_List_2_Tests(unittest.TestCase):
    
    def test_insert_in_empty_list(self):
        # Проверка ф-ции insert при пустом списке
        LL_1=LL_mod.LinkedList()
        LL_2=LL_mod.LinkedList()
        i=random_number()
        Node=Node_create(i)
        LL_1.add_in_tail(Node)
        if LL_2.len()==0:
            LL_2.insert(None,i)
        Node_LL_1=LL_1.head
        Node_LL_2=LL_2.head
        for j in range (0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,Node_LL_2.value)

    def test_insert_with_one_element(self):
        #Проверка ф-ции insert для списка с 1 элементом. Вставка э-та после первого
        #э-та, повторная вставка и далее вставка после изначально существующего эл-та. 
        LL_1=LL_mod.LinkedList()
        LL_2=LL_mod.LinkedList()
        i=random_number()
        j=random_number()
        LL_1.add_in_tail(Node_create(i))
        LL_2.insert(None,i)
        Node_LL_1=LL_1.head
        Node_LL_2=LL_2.head
        for j in range (0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,Node_LL_2.value)
        LL_1.add_in_tail(Node_create(j))
        LL_2.insert(i,j)
        Node_LL_1=LL_1.head
        Node_LL_2=LL_2.head
        for j in range (0,LL_1.len()):
            self.assertEqual(Node_LL_1.value,Node_LL_2.value)

    def test_insert_in_last_position(self):
        #Вставка в конец списка
        LL_1=LL_mod.LinkedList()
        LL_2=LL_mod.LinkedList()
        data=[]
        for i in range(0,10):
            data.append(random_number())
        for i in range(0,10):
            RN=random_number()
            if i==9:
                LL_1.add_in_tail(Node_create(RN))
                LL_2.insert(PN,RN)
            else:
                LL_1.add_in_tail(Node_create(RN))
                LL_2.add_in_tail(Node_create(RN))
            PN=RN
        Node_LL_1=LL_1.head
        Node_LL_2=LL_2.head
        for i in range(0,10):
            self.assertEqual(Node_LL_1.value,Node_LL_2.value)

    def test_insert_in_random_position(self):
       #Вставка в случайную позицию
        LL_1=LL_mod.LinkedList()
        LL_2=LL_mod.LinkedList()
        data=[]
        random_position=random.randint(1,8)
        for i in range(0,10):
            data.append(random_number())
        for i in range(0,10):
            RN=data[i]
            if i==random_position:
                LL_1.add_in_tail(Node_create(RN))
                LL_2.insert(PN,RN)
            else:
                LL_1.add_in_tail(Node_create(RN))
                LL_2.add_in_tail(Node_create(RN))
            PN=RN
        Node_LL_1=LL_1.head
        Node_LL_2=LL_2.head
        for i in range(0,10):
            self.assertEqual(Node_LL_1.value,Node_LL_2.value)    

        

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()