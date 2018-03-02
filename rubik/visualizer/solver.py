import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    Assumes the rubik.quarter_twists move set.
    """

    found = False
    i=0
    left = [((),start)]
    right = [((),end)]
    while not found:
        moves = []
        for p in left[i]:
            moves.append((left[i][0] +rubik.F) , (rubik.perm_apply(rubik.F, p)))
            moves.append((left[i][0] +rubik.Fi),(rubik.perm_apply(rubik.Fi, p)))
            moves.append((left[i][0] +rubik.L), (rubik.perm_apply(rubik.L, p)))
            moves.append((left[i][0] +rubik.Li) ,(rubik.perm_apply(rubik.Li, p)))
            moves.append((left[i][0] +rubik.U), (rubik.perm_apply(rubik.U, p)))
            moves.append((left[i][0] +rubik.Ui), (rubik.perm_apply(rubik.Ui, p)))

        left.append(moves)

        for p in right[i]:
            moves.append((right[i][0] +rubik.Fi), (rubik.perm_apply(rubik.F, p)))
            moves.append((right[i][0] +rubik.F), (rubik.perm_apply(rubik.Fi, p)))
            moves.append((right[i][0] +rubik.Li), (rubik.perm_apply(rubik.L, p)))
            moves.append((right[i][0] +rubik.L), (rubik.perm_apply(rubik.Li, p)))
            moves.append((right[i][0] +rubik.Ui), (rubik.perm_apply(rubik.U, p)))
            moves.append((right[i][0] +rubik.U), (rubik.perm_apply(rubik.Ui, p)))

        right.append(moves)

        for p in left:
            for q in p:
                for z in right[i]:
                    if q[1] == z[1]:
                        found=True
                        moves = q[0]
                        moves.append(z[0])

                        return moves
        i+=1
