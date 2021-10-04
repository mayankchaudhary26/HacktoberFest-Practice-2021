def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        hash_map={}
        temp=head
        while temp:
            hash_map[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if not temp.next:
                hash_map[temp].next=None
            else:
                hash_map[temp].next=hash_map[temp.next]
            if temp.random==None :
                hash_map[temp].random=None
            else:
                hash_map[temp].random=hash_map[temp.random]
            temp=temp.next
        return hash_map[head]
