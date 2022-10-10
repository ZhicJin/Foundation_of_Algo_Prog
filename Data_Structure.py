# DATA STRUCTURE
# Node to store x, y coordinates of the point.
import random
import math
class node:
    def __init__(self):
        self.x = None
        self.y = None

# Pairnode to store x, y, and distance of the pair of points.
class pairnode:
    def __init__(self, x1, x2):
        self.distance = None
        self.next = None
        self.read_data(x1, x2)

    def read_data(self, x1, x2):
        self.pair = [[x1.x, x1.y], [x2.x, x2.y]]
        self.distance = distance(x1, x2)

# autosort_list is a linked list of pairnodes with size limited to m.
class autosort_list:
    def __init__(self, m):
        self.size = m
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def delete_tail(self):
        if self.is_empty():
            raise Exception("The list is empty, can not delete the tail!")
        i = 0
        pre_node = None
        curr_node = self.head
        while curr_node.next != None:
            pre_node = curr_node
            curr_node = curr_node.next
        pre_node.next = None
        self.tail = pre_node
        self.length -= 1
        return

    def length(self):
        return self.length

    def __iter__(self):

        current = self.head

        while current is not None:
            yield current

            current = current.next

    def insert(self, pairnode):
        if self.is_empty():
            self.head = pairnode
            self.tail = pairnode
            self.length += 1

        else:
            pre_node = None
            curr_node = self.head
            while curr_node != None:
                if pairnode.pair == curr_node.pair:
                    break
                if pairnode.distance >= curr_node.distance and curr_node.next != None:
                    pre_node = curr_node
                    curr_node = curr_node.next
                elif pairnode.distance >= curr_node.distance and curr_node.next == None:
                    curr_node.next = pairnode
                    self.tail = pairnode
                    self.length += 1
                    break
                else:
                    if pre_node == None:
                        pairnode.next = self.head
                        self.head = pairnode
                        self.length += 1
                        break
                    else:
                        pairnode.next = pre_node.next
                        pre_node.next = pairnode
                        self.length += 1
                        break
            if self.length > self.size:
                self.delete_tail()

        return

    def minimum(self):
        return self.head.distance

    def maximum(self):
        return self.tail.distance

# sort by x using insertion sort
def mergesort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergesort(L)

        # Sorting the second half
        mergesort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].x <= R[j].x:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def read_input(filename):
    points_list = list()
    with open(filename, "r") as f:
        line_num = 1
        for line in f:
            elements = line.split()
            if len(elements) != 2:
                raise Exception("Line %i is not qualified points." % line_num)
            if isfloat(elements[0]) or isint(elements[0]):
                if isfloat(elements[1]) or isint(elements[1]):
                    xy = [eval(i) for i in elements]
                    point_node = node()
                    point_node.x = xy[0]
                    point_node.y = xy[1]
                    points_list.append(point_node)
                else:
                    raise Exception("Line %i contains non-numeric value." % line_num)
            else:
                raise Exception("Line %i contains non-numeric value." % line_num)
            line_num += 1
    return points_list


def distance(A, B):
    dist = 0
    dist = math.sqrt(((A.x - B.x) ** 2) + ((A.y - B.y) ** 2))
    return dist


def findmin(list_n):
    min_node = list_n[0]
    mindist = min_node.distance
    for item in list_n:
        if item.distance < mindist:
            min_node = item
            mindist = min_node.distance
    return min_node


def ClosestPair(PX, m_list):
    n = len(PX)
    if n == 2:
        pair_node = pairnode(PX[0], PX[1])
        m_list.insert(pair_node)

        return m_list.tail
    if n == 3:
        pair_node_1 = pairnode(PX[0], PX[1])
        m_list.insert(pair_node_1)
        pair_node_2 = pairnode(PX[1], PX[2])
        m_list.insert(pair_node_2)
        pair_node_3 = pairnode(PX[0], PX[2])
        m_list.insert(pair_node_3)

        return m_list.tail
    mid = math.ceil(n / 2)
    left = ClosestPair(PX[:mid], m_list)
    right = ClosestPair(PX[mid:], m_list)
    min_node = m_list.tail

    d = min_node.distance
    list_gn = []
    list_pn = []
    for item in PX:
        if item.x <= PX[mid].x + d and item.x >= PX[mid].x - d:
            list_gn.append(item)
    if len(list_gn) > 1:
        for i in range(len(list_gn)):
            for j in range(1, len(list_gn) - i, 1):
                m_list.insert(pairnode(list_gn[i], list_gn[i + j]))
    return m_list


def M_Closest_Pair(P, m):
    PX = mergesort(P)
    m_list = autosort_list(m)
    m_list = ClosestPair(PX, m_list)

    return m_list


def create_100_random_points(filename):
    x = list()
    y = list()
    f = open(filename, "w")
    for i in range(100):
        item = random.randint(1,100)
        x.append(item)
    for i in range(100):
        item = random.randint(1,100)
        y.append(item)
    for index in range(100):
        f.write(str(x[index])+"\t"+str(y[index]) + "\n")

    f.close()
    return
