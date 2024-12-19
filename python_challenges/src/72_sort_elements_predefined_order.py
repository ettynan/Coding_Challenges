def sort_by_predefined_order(lst, predefined_order):
    order_map = {val: idx for idx, val in enumerate(predefined_order)}
    return sorted(lst, key=lambda x: order_map.get(x, float('inf')))

# Example usage:
lst = ['apple', 'banana', 'orange', 'grape']
predefined_order = ['orange', 'apple', 'grape']
print("Sorted List:", sort_by_predefined_order(lst, predefined_order))
