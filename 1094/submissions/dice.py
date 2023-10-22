def dice(num):
    for i in range(6):
        n1 = i + 1
        for j in range(6):
            n2 = j + 1
            total = n1 + n2
            if(total % num == 0):
                print(n1, n2)


def main():
    n = int(input())
    dice(n)

if __name__ == "__main__":
    main()