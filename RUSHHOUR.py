import copy
from timeit import default_timer as timer
from queue import Queue
from queue import PriorityQueue
from queue import LifoQueue
import contextlib

import numpy as np


def solutionAndBoard(problemNum):
    if problemNumber > -1:
        if 1 >= problemNumber < 11:
            for tiles in lines[pos1:pos2 + 1]:
                print(tiles.strip('\n'))
        elif problemNumber == 11:
            for tiles in lines[pos1 + 1:pos2 + 2]:
                print(tiles.strip('\n'))
        elif problemNumber == 12:
            for tiles in lines[pos1 + 1: pos2 + 3]:
                print(tiles.strip('\n'))
        elif problemNumber == 13:
            for tiles in lines[pos1 + 1: pos2 + 2]:
                print(tiles.strip('\n'))
        elif 14 >= problemNumber < 15:
            for tiles in lines[pos1 + 1:pos2 + 2]:
                print(tiles.strip('\n'))
        elif problemNumber == 15:
            for tiles in lines[pos1 + 2:pos2 + 4]:
                print(tiles.strip('\n'))
        elif problemNumber == 16:
            for tiles in lines[pos1 + 3:pos2 + 5]:
                print(tiles.strip('\n'))
        elif problemNumber == 17:
            for tiles in lines[pos1 + 4:pos2 + 6]:
                print(tiles.strip('\n'))
        elif problemNumber == 18:
            for tiles in lines[pos1 + 5:pos2 + 7]:
                print(tiles.strip('\n'))
        elif problemNumber == 19:
            for tiles in lines[pos1 + 6:pos2 + 8]:
                print(tiles.strip('\n'))
        elif problemNumber == 20:
            for tiles in lines[pos1 + 7:pos2 + 9]:
                print(tiles.strip('\n'))
        elif problemNumber == 21:
            for tiles in lines[pos1 + 7:pos2 + 9]:
                print(tiles.strip('\n'))
        elif problemNumber == 22:
            for tiles in lines[pos1 + 8:pos2 + 10]:
                print(tiles.strip('\n'))
        elif problemNumber == 23:
            for tiles in lines[pos1 + 9:pos2 + 11]:
                print(tiles.strip('\n'))
        elif problemNumber == 24:
            for tiles in lines[pos1 + 10:pos2 + 12]:
                print(tiles.strip('\n'))
        elif problemNumber == 25:
            for tiles in lines[pos1 + 11:pos2 + 13]:
                print(tiles.strip('\n'))
        elif problemNumber == 26:
            for tiles in lines[pos1 + 12:pos2 + 14]:
                print(tiles.strip('\n'))
        elif problemNumber == 27:
            for tiles in lines[pos1 + 13:pos2 + 15]:
                print(tiles.strip('\n'))
        elif problemNumber == 28:
            for tiles in lines[pos1 + 14:pos2 + 16]:
                print(tiles.strip('\n'))
        elif problemNumber == 29:
            for tiles in lines[pos1 + 15:pos2 + 17]:
                print(tiles.strip('\n'))
        elif problemNumber == 30:
            for tiles in lines[pos1 + 16:pos2 + 19]:
                print(tiles.strip('\n'))
        elif problemNumber == 31:
            for tiles in lines[pos1 + 18:pos2 + 20]:
                print(tiles.strip('\n'))
        elif problemNumber == 32:
            for tiles in lines[pos1 + 20:pos2 + 21]:
                print(tiles.strip('\n'))
        elif problemNumber == 33:
            for tiles in lines[pos1 + 22:pos2 + 25]:
                print(tiles.strip('\n'))
        elif problemNumber == 34:
            for tiles in lines[pos1 + 24:pos2 + 27]:
                print(tiles.strip('\n'))
        elif problemNumber == 35:
            for tiles in lines[pos1 + 26:pos2 + 29]:
                print(tiles.strip('\n'))
        elif problemNumber == 36:
            for tiles in lines[pos1 + 28:pos2 + 31]:
                print(tiles.strip('\n'))
        elif problemNumber == 37:
            for tiles in lines[pos1 + 30:pos2 + 33]:
                print(tiles.strip('\n'))
        elif problemNumber == 38:
            for tiles in lines[pos1 + 33:pos2 + 37]:
                print(tiles.strip('\n'))
        elif problemNumber == 39:
            for tiles in lines[pos1 + 36:pos2 + 39]:
                print(tiles.strip('\n'))
        elif problemNumber == 40:
            for tiles in lines[pos1 + 39:pos2 + 43]:
                print(tiles.strip('\n'))
        else:
            print("<Not in range... try again.>")


