def inRange(test_list,i,j):
    for ele in test_list:
            if ele < i or ele > j :
                    return False

    return True   

def main():   
    test_list = list(map(int, input().split()))
    [i,j] = list(map(int, input().split()))
    res = inRange(test_list,i,j)
    if res:
        print('yes')
    else:
        print('no')

             
main()