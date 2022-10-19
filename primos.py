def run ():
    for i in range(100):
        # print(i)
        for j in range(i // 2 + 2):
            # print('  ' + str(j))
            if j == 1 or j == 0:
                continue
            if (i % j == 0):
                break
            if j == i//2 + 1:
                print(i)




if __name__ == '__main__':
    run()