def strToBoard(problem):
    global br
    board = []
    for i in range(6):
        for i in range(6):
            if i == 0:
                br = []

            br.append(problem[0])
            problem = problem[1:]

            if i == 5:
                board.append(br)
    return board


def getOrientation(board):
    Hcars = set()
    Vcars = set()
    Htrucks = set()
    Vtrucks = set()

    boardCount = np.array(board)
    carsOnBoard, carCounters = np.unique(boardCount, return_counts=True)

    truckList = ['O', 'P', 'Q', 'R']
    carList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'X' ]

    carsOnBoard = carsOnBoard[1:]
    carCounters = carCounters[1:]
    print(carCounters)
    for i, v in enumerate(carCounters):
        # add car to list per their count

        if v >= 1 and carsOnBoard[i] in carList:
            Hcars.add(i)
        elif v >= 1 and carsOnBoard[i] in truckList:
            Htrucks.add(i)
        elif v >= 2 and carsOnBoard[i] in carList:
            Vcars.add(i)
        elif v >= 2 and carsOnBoard[i] in truckList:
            Vtrucks.add(i)

    #
    #
    # for i in board:
    #     # print(i)
    #     As = i.count("A")
    #     Bs = i.count("B")
    #     Cs = i.count("C")
    #     Ds = i.count("D")
    #     Es = i.count("E")
    #     Fs = i.count("F")
    #     Gs = i.count("G")
    #     Hs = i.count("H")
    #     Is = i.count("I")
    #     Js = i.count("J")
    #     Ks = i.count("K")
    #     Xs = i.count("X")
    #     Os = i.count("O")
    #     Ps = i.count("P")
    #     Qs = i.count("Q")
    #     Rs = i.count("R")
    #
    #     if As >= 2:
    #         Hcars.add("A")
    #     elif As >= 1:
    #         Vcars.add("A")
    #     if Bs >= 2:
    #         Hcars.add("B")
    #     elif Bs >= 1:
    #         Vcars.add("B")
    #     if Cs >= 2:
    #         Hcars.add("C")
    #     elif Cs >= 1:
    #         Vcars.add("C")
    #     if Ds >= 2:
    #         Hcars.add("D")
    #     elif Ds >= 1:
    #         Vcars.add("D")
    #     if Es >= 2:
    #         Hcars.add("E")
    #     elif Es >= 1:
    #         Vcars.add("E")
    #     if Fs >= 2:
    #         Hcars.add("F")
    #     elif Fs >= 1:
    #         Vcars.add("F")
    #     if Gs >= 2:
    #         Hcars.add("G")
    #     elif Gs >= 1:
    #         Vcars.add("G")
    #     if Hs >= 2:
    #         Hcars.add("H")
    #     elif Hs >= 1:
    #         Vcars.add("H")
    #     if Is >= 2:
    #         Hcars.add("I")
    #     elif Is >= 1:
    #         Vcars.add("I")
    #     if Js >= 2:
    #         Hcars.add("J")
    #     elif Js >= 1:
    #         Vcars.add("J")
    #     if Ks >= 2:
    #         Hcars.add("K")
    #     elif Ks >= 1:
    #         Vcars.add("K")
    #     if Xs == 2:
    #         Hcars.add("X")
    #
    #     if Os >= 2:
    #         Htrucks.add("O")
    #     elif Os >= 1:
    #         Vtrucks.add("O")
    #     if Ps >= 2:
    #         Htrucks.add("P")
    #     elif Ps >= 1:
    #         Vtrucks.add("P")
    #     if Qs >= 2:
    #         Htrucks.add("Q")
    #     elif Qs >= 1:
    #         Vtrucks.add("Q")
    #     if Rs >= 2:
    #         Htrucks.add("R")
    #     elif Rs >= 1:
    #         Vtrucks.add("R")
    return Hcars, Vcars, Vtrucks, Htrucks


