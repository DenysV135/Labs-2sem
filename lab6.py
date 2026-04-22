
def min_beers(n: int, b: int, preferences_str: str) -> int:
    preferences = preferences_str.replace(" ", "")
    print(preferences)
    
    beer_masks = [0] * b
    for i in range(n):
        for j in range(b):
            if preferences[i * b + j] == 'Y':
                beer_masks[j] |= (1 << i)
                
    beer_masks = [mask for mask in beer_masks if mask > 0]
    
    b_effective = len(beer_masks)
    target_mask = (1 << n) - 1
    
    suffix_or = [0] * b_effective
    curr_or = 0
    for i in range(b_effective - 1, -1, -1):
        curr_or |= beer_masks[i]
        suffix_or[i] = curr_or

    min_selected = float('inf')

    def dfs(beer_index: int, current_mask: int, selected_count: int):
        nonlocal min_selected

        if current_mask == target_mask:
            min_selected = min(min_selected, selected_count)
            return

        if beer_index == b_effective:
            return
            
        if selected_count >= min_selected - 1:
            return
            
        if (current_mask | suffix_or[beer_index]) != target_mask:
            return

        new_mask = current_mask | beer_masks[beer_index]
        if new_mask != current_mask:
            dfs(beer_index + 1, new_mask, selected_count + 1)

        dfs(beer_index + 1, current_mask, selected_count)

    dfs(0, 0, 0)
    return min_selected