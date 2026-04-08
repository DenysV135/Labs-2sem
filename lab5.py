
def min_knight_steps(N, src, dest):
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    q = [(src[0], src[1], 0)]

    visited = set()
    visited.add((src[0], src[1]))

    while q:
        x, y, dist = q.pop(0)

        if x == dest[0] and y == dest[1]:
            return dist

        for i in range(8):
            nx = x + row[i]
            ny = y + col[i]

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, dist + 1))

    return -1

def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            N = int(lines[0].strip())
            src_x, src_y = map(int, lines[1].strip().split())
            dest_x, dest_y = map(int, lines[2].strip().split())
            
            src = (src_x, src_y)
            dest = (dest_x, dest_y)

        result = min_knight_steps(N, src, dest)

        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f"Мінімальна кількість кроків, яку має пройти кінь для приходу \
в місце призначення: \"{str(result)}\"")

        print(f"Мінімальна кількість кроків ({result}) записана у файл output.txt")

    except FileNotFoundError:
        print("Помилка: Файл 'input.txt' не знайдено. Cтворіть його у тій самій папці.")
    except Exception as e:
        print(f"Виникла помилка при обробці: {e}")

if __name__ == '__main__':
    main()