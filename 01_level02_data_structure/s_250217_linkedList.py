
### 연결 리스트

# 배열 : 메모리가 연속적이며, 추가 및 수정에 오버헤드(컴퓨터가 힘들어해요)가 발생한다.
# 연결 리스트 : 메모리 위치된 곳은 상관 없이, 서로가 서로를 가르켜 연결하는 방식, 수정 및 추가, 삭제 등이 매우 간단하고 편리하다.



# 챌린지 1.

# 아래는 제가 구현한 연결리스트 클래스 입니다.
# 한줄 한줄 주석을 달아서 이게 뭔지, 어떤 동작인지 설명해보세요.

class LinkedList:
    def __init__(self):
        self.head = None  # 연결 리스트의 첫 번째 노드를 가리키는 head 포인터
        self.nodes = []   # 노드를 저장하는 리스트

    class Node:
        def __init__(self, data):
            self.data = data  # 노드의 데이터
            self.prev = None  # 이전 노드를 가리키는 포인터
            self.next = None  # 다음 노드를 가리키는 포인터

        def __str__(self):
            return f"{self.data}"  # 노드의 데이터를 문자열로 반환

    def push_back(self, data):
        new_node = self.Node(data)  # 새로운 노드 생성
        if not self.head:  # 리스트가 비어 있으면
            self.head = new_node  # head를 새로운 노드로 설정
            prevNode = None
        else:
            self.nodes[-1].next = new_node  # 마지막 노드의 next를 새로운 노드로 연결
            prevNode = self.nodes[-1]  # 이전 노드를 마지막 노드로 설정
        self.nodes.append(new_node)  # 노드 리스트에 추가
        self.nodes[-1].prev = prevNode  # 현재 노드의 prev를 이전 노드로 설정
    
    def insert(self, find_data, insert_data):
        new_node = self.Node(insert_data)  # 삽입할 새로운 노드 생성
        isFind = False
        for node in self.nodes:  # 리스트에서 find_data를 가진 노드를 찾음
            if node.data == find_data:
                curNode = node
                isFind = True
                break
        if not isFind:  # 찾지 못하면 함수 종료
            return    

        if curNode.prev is not None:  # 삽입할 위치가 head가 아닐 경우
            new_node.prev = curNode.prev  # 새로운 노드의 prev를 이전 노드로 설정
            curNode.prev.next = new_node  # 이전 노드의 next를 새로운 노드로 설정
            curNode.prev = new_node  # 현재 노드의 prev를 새로운 노드로 설정
            new_node.next = curNode  # 새로운 노드의 next를 현재 노드로 설정
        else:  # 삽입할 위치가 head일 경우
            self.head = new_node  # head를 새로운 노드로 변경
            new_node.prev = None
            new_node.next = curNode
            curNode.prev = new_node

    def delete(self, del_data):
        for node in self.nodes:  # 리스트에서 삭제할 노드를 찾음
            if node.data == del_data:
                delData = node
                break
        if self.head == delData:  # 삭제할 노드가 head일 경우
            self.head = delData.next
        elif delData.next is None:  # 마지막 노드를 삭제하는 경우
            delData.prev.next = None
        else:  # 중간 노드를 삭제하는 경우
            delData.prev.next = delData.next
            delData.next.prev = delData.prev
        del(delData)  # 노드 삭제

    def find(self, find_data):
        findNode = None
        for node in self.nodes:  # 리스트에서 찾을 노드를 탐색
            if node.data == find_data:
                findNode = node
                break
        return findNode  # 찾은 노드 반환 (없으면 None 반환)
        
    def print_list(self, reverse=False):
        current = self.head
        if not reverse:  # 정방향 출력
            print('정방향 출력 : ', end='')
            while current:
                print(current, end=" -> ")
                current = current.next
            print("None")
        else:  # 역방향 출력
            print('역방향 출력 : ', end='')
            while current.next is not None:  # 리스트 끝까지 이동
                current = current.next
            while current is not None:  # 역방향으로 출력
                print(current, end=' --> ')
                current = current.prev
            print("None")

# 연결 리스트 테스트
list2 = LinkedList()
list2.push_back('굼씨')
list2.push_back('진씨')
list2.print_list()
list2.insert('굼씨', '주씨')
list2.print_list()
