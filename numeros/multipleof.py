
def multipleof(n, m):
    ismultiple = True

    if (m % n) != 0:
        ismultiple = False

    return ismultiple



if __name__ == '__main__':
    assert multipleof(2, 6) == True
    assert multipleof(3, 5) == False
    assert multipleof(3, 9) == True
