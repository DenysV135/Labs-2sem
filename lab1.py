
def identlims(mas):
    if len(mas) < 2:
        return (-1, -1)
    
    for i, el in enumerate(mas):
        j = i + 1
        left_break_index = 0
        found_break_left = False
        found_break_right = False
        while j < len(mas):
            if not (el < mas[j]): 
                print(f"Ліва точка розвиву: Елемент {el} (індекс {i})")
                found_break_left = True
                left_break_index = i
                break
            j += 1
        if found_break_left:
            break

    if not found_break_left and j == len(mas) and i < len(mas)-1:
        print(f"Елемент {el} (індекс {i}): Стоїть правильно (менший за всі попереду)")
        print(found_break_left)

    for i in range(len(mas) - 1, 0, -1):
        el = mas[i]
        j = 0
        right_break_index = len(mas)
        while j < i:
            if not el > mas[j]:
                print(f"Права точка розриву: Елемент {el} (індекс {i})")
                found_break_right = True
                right_break_index = i + 1
                break
            j+=1

        if found_break_right:
            break

    if not found_break_right or not found_break_left and j == len(mas) and i < len(mas)-1:
        return ( -1, -1)
    
    unsorted_part = mas[left_break_index: right_break_index]
    print(unsorted_part)
    mas[:] = unsorted_part
    return mas