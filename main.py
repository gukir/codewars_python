def snail(snail_map):
    if not snail_map:
        return []
    else:
        return snail_map[0]+snail(list(map(list, zip(*(snail_map[1:]))))[::-1])
