struct Node {
    int val;
    Node* next;
    Node(int x) : val(x), next(NULL) {}
};

class MyLinkedList {
public:
    /** Initialize your data structure here. */
    Node* head;
    Node* tail;
    int size;
    MyLinkedList() {
        head = NULL;
        tail = NULL;
        size = 0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index >= size) return -1;
        Node* cur = this->head;
        while(index--) cur = cur->next;
        return cur->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        size++;
        Node* root = new Node(val);
        root->next = head;
        // if (this->head != NULL) delete(head);
        this->head = root;
        if (size == 1) this->tail = this->head;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        size++;
        Node* newTail = new Node(val);
        this->tail->next = newTail;
        this->tail = newTail;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index > size || index < 0) return;
        if (index == 0) {
            addAtHead(val);
            return;
        }
        if (index == size) {
            addAtTail(val);
            return;
        }
        size++;
        Node* cur = this->head;
        while(--index) cur = cur->next;
        Node* newNode = new Node(val);
        newNode->next = cur->next;
        cur->next = newNode;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index >= size || index < 0) return;
        if (index == 0) {
            if (size == 1) {
                delete(this->head);
            } else {
                Node* newHead = this->head->next;
                delete(this->head);
                this->head = newHead;
            }
            size--;
            return;
        }
        if (index == size - 1) {
            Node* cur = this->head;
            while(--index) cur = cur->next;
            delete cur->next;
            this->tail = cur;
            size--;
            return;
        }
        Node* cur = this->head;
        while(--index) cur = cur->next;
        Node* right = cur->next->next;
        delete(cur->next);
        cur->next = right;
        size--;
    }
};
