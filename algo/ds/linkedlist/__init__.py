class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        head = f"{self.val}"
        cur = self.next
        if cur is not None:
            head += f" -> {cur}"
            cur = cur.next

        return head


def build_from_array(array):
    if not array:
        return ListNode()

    cur = head = ListNode(array[0])
    for i in range(1, len(array)):
        cur.next = ListNode(array[i])
        cur = cur.next

    return head


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    head = build_from_array(arr1)
    print(head)

    arr2 = [1]
    head = build_from_array(arr2)
    print(head)

    arr3 = []
    head = build_from_array(arr3)
    print(head)
