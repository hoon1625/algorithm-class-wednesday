items = [
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4)
]

n = len(items)

W = int(input("배낭 용량을 입력 하세요 : "))

A = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    name, wt, val = items[i - 1]
    for w in range(1, W + 1):
        if wt > w:
            A[i][w] = A[i - 1][w]
        else:
            A[i][w] = max(
                A[i - 1][w],
                val + A[i - 1][w - wt]
            )

max_value = A[n][W]

selected_items = []
w = W

for i in range(n, 0, -1):
    if A[i][w] != A[i - 1][w]:
        name, wt, val = items[i - 1]
        selected_items.append(name)
        w -= wt

selected_items.reverse()

print(f"최대 만족도: {max_value}")
print(f"선택된 물건: {selected_items}")