class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def PrintLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp=self.head
        llstr=""
        while temp:
            llstr+=str(temp.data)+"->"
            temp=temp.next
        print(llstr)
    
    def legnth(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count

    def insert_at_begining(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next: temp=temp.next
        temp.next=Node(data)
        
    def insert_at_index(self,index,data):
        if index<0 and index>=self.legnth:
            raise Exception("Index is not valid")
        if index==0:
            self.insert_at_begining(data)
            return
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            temp1=temp.next
            node=Node(data)
            temp.next=node
            node.next=temp1

    def insert_data_list(self,index, data_list):
        if index<0 and index>=self.legnth:
            raise Exception("Index is not valid")
        else:
            temp=self.head
            count=0
            while temp:
                if count==index-1:
                    temp1=temp.next
                    for data in data_list:
                        node=Node(data)
                        temp.next=node
                        temp=temp.next
                    temp.next=temp1
                    break
                temp=temp.next

    def delete_at_index(self,index):
        if index<0 and index>=self.legnth:
            raise Exception("Index is not valid")
        if index==0: 
            self.head=self.head.next
            return
        else:
            count=0
            temp=self.head
            while temp:
                if count==index-1:
                    temp.next=temp.next.next
                    break
                temp=temp.next
                count+=1


if __name__ == '__main__':                   
    ll=LinkedList()
    ll.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)

    ll.head.next=second
    second.next=third
    third.next=fourth

    ll.insert_at_begining(19)
    ll.insert_at_end(25)
    ll.insert_at_index(2,22)
    ll.insert_at_index(4,42)
    ll.insert_data_list(1,[12,13,14])
    ll.delete_at_index(4)
    ll.PrintLinkedList()
    print(ll.legnth())