class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_linked_list(head, target):
    # 1. ვქმნით დროებით მიმთითებელს (Current), რათა 'head' არ დავკარგოთ
    current = head 

    # 2. გადავაადგილებთ current-ს და არა head-ს
    while current is not None:
        
        # 3. ვამოწმებთ მიმდინარე კვანძის მონაცემს
        if current.data == target:
            return True  # მნიშვნელობა ნაპოვნია
            
        # 4. გადავდივართ შემდეგ კვანძზე
        current = current.next

    return False  # თუ ციკლი დასრულდა და ვერ ვიპოვეთ

def insert_at_end(head, value):
    new_node = Node(value)
    
    # თუ სია ცარიელია, ახალი კვანძი ხდება Head
    if head is None:
        return new_node
    
    # ვიყენებთ current-ს, რომ head არ დავკარგოთ
    current = head
    while current.next is not None:
        current = current.next
        
    # ბოლო კვანძის ბმულს ვაერთებთ ახალ კვანძთან
    current.next = new_node
    
    return head

def insert_at_position(head, pos, data):
    # 1. თუ პოზიცია ვალიდური არ არის
    if pos < 1:
        print("შეცდომა: პოზიცია უნდა იყოს 1 ან მეტი!")
        return head

    # 2. სპეციალური შემთხვევა: ჩამატება თავში (pos == 1)
    if pos == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node

    # 3. ვეძებთ პოზიციას
    current = head
    count = 1
    
    # მივდივართ სასურველ პოზიციამდე ან სიის ბოლომდე
    while count < pos - 1 and current is not None:
        current = current.next
        count += 1

    # 4. თუ current არის None, ნიშნავს რომ სია იმაზე მოკლეა, ვიდრე ვითხოვდით
    if current is None:
        print(f"შეცდომა: სიაში არ არის {pos-1} ელემენტიც კი!")
        return head

    # 5. ჩამატების პროცესი (აქ თანმიმდევრობა კრიტიკულია!)
    new_node = Node(data)
    new_node.next = current.next  # ჯერ ახალს ვაბამთ მომდევნოს
    current.next = new_node       # მერე წინას ვაბამთ ახალზე
    
    return head


def delete_at_position(head, position):
    if head is None or position < 1:
        return head
    
    # შემთხვევა 1: თავის წაშლა
    if position == 1:
        return head.next

    current = head
    # მივდივართ წასაშლელი კვანძის წინ მდგომ კვანძთან
    for i in range(1, position - 1):
        if current is not None:
            current = current.next
    
    # თუ პოზიცია სიაზე დიდია
    if current is None or current.next is None:
        print("პოზიცია სცილდება სიის ფარგლებს")
        return head
    
    # წაშლის ლოგიკა: გადავაბამთ წინა კვანძს წასაშლელის მომდევნოზე
    current.next = current.next.next
    
    return head