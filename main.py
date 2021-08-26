from board import Board


def main():
    rows = int(input('Enter amount of rows: '))
    columns = int(input('Enter amount of columns: '))

    board = Board(rows, columns)
    board.drawBoard()
    print(f'Generation: {board.genNumber}. Amount of living cells: {board.findAmountAlive()}')
    print('')

    while True:
        user = input('Press enter to continue and q to exit')
        if user == '':
            board.update()
            board.drawBoard()
            print(f'Generation: {board.genNumber}. Amount of living cells: {board.findAmountAlive()}')
            print('')
        elif user == 'q':
            break


if __name__ == "__main__":
    main()
