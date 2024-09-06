def fill_if_needed(arr, index, fillvalue):
    if len(arr) <= index:
        arr += [fillvalue for i in range(index - len(arr) + 1)]
        #TODO make more efficient

def idxvals(container):# -> (int, ) #TODO learn how to make better type annotation with dtype
    sz = len(container)
    #TODO: make yield
    return [(i, container[i]) for i in range(sz)]

def idx(container):
    sz = len(container)
    return range(0,sz)

def vals_using_indices(container, indices_container):
    #TODO: make yield
    return [container[i] for i in indices_container]
