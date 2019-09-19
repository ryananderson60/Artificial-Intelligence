import sys

output = open("Readme.txt", "w")

class Puzzle:
    """
    A class for the puzzle (15 puzzle) we will be performing the
    searches on.
    Author: Ryan Anderson
    Date: 7-6-19
    """
    #Constructor method for puzzle.
    #
    #Params:
    #   state: current puzzle state
    #   searchMethod: search method desired
    #   options: for certain searches
    def __init__(self, state, searchMethod, options = None):
        self.state = state
        self.searchMethod = searchMethod
        self.options = options


    #Method to move space up by subtracting 4
    #from index.
    #Params:
    #   puzzle: state
    #   spaceIndex: index of space to be moved
    #Returns:
    #   new state of puzzle after move.
    def up(puzzle, spaceIndex):
        newSpaceIndex = spaceIndex - 4
        switchChar = puzzle.state[newSpaceIndex]
        newPuzzleList = list(puzzle.state)
        newPuzzleList[spaceIndex] = switchChar
        newPuzzleList[newSpaceIndex] = " "
        newPuzzle = "".join(newPuzzleList)
        newNode = Node(newPuzzle, puzzle.depth, None)
        newNode.priority = 4
        return newNode

    #Method to move space down by adding 4
    #to index.
    #Params:
    #   puzzle: state
    #   spaceIndex: index of space to be moved
    #Returns:
    #   new state of puzzle after move.
    def down(puzzle, spaceIndex):
        newSpaceIndex = spaceIndex + 4
        switchChar = puzzle.state[newSpaceIndex]
        newPuzzleList = list(puzzle.state)
        newPuzzleList[spaceIndex] = switchChar
        newPuzzleList[newSpaceIndex] = " "
        newPuzzle = "".join(newPuzzleList)
        newNode = Node(newPuzzle, puzzle.depth, None)
        newNode.priority = 2
        return newNode

    #Method to move space to the left by subtracting 1
    #from index.
    #Params:
    #   puzzle: state
    #   spaceIndex: index of space to be moved
    #Returns:
    #   new state of puzzle after move.
    def left(puzzle, spaceIndex):
        newSpaceIndex = spaceIndex - 1
        switchChar = puzzle.state[newSpaceIndex]
        newPuzzleList = list(puzzle.state)
        newPuzzleList[spaceIndex] = switchChar
        newPuzzleList[newSpaceIndex] = " "
        newPuzzle = "".join(newPuzzleList)
        newNode = Node(newPuzzle, puzzle.depth, None)
        newNode.priority = 3
        return newNode

    #Method to move space to the right by adding 1
    #to index.
    #Params:
    #   puzzle: state
    #   spaceIndex: index of space to be moved
    #Returns:
    #   new state of puzzle after move.
    def right(puzzle, spaceIndex):
        newSpaceIndex = spaceIndex + 1
        switchChar = puzzle.state[newSpaceIndex]
        newPuzzleList = list(puzzle.state)
        newPuzzleList[spaceIndex] = switchChar
        newPuzzleList[newSpaceIndex] = " "
        newPuzzle = "".join(newPuzzleList)
        newNode = Node(newPuzzle, puzzle.depth, None)
        newNode.priority = 1
        return newNode

    #A method for valid moves of state
    #
    #Params:
    #   puzzle: the state to find moves of
    #Returns:
    #   list of valid moves(states)
    def validMoves(puzzle):
        spaceIndex = 0
        for i in range(len(puzzle.state)):
            if puzzle.state[i] is " ":
                spaceIndex = i
                break

        #The following if statements are valid moves for
        #current state.  Return a list of moves.
        if (spaceIndex == 5 or
            spaceIndex == 6 or
            spaceIndex == 9 or
            spaceIndex == 10):
            return [Puzzle.right(puzzle, spaceIndex),
                    Puzzle.down(puzzle, spaceIndex),
                    Puzzle.left(puzzle, spaceIndex),
                    Puzzle.up(puzzle, spaceIndex)]     
        if (spaceIndex == 0):
            return [Puzzle.right(puzzle, spaceIndex),
                    Puzzle.down(puzzle, spaceIndex)]
        if (spaceIndex == 1 or
            spaceIndex == 2):
            return [Puzzle.right(puzzle, spaceIndex),
                    Puzzle.down(puzzle, spaceIndex),
                    Puzzle.left(puzzle, spaceIndex)]
        if (spaceIndex == 3):
            return [Puzzle.down(puzzle, spaceIndex),
                    Puzzle.left(puzzle, spaceIndex)]
        if (spaceIndex == 4 or
            spaceIndex == 8):
            return [Puzzle.right(puzzle, spaceIndex),
                    Puzzle.down(puzzle, spaceIndex),
                    Puzzle.up(puzzle, spaceIndex)]
        if (spaceIndex == 7 or
            spaceIndex == 11):
            return [Puzzle.down(puzzle, spaceIndex),
                    Puzzle.left(puzzle, spaceIndex),
                    Puzzle.up(puzzle, spaceIndex)]
        if (spaceIndex == 12):
            return [Puzzle.right(puzzle, spaceIndex),
                    Puzzle.up(puzzle, spaceIndex)]
        if (spaceIndex == 13 or
            spaceIndex == 14):
            return [Puzzle.right(puzzle, spaceIndex),
                    Puzzle.left(puzzle, spaceIndex),
                    Puzzle.up(puzzle, spaceIndex)]
        if (spaceIndex == 15):
            return [Puzzle.left(puzzle, spaceIndex),
                    Puzzle.up(puzzle, spaceIndex)]        

    #Method to check goal state of puzzle. 
    #
    #Params:
    #   puzzle: current puzzle state
    #Returns:
    #   True if goal
    def checkGoal(puzzle):
        if (puzzle == "123456789ABCDEF " or
            puzzle == "123456789ABCDFE "):
            return True
        else:
            return False

    #Method to print formation of puzzle. Testing.
    #
    #Params:
    #   puzzle: current state
    def printFormation(puzzle):
        print(puzzle[0:4])
        print(puzzle[4:8])
        print(puzzle[8:12])
        print(puzzle[12:16])

