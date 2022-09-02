def reverse_iter(head):
    if not head or not head.next:
        return head

    pre = None
    while head:
        cur = head
        head = head.next
        cur.next = pre
        pre = cur

    return pre


def reverse_recur(head):
    if not head or not head.next:
        return head

    last = self.reverse_recur(head.next)
    head.next.next = head
    head.next = None
    return last
