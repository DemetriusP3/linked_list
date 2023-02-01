class Node:
    def __init__(self):
        self.item = None
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self._start_item = Node()

    def _get_element(self, elemt):
        if self._start_item.item is None:
            return None
        else:
            node = self._start_item
            while node.item is not elemt:
                node = node.next
            return node

    def list_elements(self) -> tuple or None:
        if self._start_item.item is not None:
            node = self._start_item
            list_element = []
            while node.item is not None:
                # print(node.item)
                list_element.append(node.item)
                if node.next is not None:
                    node = node.next
                else:
                    break
            return tuple(list_element)
        else:
            return None

    def neighbors(self, elem) -> tuple or None:
        # this method printing Adjacent element
        if self._start_item.item is None:
            raise 'List is empty. Look list O_o?'
        node = self._get_element(elem)
        prev_data = node.prev.item if node.prev is not None else None
        next_data = node.next.item if node.next is not None else None

        return prev_data, next_data

    def add(self, data):
        # this method added new element to end list
        if self._start_item.item is not None:
            node = self._start_item
            while node.next is not None:
                node = node.next
            new_node = Node()
            new_node.item = data
            new_node.prev = node
            node.next = new_node
        else:
            node = self._start_item
            node.item = data

    def add_to_start(self, data):
        # this method added new element to start list
        if self._start_item.item is not None:
            node = self._start_item
            new_node = Node()
            new_node.item = data
            new_node.next = node
            self._start_item = new_node
            node.prev = new_node
        else:
            self._start_item.item = data

    def remove_element(self, elemt):
        # this method removing element
        if self._start_item.item is None:
            raise 'List is empty'
        else:
            node = self._get_element(elemt)
            prev_node = node.prev if node.prev is not None else None
            next_node = node.next if node.next is not None else None
            if prev_node is not None:
                prev_node.next = next_node
            else:
                self._start_item = next_node
            if next_node is not None:
                next_node.prev = prev_node

    def insert_element(self, pos, data):
        # this method insert element, the item will be added after the specified
        node = self._get_element(pos)
        if node is None:
            self.add(data)
            return

        next_node = node.next
        new_node = Node()
        new_node.item = data
        new_node.next = next_node
        new_node.prev = node

        node.next = new_node
        if next_node is not None:
            next_node.prev = new_node

    def replace_data(self, elemt, data):
        # this method replace element
        node = self._get_element(elemt)
        if node is not None:
            node.item = data
        else:
            raise "No replace data in empty list!"

    def clear_list(self):
        self._start_item = None
        