def listoverlap(list1, list2):
    overlaplist = []
    for number in list1:
        if number in list2:
            if number in overlaplist:
                pass
            else:
                overlaplist.append(number)
    return overlaplist


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(listoverlap(a, b))
    return


if __name__ == '__main__':
    main()
