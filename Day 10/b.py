def print_reverse_pyramid(rows):
    for i in range(rows):
        spaces= " "*i
        stars= "*" * (2 * rows-i)-1
        print(spaces+stars)

print_reverse_pyramid(5)
        