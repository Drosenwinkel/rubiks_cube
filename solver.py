import rubik

def shortest_path(start, end):

    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    Assumes the rubik.quarter_twists move set.
    """
    if start ==end:
        return []
    else:
        numTwists =0;
        found = False
        i=0
        left = [ [ ([],start) ] ]
        right = [[([],end)]]
        while not found:
            moves = []
            for p in left[i]:
                #print left[i]
                #print p
                moves.append(( ['F']+ p[0], (rubik.perm_apply(rubik.F, p[1]))))
                moves.append(( ['Fi']+p[0],(rubik.perm_apply(rubik.Fi, p[1]))))
                moves.append(( ['L']+ p[0], (rubik.perm_apply(rubik.L, p[1]))))
                moves.append(( ['Li']+p[0],(rubik.perm_apply(rubik.Li, p[1]))))
                moves.append(( ['U'] +p[0], (rubik.perm_apply(rubik.U, p[1]))))
                moves.append(( ['Ui']+p[0], (rubik.perm_apply(rubik.Ui, p[1]))))

            left.append(moves)

            for p in left:
                for q in p:
                    for z in right[i]:
                        if q[1] == z[1]:
                            found=True
                            moves =[]


                            #print q[0]
                            #print z[0]
                            #print list(q[0])
                            #print list(z[0])

                            moves =list(q[0]) + list(z[0])
                            print moves

                            answer = []
                            for m in moves:
                                if m == 'F':
                                    answer.append(rubik.F)
                                elif m== 'Fi':
                                    answer.append(rubik.Fi)
                                elif m== 'L':
                                    answer.append(rubik.L)
                                elif m== 'Li':
                                    answer.append(rubik.Li)
                                elif m == 'U':
                                    answer.append(rubik.U)
                                elif m == 'Ui':
                                    answer.append(rubik.Ui)


                            #print(len(answer))
                            return answer

            moves=[]

            for p in right[i]:
                moves.append((['Fi']+p[0], (rubik.perm_apply(rubik.F, p[1]))))
                moves.append((['F'] +p[0], (rubik.perm_apply(rubik.Fi, p[1]))))
                moves.append((['Li']+p[0], (rubik.perm_apply(rubik.L, p[1]))))
                moves.append((['L'] +p[0], (rubik.perm_apply(rubik.Li, p[1]))))
                moves.append((['Ui']+p[0], (rubik.perm_apply(rubik.U, p[1]))))
                moves.append((['U'] +p[0], (rubik.perm_apply(rubik.Ui, p[1]))))

            right.append(moves)


            i+=1
