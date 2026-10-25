from abc import ABC, abstractmethod


class Order:
    """Representa un pedido: cliente y cantidad de producto."""

    def __init__(self, qtty, customer):
        self.__customer = customer
        self.__qtty = qtty

    def print(self):
        print("      Customer: " + self.getCustomer())
        print("      Quantity: " + str(self.getQtty()))
        print("      ------------")

    def getQtty(self):
        return self.__qtty

    def getCustomer(self):
        return self.__customer


class QueueInterface(ABC):
    @abstractmethod
    def size(self):
        """Devuelve el número de elementos de la cola."""

    @abstractmethod
    def isEmpty(self):
        """True si la cola está vacía, False si no."""

    @abstractmethod
    def front(self):
        """Devuelve el primer elemento SIN borrarlo. None si está vacía."""

    @abstractmethod
    def enqueue(self, info):
        """Añade un nuevo elemento a la cola."""

    @abstractmethod
    def dequeue(self):
        """Devuelve el primer elemento y LO BORRA. None si está vacía."""


class Node:
    """Nodo de la lista enlazada."""

    def __init__(self, info):
        self.__info = info    # objeto que realmente contiene el nodo
        self.__next = None    # siguiente nodo (None si es el último)

    def getNext(self):
        return self.__next

    def setNext(self, next_node):
        self.__next = next_node

    def getInfo(self):
        return self.__info

    def setInfo(self, info):
        self.__info = info


class Queue(QueueInterface):
    """Cola FIFO implementada con una lista enlazada."""

    def __init__(self):
        self.__top = None     # cabeza: de aquí se extrae
        self.__tail = None    # final: aquí se inserta
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__top is None

    def front(self):
        if self.isEmpty():
            return None
        return self.__top.getInfo()

    def enqueue(self, info):
        new_node = Node(info)
        if self.isEmpty():
            self.__top = new_node             # primer elemento: cabeza y final
        else:
            self.__tail.setNext(new_node)    # enlazamos tras el último nodo
        self.__tail = new_node                # el nuevo nodo pasa a ser el último
        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        info = self.__top.getInfo()
        self.__top = self.__top.getNext()    # avanzamos la cabeza
        if self.__top is None:
            self.__tail = None                # la cola se ha vaciado
        self.__size -= 1
        return info

    # Ejercicio 2: n-ésimo elemento (1 = primero) sin borrarlo.
    # Devuelve None si la posición no es válida.
    def getNth(self, nth):
        if nth < 1 or nth > self.__size:
            return None
        node = self.__top
        for _ in range(nth - 1):
            node = node.getNext()
        return node.getInfo()

    def printInfo(self):
        print("********* QUEUE DUMP *********")
        print("   Size: " + str(self.__size))
        node = self.__top
        i = 1
        while node is not None:
            print("   ** Element " + str(i))
            node.getInfo().print()
            node = node.getNext()
            i += 1
        print("******************************")


class TestQueue:
    @staticmethod
    def main():
        # ---------- Ejercicio 1 ----------
        queue = Queue()

        print(">> Cola recién creada")
        queue.printInfo()

        print("\n>> enqueue de 4 pedidos (printInfo tras cada inserción)")
        for qtty, customer in [(20, "cust1"), (30, "cust2"), (40, "cust3"), (50, "cust3")]:
            queue.enqueue(Order(qtty, customer))
            queue.printInfo()

        print("\n>> front (no borra)")
        queue.front().print()
        queue.printInfo()

        print("\n>> dequeue (borra el primero)")
        queue.dequeue().print()
        queue.printInfo()

        print("\n>> dequeue hasta vaciar la cola")
        while not queue.isEmpty():
            queue.dequeue()
            queue.printInfo()
        print("front en cola vacía:", queue.front())
        print("dequeue en cola vacía:", queue.dequeue())

        # ---------- Ejercicio 2 ----------
        print("\n>> Ejercicio 2: introducir 4 elementos y obtener el tercero")
        queue2 = Queue()
        queue2.enqueue(Order(20, "cust1"))
        queue2.enqueue(Order(30, "cust2"))
        queue2.enqueue(Order(40, "cust3"))
        queue2.enqueue(Order(50, "cust4"))
        print("Elemento 3:")
        queue2.getNth(3).print()
        print("Elemento 0 ->", queue2.getNth(0))
        print("Elemento 99 ->", queue2.getNth(99))
        queue2.printInfo()   # sigue igual: getNth no borra


if __name__ == "__main__":
    TestQueue.main()