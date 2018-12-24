def get_even_list(l):
    even_list = []
    for num in l:
        if num % 2 == 0:
            even_list.append(num)
    return(even_list)

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

            