def new_in_list(my_list, idx, element):
    rep = my_list[:]
    if idx >= 0 and idx < len(rep):
        rep[idx] = element
    return rep
