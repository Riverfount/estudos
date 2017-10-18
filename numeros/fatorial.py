def fat(num):
    if num == 1:
        return 1
    else:
        return (num * fat(num - 1))


if __name__ == '__main__':
    print(f'O fatorial de 15 é {fat(15)}')
