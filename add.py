from main import zigzag


def main():
    n, m = map(int, input("Введіть розмір масиву n та m через пробіл: ").split())
    matrix = []
    print(f"Введіть матрицю ({n} рядків по {m} чисел):")
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    k = int(input("Введіть k (скільки перших елементів порахувати): "))
    stream = zigzag(matrix)
    total_sum = sum(stream[:k])

    print(total_sum)


if __name__ == "__main__":
    main()