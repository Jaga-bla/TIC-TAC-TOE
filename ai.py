import random

def choice_ai(map, empty_fields_list):
    #prevent vertical win possibilities
    for j in range(0,7,3):
        if map[0+j][1] ==1 and map[1+j][1]==1 and map[2+j][1] ==0:
            return map[2+j][0]
        if map[0+j][1] ==0 and map[1+j][1]==1 and map[2+j][1] ==1:
            return map[0+j][0]
        if map[0+j][1] ==1 and map[1+j][1]==0 and map[2+j][1] ==1:
            return map[1+j][0]
    #prevent horizontal win possibilities
    for j in range(3):
        if map[0+j][1] ==1 and map[3+j][1]==1 and map[6+j][1] ==0:
            return map[6+j][0]
        if map[0+j][1] ==0 and map[3+j][1]==1 and map[6+j][1] ==1:
            return map[0+j][0]
        if map[0+j][1] ==1 and map[3+j][1]==0 and map[6+j][1] ==1:
            return map[3+j][0]
    #prevent diagonal win possibilities
    for j in range(0,3,2):
        if map[0+j][1] ==1 and map[4][1]==1 and map[8-j][1] ==0:
            return map[8-j][0]
        if map[0+j][1] ==0 and map[4][1]==1 and map[8-j][1] ==1:
            return map[0+j][0]
        if map[0+j][1] ==1 and map[4][1]==0 and map[8-j][1] ==1:
            return map[4][0]
    else:
        return random.choice(empty_fields_list)

