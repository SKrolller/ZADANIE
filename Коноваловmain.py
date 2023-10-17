# № 1
N = int(input('Введите число: '))

for d in range(1, N // 2 + 1):
    if N % d == 0:
        print(d, ' ', sep='', end='')
print(N)


# № 2
def three_args(var1, var2, var3):
    res_dict = locals()
    print('Аргументы: ', *(f'{key} = {value}' for key, value in res_dict.items() if value))


three_args(1, None, 'asd')

# № 3
с = input()
l = len(с)
l = l // 2
for i in range(l):
    if с[i] != с[-1 - i]:
        print("It's not palindrome")
        quit()
print("It's palindrome")
input()

# ЗАДАНИЕ 4
from string import punctuation

text = '''Игрушки есть у Димы
Красивые, блестящие.
Но любит он машины,
Большие, настоящие.
В машину сам садится,
И в руки руль берёт.
Никто тогда и близко
К нему не подойдёт.
“Пойдем обедать Дима” -
Зовёт сестрёнка Аня.
А он ей из машины:
“Не буду – очень занят.“
Не нужен ему завтрак,
Обед ему не нужен.
Когда он за баранкой,
То подождёт и ужин.
Педали нажимает,
Кивает головой.
Ключи в панель вставляет -
Он лучший рулевой.
Но в день рожденья Дима
(Пошёл нам третий год!)
Забросил все машины,
Влюбился в самолёт.'''

tbl = str.maketrans('', '', punctuation)
words = text.translate(tbl).lower().split()
print(max(words, key=len))
print(max(set(words), key=lambda x: words.count(x)))

# № 5
n = int(input())
t = [[0] * n for i in range(n)]
i, j = 0, 0
for k in range(1, n * n + 1):
    t[i][j] = k
    if k == n * n: break
    if i <= j + 1 and i + j < n - 1:
        j += 1
    elif i < j and i + j >= n - 1:
        i += 1
    elif i >= j and i + j > n - 1:
        j -= 1
    elif i > j + 1 and i + j <= n - 1:
        i -= 1
for i in range(n):
    print(*t[i])

# № 6
n, m = (int(i) for i in input().split())
spiral = []
x, y, dx, dy, k = 0, 0, 1, 0, 1
spiral = [[0] * n for _ in range(m)]
for i in range(1, n * m + 1):
    spiral[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < m and 0 <= ny < n and spiral[nx][ny] == 0:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x + dx, y + dy
for i in range(n):
    for j in range(m):
        print(str(spiral[j][i]).ljust(3), end=' ')
    print()