#Reverse Sort List
def reverse_sort(list):
    ans = []
    if len(list) == 1:
        return list     #base case
    else:
        if list[0] > list[1]:
            ans = [list[0]] + reverse_sort(list[2:] + [list[1]])
        else:
            ans = [list[1]] + reverse_sort(list[2:] + [list[0]])
    return reverse_sort(ans[:-1]) + ans[-1:]

inp = list(map(int, input("Enter your List : ").split(",")))
print("List after Sorted :",reverse_sort(inp))