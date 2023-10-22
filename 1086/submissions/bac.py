def checkLimit(bac):
    """
    Check a person's blood alcohol content (BAC) level and return the corresponding legal status.

    Parameters:
    bac (float): Blood alcohol content as a percentage.

    Returns:
    str: Legal status based on BAC.
    """
    if bac < 0.08:
        print("You are free to go")
    elif 0.08 <= bac < 0.15:
        print("You have been charged with DUI")
    else:  # bac >= 0.15
        print("You are going straight to jail")

def main():
    b = float(input())
    checkLimit(b)

if __name__ == "__main__":
    main()