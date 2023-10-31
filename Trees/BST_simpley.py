def search_node_in_bst(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    if value < root.value:
        return search_node_in_bst(root.left, value)
    else:
        return search_node_in_bst(root.right, value)

# Example: Search for value 4 in the BST
if __name__ == "__main__":
    value_to_search = 4
    result = search_node_in_bst(root, value_to_search)
    print(result)  # This should print True