def sqrBoard(problemNum):
    if 1 >= problemNumber <= 40:
        for i in range(6):
            for j in range(6):
                print(board[i][j], end='')
            print()
    else:
        print("<Not in range>")
    print()


def checkBF(board):
    # checks a boards blocking factor
    bf = 0
    if board[2][2] != EMPTY_SPACE and board[2][2] != 'X':
        bf += 1
    if board[2][3] != EMPTY_SPACE and board[2][3] != 'X':
        bf += 1
    if board[2][4] != EMPTY_SPACE and board[2][4] != 'X':
        bf += 1
    if board[2][5] != EMPTY_SPACE and board[2][5] != 'X':
        bf += 1

    return bf


def cloneBoard(board):
    # return [_[:] for _ in board]
    return copy.deepcopy(board)


def checkWin(board):
    if board[2][5] == 'X':
        return True

    return False


def moveVertical(States, board, c, car, r):
    # if truck
    if car in vertTrucks:
        if (r - 1) >= 0 and (r + 2) < N:  # move up
            if board[r - 1][c] == EMPTY_SPACE:
                localBoardTU = cloneBoard(board)
                localBoardTU[r - 1][c], localBoardTU[r + 2][c] = car, EMPTY_SPACE
                move = f'{car}U1'
                parent = cloneBoard(board)
                bf = checkBF(localBoardTU)
                States.append((localBoardTU, move, bf, parent))
                # totalBoards.append((localBoardTU, move, bf, parent))

        if (r + 1) < N and (r - 2) >= 0:  # move down
            if board[r + 1][c] == EMPTY_SPACE:
                localBoardTD = cloneBoard(board)
                localBoardTD[r - 2][c], localBoardTD[r + 1][c] = EMPTY_SPACE, car
                move = f'{car}D1'
                parent = cloneBoard(board)
                bf = checkBF(localBoardTD)
                States.append((localBoardTD, move, bf, parent))
                # totalBoards.append((localBoardTD, move, bf, parent))

    # if car
    if car in vertCars:
        if (r - 1) >= 0 and (r + 1) < N:  ## move down
            if board[r - 1][c] == EMPTY_SPACE:
                localBoardCD = cloneBoard(board)
                localBoardCD[r - 1][c], localBoardCD[r + 1][c] = car, EMPTY_SPACE
                move = f'{car}D1'
                parent = cloneBoard(board)
                bf = checkBF(localBoardCD)
                States.append((localBoardCD, move, bf, parent))
                # totalBoards.append((localBoardCD, move, bf, parent))

        if (r + 1) < N and (r - 1) >= 0:  ## move up
            if board[r + 1][c] == EMPTY_SPACE:
                localBoardCU = cloneBoard(board)
                localBoardCU[r - 1][c], localBoardCU[r + 1][c] = EMPTY_SPACE, car
                move = f'{car}U1'
                parent = cloneBoard(board)
                bf = checkBF(localBoardCU)
                States.append((localBoardCU, move, bf, parent))
                # totalBoards.append((localBoardCU, move, bf, parent))


