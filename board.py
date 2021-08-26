from random import randint
from cell import Cell


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cellMatrix = []
        self.genNumber = 1

        for row in range(rows):
            self.templist = []
            for column in range(columns):
                self.templist.append(Cell(True))
            self.cellMatrix.append(self.templist)

        self.generate()

    def drawBoard(self):
        for row in range(len(self.cellMatrix)):
            print('')
            for column in range(len(self.cellMatrix[row])):
                print(self.cellMatrix[row][column].getStatusSign(), end=" ")
        print('')

    def update(self):
        # Cell-lists for living cells to die and cells to resurrect or keep alive
        deadCellsToBecomeAlive = []
        livingCellsToBecomeDead = []

        # Check every square in the matrix
        for row in range(len(self.cellMatrix)):
            for column in range(len(self.cellMatrix[row])):

                # check neighbour pr. square:
                checkNeighbour = self.findNeighbour(row, column)
                livingNeighboursCount = []

                for neighbourCell in checkNeighbour:
                    # Check live status for neighbour cell
                    if neighbourCell.isAlive():
                        livingNeighboursCount.append(neighbourCell)

                cellObject = self.cellMatrix[row][column]  # Represents all the cell-objects in the matrix
                statusMainCell = cellObject.isAlive()  # Returns True or False

                # If the cell is alive, check the neighbour status acording to the rules:

                # Any live cell with two or three live neighbours survives.
                # Any dead cell with three live neighbours becomes a live cell.
                # All other live cells die in the next generation. Similarly, all other dead cells stay dead.

                if statusMainCell:
                    if len(livingNeighboursCount) < 2 or len(livingNeighboursCount) > 3:
                        livingCellsToBecomeDead.append(cellObject)

                    if len(livingNeighboursCount) == 3 or len(livingNeighboursCount) == 2:
                        deadCellsToBecomeAlive.append(cellObject)

                else:
                    if len(livingNeighboursCount) == 3:
                        deadCellsToBecomeAlive.append(cellObject)

        # sett cell statuses
        for cells in deadCellsToBecomeAlive:
            cells.setAlive()

        for cells in livingCellsToBecomeDead:
            cells.setDead()

        self.genNumber += 1

    def generate(self):
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                randomNumber = randint(0, 2)
                if randomNumber == 0:
                    self.cellMatrix[row][column].alive = True

    def findNeighbour(self, checkRow, checkColumn):
        """
        :param checkRow: The Cells coordinates
        :param checkColumn: The Cells coordinates
        :return: A list with all the cells neighbours
        """

        # depth of the search:
        searchMin = -1
        searchMax = 2

        # empty list to append neighbours into.
        neighbourList = []

        for row in range(searchMin, searchMax):
            for column in range(searchMin, searchMax):
                neighbourRow = checkRow + row
                neighbourColumn = checkColumn + column

                validNeighbour = True

                if neighbourRow == checkRow and neighbourColumn == checkColumn:
                    validNeighbour = False

                if neighbourRow < 0 or neighbourRow >= self.rows:
                    validNeighbour = False

                if neighbourColumn < 0 or neighbourColumn >= self.columns:
                    validNeighbour = False

                if validNeighbour:
                    neighbourList.append(self.cellMatrix[neighbourRow][neighbourColumn])

        return neighbourList

    def findAmountAlive(self):
        cellCounter = 0
        for row in range(len(self.cellMatrix)):
            for column in range(len(self.cellMatrix[row])):
                if self.cellMatrix[row][column].isAlive():
                    cellCounter += 1

        return cellCounter
