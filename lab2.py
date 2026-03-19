
def calcut(numb, width, height):
    if width > height:
        bigger = width
    else:
        bigger = height

    left = bigger
    right = bigger * numb
    i = 0
    while left < right:
        mid = (left + right) // 2
        fit = (mid // width) * (mid // height)
        i += 1
        if fit >= numb:
            right = mid
        else:
            left = mid + 1

    print(f"Для {numb} листків розміром: {width}x{height} ідеальний квадрат має сторону: {left} \
, кількість ітерацій: {i}")
    return left

if __name__ == "__main__":
    numb, width, height = map(int, input("Введіть скільки, ширину, і висоту відповідно: ").split())
    calcut(numb, width, height)