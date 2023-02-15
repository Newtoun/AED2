class Heap:

    def montar_heap(vetor):
        heap = []
        for i in vetor:
            tam = len(heap)
            heap = Heap.aumentar_chave(heap, tam , i)
        return heap


    
    def aumentar_chave(heap, pos, novo):
        tam = len(heap)
        if pos == tam:
            heap.append(novo)
        else:
            heap[pos] = novo
        pai = (pos-1)//2
        while (pos > 0 ) and (heap[pos]<heap[pai]):
            heap[pai],heap[pos] = heap[pos],heap[pai]
            pos = pai
            pai = (pos-1)//2
        return heap

