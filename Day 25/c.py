def sort_names(names_list, reverse_order=False):
    names_list.sort(key=str.lower, reverse=reverse_order)
    return names_list
if __name__ == "__main__":
    test_names = ["Zachary", "alice", "Bob", "charlie", "Amanda"]

    print("Original list: ", test_names)
    sorted_az = sort_names(test_names.copy())
    print("Alphabetical:  ", sorted_az)
    sorted_za = sort_names(test_names.copy(), reverse_order=True)
    print("Reverse Alpha: ", sorted_za)