import sys
print("        DISCRETE MATH. PROJECT №5. HAYDA A. LEBYAK O. HRYTSIV T.")
print("                               TASK:")
print("   Build all lexicographic permutations with numbers in ",
      "set {1,2,3...,n}")
print("                           INSTRUCTIONS:")
print("You have to enter 'n', what is the last element in the set")
print("                              RESULT:")
print("The result would be all permutations in the set you've entered")


def lexicographic_order(lst, index):
    """
    (list, int) -> list
    This function returns lists with lexicographic order for all numbers in
    'lst'. The changes start from the 'index' point
    >>> lexicographic_order([1, 2, 3],0)
    [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3]
    [2, 3, 1]
    [3, 1, 2]
    [3, 2, 1]
    >>> lexicographic_order([1, 2, 3, 4],0)
    [1, 2, 3, 4]
    [1, 2, 4, 3]
    [1, 3, 2, 4]
    [1, 3, 4, 2]
    [1, 4, 2, 3]
    [1, 4, 3, 2]
    [2, 1, 3, 4]
    [2, 1, 4, 3]
    [2, 3, 1, 4]
    [2, 3, 4, 1]
    [2, 4, 1, 3]
    [2, 4, 3, 1]
    [3, 1, 2, 4]
    [3, 1, 4, 2]
    [3, 2, 1, 4]
    [3, 2, 4, 1]
    [3, 4, 1, 2]
    [3, 4, 2, 1]
    [4, 1, 2, 3]
    [4, 1, 3, 2]
    [4, 2, 1, 3]
    [4, 2, 3, 1]
    [4, 3, 1, 2]
    [4, 3, 2, 1]
    """
    if index == len(lst)-1:
        print(lst)
        return
    for i in range(index, len(lst)):
        new_lst = lst[:]  # all elements from lst are copied to 'new_lst'
        temporary = new_lst.pop(i)  # removing an element from the list and
        # giving it a value of a temporary variable
        new_lst.insert(index, temporary)  # inserts temporary variable in the
        # specific place
        lexicographic_order(new_lst, index+1)  # using recursion to do the same
        # with next index

try:
    end = int(input("Enter the range. From 1 to "))  # End of the set
except ValueError:
    print("You've entered not an integer number.")
    sys.exit(1)
start = 1  # Start point of the set
a = list(range(start, int(end)+1))  # Range of the set
print("The set is ", set(a))
lexicographic_order(a, 0)  # Calling a function, which returns
# lexicographic order
