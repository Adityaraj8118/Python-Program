def pyramid_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
rows = 5
pyramid_pattern(rows)
