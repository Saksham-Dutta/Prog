def max_frequency_manual(arr):
    if not arr:
        return None
    frequency_map={}
    for num in arr:
        frequency_map[num]=frequency_map.get(num,0)+1
    most_frequent=max(frequency_map,key=frequency_map.get)
    highest_count=frequency_map[most_frequent]
    return most_frequent,highest_count
