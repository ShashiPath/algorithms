def sliding_window(input_data, window_size):
    n = len(input_data)
    traversed_nodes = []
    final_output = []
    
    for i in range(0, n, window_size):
        window = input_data[i:i+window_size]
        traversed_nodes.append(window)
        final_output.extend(window)
    
    return traversed_nodes, final_output

def sliding_window_with_data_loss(input_data, window_size, loss_indices):
    n = len(input_data)
    traversed_nodes = []
    final_output = []
    lost_nodes = []

    # First pass - simulate data loss
    for i in range(0, n, window_size):
        window = input_data[i:i+window_size]
        traversed_nodes.append(window)
        if i not in loss_indices:
            final_output.extend(window)
        else:
            lost_nodes.append(window)

    # Second pass - re-address lost nodes
    for window in lost_nodes:
        final_output.extend(window)

    return traversed_nodes, final_output

input_string = [8, 8, 7, 7, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1]
loss_indices = [4, 10, 18]  # Indices where data loss occurs

print("Best case scenario (no data loss):")
traversed_nodes_best, final_output_best = sliding_window(input_string, 2)
print("Traversed nodes:", traversed_nodes_best)
print("Final traversed output:", final_output_best)

print("\nScenario with some data loss and re-addressing lost nodes:")
traversed_nodes_loss, final_output_loss = sliding_window_with_data_loss(input_string, 2, loss_indices)
print("Traversed nodes:", traversed_nodes_loss)
print("Final traversed output:", final_output_loss)