class Node:
    """
    A class for nodes to hold state and depth.
    Author: Ryan Anderson
    Date: 7-6-19
    """

    #Constructor method for Node class.
    #
    #Params:
    #   state: current puzzle state of node
    #   depth: current depth of puzzle
    #   h: heuristic cost
    def __init__(self, state, depth, h = None):
        self.state = state
        self.depth = depth + 1
        self.h = None
        self.priority = None
        self.f = None

    def __eq__(self, other):
        equal = True
        for i in range(len(self.state)):
            if self.state[i] != other.state[i]:
                equal = False
        return isinstance(other, Node) and equal

class Search:
    """
    A class to implement searches for the 15 puzzle problem.
    Author: Ryan Anderson
    Date: 7-6-19
    """
    
    #A method to choose which search specified by
    #user
    #
    #Params:
    #   puzzle: puzzle (15 puzzle) to be solved
    def startSearch(puzzle):
        if puzzle.searchMethod == "BFS":
            Search.bfsGraph(puzzle.state)
        if puzzle.searchMethod == "DFS":
            Search.dfsGraph(puzzle.state)
        if puzzle.searchMethod == "GBFS":
            Search.gbfsGraph(puzzle.state, puzzle.options)
        if puzzle.searchMethod == "AStar":
            Search.aStar(puzzle.state, puzzle.options)
        if puzzle.searchMethod == "DLS":
            Search.dls(puzzle.state)

    #A bfs graph search using two lists to keep track of
    #explored and frontier.  Prints results.
    #
    #Params:
    #   puzzle: puzzle (15 puzzle) to be solved
    def bfsGraph(puzzle):
        result = Result()
        node = Node(puzzle, -1, None)
        if (Puzzle.checkGoal(node.state)):
            result.printResults(0)
            return None
        explored = set()
        frontier = [node]
        frontierSet = set()
        while(frontier):
            node = frontier.pop(0)
            moves = Puzzle.validMoves(node)
            result.numCreated += len(moves)
            for m in moves:
                if(Puzzle.checkGoal(m.state)):
                        result.printResults(m.depth)
                        return None
                if (m.state not in explored and m.state not in frontierSet):
                    result.numExpanded += 1
                    frontier.append(m)
                    frontierSet.add(m.state)
            explored.add(node.state)

            #Check maxFringe
            result.checkMaxFringe(len(frontier))
            
        #No solution found
        result.printResults(-1)

    #A dfs graph search using a list and a set to keep track
    #of visited nodes to compare with new moves and avoid
    #redundant paths. Output results.
    #
    #Params:
    #   puzzle: puzzle to be solved.
    def dfsGraph(puzzle):
        result = Result()
        node = Node(puzzle, -1, None)
        frontier = [node]
        explored = set()
        while (frontier):
            node = frontier.pop(0)
            if Puzzle.checkGoal(node.state):
                result.printResults(node.depth)
                return None
            explored.add(node.state)
            result.numExpanded += 1
            moves = Puzzle.validMoves(node)      
            for m in moves:
                result.numCreated += 1
                if (m not in frontier and m.state not in explored):
                    frontier.append(m)
            result.checkMaxFringe(len(frontier))
        result.printResults(-1)

    #A gbfs search using a heuristic specified by the user.
    #Calls output results.
    #Params:
    #   puzzle: the puzzle to be solved
    #   h: h1 or h2 to be used
    def gbfsGraph(puzzle, h):
        result = Result()
        node = Node(puzzle, -1, Search.getHeuristic(puzzle, h))
        explored = set()
        frontier = [node]
        if (Puzzle.checkGoal(node.state)):
            result.printResults(0)
            return None
        while (len(frontier) != 0):
            node = frontier.pop(0)
            if len(frontier) > 100:
                result.printResults(-1)
                return None
            if(Puzzle.checkGoal(node.state)):
                result.printResults(node.depth)
                return None
            result.numExpanded += 1
            explored.add(node.state)
            moves = Puzzle.validMoves(node)
            result.numCreated += len(moves)
            for m in moves:
                m.h = Search.getHeuristic(m.state, h)
                if (m not in frontier):
                    if (m.state not in explored):
                        insertIndex = -1
                        for i in range(len(frontier)):
                            if m.h < frontier[i].h:
                                insertIndex = i
                                break
                        if insertIndex == -1:
                            frontier.append(m)
                        else:
                            frontier.insert(insertIndex, m)
            result.checkMaxFringe(len(frontier))
            
        result.printResults(-1)

    #Method for aStar search.  Uses heuristic function and path cost
    #
    #Params:
    #   puzzle - original puzzle state
    #   h - heuristic function to use
    def aStar(puzzle, h):
        result = Result()
        node = Node(puzzle, -1, Search.getHeuristic(puzzle, h))
        explored = set()
        frontier = [node]
        if (Puzzle.checkGoal(node.state)):
            result.printResults(0)
            return None
        while(len(frontier) != 0):
            node = frontier.pop(0)
            if(Puzzle.checkGoal(node.state)):
                result.printResults(node.depth)
                return None
            result.numExpanded += 1
            explored.add(node.state)
            moves = Puzzle.validMoves(node)
            result.numCreated += len(moves)
            for m in moves:
                m.h = Search.getHeuristic(puzzle, h)
                m.f = m.h + m.priority
                if (m.state not in explored
                    and m not in frontier):                 
                    insertIndex = -1
                    for i in range(len(frontier)):
                        if m.f < frontier[i].f:
                            insertIndex = i
                            break
                    if insertIndex == -1:
                        frontier.append(m)
                    else:
                        frontier.insert(insertIndex, m)
                elif (m in frontier):
                    for i in range(len(frontier)):
                        if m == frontier[i]:
                            if m.f < frontier[i].f:
                                frontier[i] = m
            result.checkMaxFringe(len(frontier))
                
                    
    #Method for depth limited search.  Output results
    #
    #Params:
    #   puzzle - puzzle to be solved
    #   limit - limit of depth
    def dls(puzzle, limit = 50):
        pResult = Result()
        pResult.maxFringe = 4
        def recursive_dls(node, puzzle, limit, pResult):
            if Puzzle.checkGoal(node.state):
                pResult.printResults(node.depth)
                return False
            elif limit == 0:
                pResult.numExpanded += 1
                return 'cutoff'
            else:
                pResult.numExpanded += 1
                cutoff_occurred = False
                moves = Puzzle.validMoves(node)
                pResult.numCreated += len(moves)
                for m in moves:
                    result = recursive_dls(m, puzzle, limit - 1, pResult)
                    if result == 'cutoff':
                        cutoff_occurred = True
                    elif result is not None:
                        return result
                return 'cutoff' if cutoff_occurred else None

        # Body of depth_limited_search:
        return recursive_dls(Node(puzzle, -1, None), puzzle, limit, pResult)
    
           
    #Method to get heuristic of puzzle.  The heuristic of the puzzle is
    #determined at runtime and does not change.  The two heuristics h1
    #and h2 are number of misplaced tiles and manhattan distance respectively
    #
    #Params: 
    #   puzzle - the current puzzle acted on
    #   h - the heuristic function requested
    #Returns: hscore - the heurstic score (lower is better in this case)
    def getHeuristic(puzzle, h):
        solved1 = "123456789ABCDEF "
        solved2 = "123456789ABCDFE "
        hscore = 0

        #Number of misplaced tiles
        if (h == "h1"):
            for i in range(len(solved1)):
                if (puzzle[i] != solved1[i] or
                puzzle[i] != solved2[i]):
                    hscore += 1
            return hscore
        #Manhattan Distance
        if (h == "h2"):
            h, w = 4, 4
            multiMatrix = [[0 for x in range(w)] for y in range(h)]
            count = 0
            for i in range(h):
                for t in range(w):
                    multiMatrix[i][t] = puzzle[count]
                    count += 1

            for t in range(h):
                for s in range(w):
                    if multiMatrix[t][s] == " ":
                        hscore += abs(0 - t)
                        hscore += abs(0 - s)
                    elif multiMatrix[t][s] == "1":
                        hscore += abs(0 - t)
                        hscore += abs(1 - s)
                    elif multiMatrix[t][s] == "2":
                        hscore += abs(0 - t)
                        hscore += abs(2 - s)
                    elif multiMatrix[t][s] == "3":
                        hscore += abs(0 - t)
                        hscore += abs(3 - s)
                    elif multiMatrix[t][s] == "4":
                        hscore += abs(1 - t)
                        hscore += abs(0 - s)
                    elif multiMatrix[t][s] == "5":
                        hscore += abs(1 - t)
                        hscore += abs(1 - s)
                    elif multiMatrix[t][s] == "6":
                        hscore += abs(1 - t)
                        hscore += abs(2 - s)
                    elif multiMatrix[t][s] == "7":
                        hscore += abs(1 - t)
                        hscore += abs(3 - s)
                    elif multiMatrix[t][s] == "8":
                        hscore += abs(2 - t)
                        hscore += abs(0 - s)
                    elif multiMatrix[t][s] == "9":
                        hscore += abs(2 - t)
                        hscore += abs(1 - s)
                    elif multiMatrix[t][s] == "A":
                        hscore += abs(2 - t)
                        hscore += abs(2 - s)
                    elif multiMatrix[t][s] == "B":
                        hscore += abs(2 - t)
                        hscore += abs(3 - s)
                    elif multiMatrix[t][s] == "C":
                        hscore += abs(3 - t)
                        hscore += abs(0 - s)
                    elif multiMatrix[t][s] == "D":
                        hscore += abs(3 - t)
                        hscore += abs(1 - s)
                    elif multiMatrix[t][s] == "E":
                        hscore += abs(3 - t)
                        hscore += abs(2 - s)
                    elif multiMatrix[t][s] == "F":
                        hscore += abs(3 - t)
                        hscore += abs(3 - s)
            return hscore
        
        