def moveHorizontal(States, board, c, car, r):
    # Left - Car
    if car in horCars:
        if c + 1 < N and c - 1 >= 0:
            if board[r][c + 1] == EMPTY_SPACE:  # check right
                localBoardCR = cloneBoard(board)
                localBoardCR[r][c - 1], localBoardCR[r][c + 1] = EMPTY_SPACE, car
                move = f'{car}R1'
                parent = cloneBoard(board)
                bf = checkBF(localBoardCR)
                States.append((localBoardCR, move, bf, parent))
                # totalBoards.append((localBoardCR, move, bf, parent))

        if (c - 1) >= 0 and (c + 1) < N:
            if board[r][c - 1] == EMPTY_SPACE:  # check left
                localBoardCL = cloneBoard(board)
                localBoardCL[r][c - 1], localBoardCL[r][c + 1] = car, EMPTY_SPACE
                move = f'{car}L1'
                parent = cloneBoard(board)
                bf = checkBF(localBoardCL)
                States.append((localBoardCL, move, bf, parent))
                # totalBoards.append((localBoardCL, move, bf, parent))

    # Left - Truck
    if car in horTrucks:
        if (c + 1) < N and (c - 2) >= 0:
            if board[r][c + 1] == EMPTY_SPACE:  # check right
                localBoardTR = cloneBoard(board)
                localBoardTR[r][c - 2], localBoardTR[r][c + 1] = EMPTY_SPACE, car
                move = f'{car}R1'
                parent = cloneBoard(board)
                bf = checkBF(localBoardTR)
                States.append((localBoardTR, move, bf, parent))
                # totalBoards.append((localBoardTR, move, bf, parent))

        if (c - 1) >= 0 and (c + 2) < N:
            if board[r][c - 1] == EMPTY_SPACE:  # check left
                localBoardTL = cloneBoard(board)
                localBoardTL[r][c - 1], localBoardTL[r][c + 2] = car, EMPTY_SPACE
                move = f'{car}L1'
                parent = cloneBoard(board)
                bf = checkBF(localBoardTL)
                States.append((localBoardTL, move, bf, parent))
                # totalBoards.append((localBoardTL, move, bf, parent))


def getNextStates(board):
    # returns a list of possible states from the initial state
    States = []  # eventually will contain [(state, move, bf), (state, move, bf), ... ]
    for r in range(N):
        for c in range(N):
            newBoardState = cloneBoard(board)
            currentCell = board[r][c]

            if currentCell in horCars:
                moveHorizontal(States, board, c, currentCell, r)

            if currentCell in horTrucks:
                moveHorizontal(States, board, c, currentCell, r)

            if currentCell in vertTrucks:
                moveVertical(States, board, c, currentCell, r)

            if currentCell in vertCars:
                moveVertical(States, board, c, currentCell, r)

    statesPerLayer = len(States)
    # print('stop')
    return States


def bfs(board):
    q = Queue()
    q.put(board)
    visited = []
    totalStates = []

    while not q.empty():
        current = q.get()

        if checkWin(current):
            print("BFS: Goal found")
            print(f'Expanded nodes:{len(visited)}')
            print(f'Total states:{len(totalStates)}')
            return True

        # state move bf parent
        for (states, move, bf, parent) in getNextStates(current):
            totalStates.append((bf, states, move, parent))
            if states not in visited:
                visited.append(states)
                q.put(states)

    # print("stop")
    return False


def Id(board):
    q = LifoQueue()
    q.put(board)
    visited = []
    totalStates = []

    # find depth and follow until no more boards present
    while not q.empty():
        current = q.get()

        if checkWin(current):
            print("ID: Goal found")
            print(f'Expanded nodes:{len(visited)}')
            print(f'Total states:{len(totalStates)}')
            return True

        # state move bf parent
        # every idx 0 == new layer staring
        for idx, (states, move, bf, parent) in enumerate(getNextStates(current)):
            totalStates.append((idx, (bf, states, move, parent)))
            if (idx, (bf, states, move, parent)) not in visited:
                visited.append((idx, (bf, states, move, parent)))
                q.put((idx, states))

    # print("stop")
    return False


