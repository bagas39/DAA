def generate_permutations(arr):
    result = []
    
    def backtrack(start_index):
        if start_index == len(arr):
            result.append(arr[:])
            return
            
        for i in range(start_index, len(arr)):
            arr[start_index], arr[i] = arr[i], arr[start_index]
            backtrack(start_index + 1)
            arr[start_index], arr[i] = arr[i], arr[start_index]
            
    backtrack(0)
    return result

def tsp_brute_force(distances):
    n = len(distances)
    start_node = 0
    nodes_to_visit = [i for i in range(1, n)]
    
    min_distance = float('inf')
    best_routes = []
    all_evaluations = [] 
    
    all_permutations = generate_permutations(nodes_to_visit)
    
    for current_route in all_permutations:
        current_distance = 0
        current_node = start_node
        
        for next_node in current_route:
            current_distance += distances[current_node][next_node]
            current_node = next_node
            
        current_distance += distances[current_node][start_node]
        
        full_route = [start_node] + current_route + [start_node]
        
        all_evaluations.append((full_route, current_distance))
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_routes = [full_route]
        elif current_distance == min_distance:
            best_routes.append(full_route)
            
    return all_evaluations, best_routes, min_distance

if __name__ == "__main__":
    matrix_jarak = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    semua_evaluasi, rute_optimal, jarak_min = tsp_brute_force(matrix_jarak)
    
    print("=== Seluruh Kemungkinan Rute ===")
    for idx, (rute, jarak) in enumerate(semua_evaluasi, 1):
        rute_str = ' -> '.join(map(str, rute))
        print(f"Percobaan {idx}: Rute [{rute_str}] | Total Jarak = {jarak}")
        
    print("\n=== Hasil Optimal ===")
    print(f"Total Jarak Minimum: {jarak_min}")
    print("Rute Pilihan:")
    for idx, rute in enumerate(rute_optimal, 1):
        rute_str = ' -> '.join(map(str, rute))
        print(f"{idx}. {rute_str}")