class Result:
    """
    A class to hold results such as numCreated, numExpanded, and
    maxFringe for searches and to display.
    Author: Ryan Anderson
    Date: 7-6-19
    """

    #Constructor method for Result
    #
    #Params:
    #   numCreated: number of nodes created
    #   numExpanded: number of nodes tested and not returned goal
    #   maxFringe: max frontier
    def __init__(self, numCreated = 0, numExpanded = 0, maxFringe = 0):
        self.numCreated = numCreated
        self.numExpanded = numExpanded
        self.maxFringe = maxFringe

    #Method to check and update max fringe if it is
    #less than current frontier
    #
    #Params:
    #   currentFrontier: frontier of current node
    def checkMaxFringe(self, currentFrontier):
        if self.maxFringe < currentFrontier:
            self.maxFringe = currentFrontier

    #Method to output search results. Exits program.
    #
    #Params:
    #   depth: depth of solution found
    def printResults(self, depth):
        if depth == -1:
            output.write(": {}, {}, {}, {}\n".format(-1, -1, -1, -1))
        else:
            output.write(": {}, {}, {}, {}\n".format(depth, self.numCreated,
                                    self.numExpanded, self.maxFringe))

#Main method of program
def main(): 
    #Check for valid initialState arument length
    #Will assume valid digits, letters and space used
    if (len(sys.argv) > 1):
        if (len(sys.argv[1]) != 16):
            print("Initialstate must be 16 characters: only %d entered" %
                  len(sys.argv[0]))
            sys.exit()

    #Check that search method is valid
    if (len(sys.argv) > 1):
        if (sys.argv[2] != "BFS" and
            sys.argv[2] != "DFS" and
            sys.argv[2] != "GBFS" and
            sys.argv[2] != "AStar" and
            sys.argv[2] != "DLS"):
            print("Please enter a valid search")
            sys.exit()

    #No options search initialization
    if len(sys.argv) == 3:
         puzzle = Puzzle(sys.argv[1], sys.argv[2])
         Search.startSearch(puzzle) #start search

    #Options search initialization (
    if len(sys.argv) == 4:
         puzzle = Puzzle(sys.argv[1], sys.argv[2], sys.argv[3])
         Search.startSearch(puzzle) #start search

    #Perform regular output
    if (len(sys.argv) == 1):
        output.write("Part 1:\n")
        initialStates = ["123456789ABC DFE", "123456789AB DEFC"]
        searches = ["BFS", "DFS", "GBFS", "AStar", "DLS"]
        for i in initialStates:
            output.write("Initial State: '{}'\n".format(i))
            output.write("")
            for s in searches:
                if (s == "BFS" or
                    s == "DFS" or
                    s == "DLS"):
                    output.write("{}".format(s))
                    puzzle = Puzzle(i, s)
                    Search.startSearch(puzzle)
                elif (s == "GBFS" or
                      s == "AStar"):        
                    puzzle = Puzzle(i, s, "h1")                 
                    puzzle2 = Puzzle(i, s, "h2")
                    output.write("{}, {}".format(s, "h1"))
                    Search.startSearch(puzzle)
                    output.write("{}, {}".format(s, "h2"))
                    Search.startSearch(puzzle2)
        output.write("\n")
        output.write("Part 2:\n")
        output.write("\n")
        output.write("Time complexities:\n")
        output.write("BFS graph: O(V+E) V is vertex, E is edges\n")
        output.write("DFS graph: O(V+E) V is vertex, E is edges\n")
        output.write("GBFS graph: O(nlogn) where n is number of nodes\n")
        output.write("AStar graph: O(b^d) d is depth\n")
        output.write("DLS: O(b^l) where l is the cutoff\n")
    output.close()
            
        
if __name__ == "__main__":
    main()