def DfsWithPath(board):
    q = [[board]]
    visited = []
    totalStates = []
    while q:
        path = q.pop()
        if path[-1][2][5] == 'X':
            print(f"Goal State found in {len(path)} steps")
            print(f"Expanded nodes:{len(visited)}")
            print(f"Total states:{len(totalStates)}")

            # for boards in path:
            #     print()
            #     for board in boards:
            #         print(board)
            return True

        for states, bf, move, parent in getNextStates(path[-1]):
            totalStates.append(states)
            if states not in visited:
                visited.append(states)
                q.append(path + [states])

    print("break")
    return False


def aStar(board):
    bf = checkBF(board)
    q = PriorityQueue()
    q.put((bf, board))
    visited = []
    totalBoardsAStar = []
    cameFrom = None

    while not q.empty():
        current = q.get()

        if current[0] == 0:
            # print(current)
            print("A*: Goal found")
            print(f"Expanded nodes:{len(visited)}")
            print(f'total states:{len(totalBoardsAStar)}')
            return True

        # state move bf parent
        # for each neighbor of current <--
        for states, moves, bf, parent in getNextStates(current[1]):
            totalBoardsAStar.append((states, moves, bf, parent))
            if (bf, states) not in visited:
                # need bf first to work with prio queue
                visited.append((bf, states))
                q.put((bf, states))

    print("A*: Goal not found")
    return False


# ============================================================================================
EMPTY_SPACE = '.'
N = 6

with open("rh.txt", "r", encoding='utf-8') as fd:
    lines = (fd.readlines())

totalBoards = []

# main loop
while True:
    print("RUSH HOUR - pick 1 of 40 puzzles")
    algoNum = int(input("Select a search algorithm:\n"
                        "(1):BFS\n"
                        "(2):ID\n"
                        "(3):A*\n"))
    problemNumber = int(input("Select a problem(1..40) or select(0) to run all problems:\n> "))

    if 0 < algoNum <= 5 and 0 <= problemNumber <= 40:
        # getting info to compute all problems in a loop
        if problemNumber == 0:
            with open("Output.txt", "w") as f:
                with contextlib.redirect_stdout(f):
                    for i in range(4, 44):
                        problem = lines[i]
                        board = strToBoard(problem)
                        horCars, vertCars, vertTrucks, horTrucks = getOrientation(board)

                        if algoNum == 1:  # BFS
                            print(f"Problem {i - 3}")
                            start = timer()
                            bfs(board)
                            end = timer()
                            print(f"Goal reached in {end - start:0.4f} seconds\n")

                        if algoNum == 2:  # ID
                            print(f"Problem {i - 3}")
                            start = timer()
                            Id(board)
                            end = timer()
                            print(f"Goal reached in {end - start:0.5f} seconds\n")

                        if algoNum == 3:  # A*
                            print(f"Problem {i - 3}")
                            sqrBoard(i - 3)
                            start = timer()
                            aStar(board)
                            end = timer()
                            print(f"Goal reached in {end - start:0.5f} seconds\n")

                    break
        else:
            # getting info for single problems
            pos1 = 48 + ((problemNumber - 1) * 15)
            pos2 = 61 + ((problemNumber - 1) * 15)
            s = (problemNumber - 1) + 4
            problem = lines[s]
            board = strToBoard(problem)
            horCars, vertCars, vertTrucks, horTrucks = getOrientation(board)

            if algoNum == 1:  # bfs
                solutionAndBoard(problemNumber)
                print()
                start = timer()
                bfs(board)
                end = timer()
                print(f"Goal reached in {end - start:0.5f} seconds\n")

            if algoNum == 2:  # ID
                solutionAndBoard(problemNumber)
                print()
                start = timer()
                Id(board)
                end = timer()
                print(f"Goal reached in {end - start:0.5f} seconds\n")

            if algoNum == 3:  # A*
                solutionAndBoard(problemNumber)
                print()
                start = timer()
                aStar(board)
                end = timer()
                print(f"Goal reached in {end - start:0.5f} seconds\n")

    else:
        print("> Invalid command. Try again!\n")
