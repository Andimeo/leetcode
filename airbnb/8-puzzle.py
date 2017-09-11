import heapq


def hamming(x, y, board, step):
    # (x - 2) ** 2 + (y - 2) ** 2  # (3 - x) ** 2 + (3 - y) ** 2
    return sum([1 for i, x in enumerate(board) if (i + 1) != int(x) and x != '0']) + step


def manhattan(x, y, board, step):
    result = 0
    for i, c in enumerate(board):
        if c != '0':
            c = int(c)
            result += abs(c // 3 - i // 3) + abs(c % 3 - i % 3)
    return result + step


dis = hamming


def move(board, x, y, nx, ny):
    b = list(board)
    b[x * 3 + y], b[nx * 3 + ny] = b[nx * 3 + ny], b[x * 3 + y]
    return ''.join(b)


def is_valid(board):
    inversion_num = 0
    for i in range(1, len(board)):
        for j in range(i):
            if board[i] == '0' or board[j] == '0':
                continue
            if board[j] > board[i]:
                inversion_num += 1
    if inversion_num % 2 == 1:
        return False
    return True


def play(board):
    n, m = len(board), len(board[0])
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '0':
                x, y = i, j
    visited = set()
    init_board = ''.join(''.join(board[i]) for i in range(n))
    if not is_valid(init_board):
        return False
    heap = [(dis(x, y, init_board, 0), x, y, init_board, 0)]
    while heap:
        _, x, y, cur, step = heapq.heappop(heap)
        if cur in visited:
            continue
        visited.add(cur)
        if cur == '123456780':
            return step
        for dx, dy in zip((1, -1, 0, 0), (0, 0, -1, 1)):
            if 0 <= x + dx < n and 0 <= y + dy < m:
                new_board = move(cur, x, y, x + dx, y + dy)
                heapq.heappush(heap, (dis(x + dx, y + dy, new_board, step), x + dx, y + dy, new_board, step + 1))

    return False


import time

b = time.time()
print(play(
    [
        ['1', '2', '3'],
        ['4', '8', '5'],
        ['7', '6', '0']
    ]
))
print(time.time() - b)

b = time.time()
print(play(
    [
        ['5', '6', '7'],
        ['4', '0', '8'],
        ['3', '2', '1']
    ]
))
print(time.time() - b)
