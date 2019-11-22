from LRU import LRU
from Heaps import MaxHeap


def main(a):
    if a == 1:
        least_recently_used = LRU(10)

        for i in range(15):
            least_recently_used.put(i)

        print(least_recently_used)

    else:
        word_list = []
        with open("WORDS") as file:
            line = file.readline().split()
            while line:
                word_list.extend(line)
                line = file.readline().split()

        most_frequent_elements(word_list)


def most_frequent_elements(words):
    heap = MaxHeap()

    for word in words:
        heap.insert(word)

    for i in range(len(heap.tree)):
        print(str(heap.tree[i].word) + " " + str(heap.tree[i].count))


main(1)
