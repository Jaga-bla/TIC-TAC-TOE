import random

# + za osobny plik
# + za przekazywanie parametrów, a nie korzystanie z globalnych zmiennych
# zmieniłbym nazwę `new_list`, ponieważ nie wiadomo co tam siedzi, wiadomo tylko, że to jakaś lista
def choice_ai(map, new_list):
    # dopisałbym komentarze do każdej pętli jaką sytuacją ona pokrywa, zgaduję że chodzi o rzędy, kolumny i przekątne?
    # gdyby trzeba było za 2 miesiące coś poprawić będzie ciężko to skminić
    for j in range(0,7,3):
        # mogłabyś utworzyć zmienne globalne CIRCLE=1 i CROSS=0 (czy tam odwrotnie), żeby wiedzieć który jest który
        if map[0+j][1] ==1 and map[1+j][1]==1 and map[2+j][1] ==0:
            return map[2+j][0]
    for j in range(3):
        if map[0+j][1] ==1 and map[3+j][1]==1 and map[6+j][1] ==0:
            return map[6+j][0]
    for j in range(0,3,2):
        if map[0+j][1] ==1 and map[4][1]==1 and map[8-j][1] ==0:
            return map[8-j][0]
    # czy ta pętla i pierwsza pętla mogły by być połączone? 
    for j in range(0,7,3):
        if map[0+j][1] ==0 and map[1+j][1]==1 and map[2+j][1] ==1:
            return map[0+j][0]
    for j in range(3):
        if map[0+j][1] ==0 and map[3+j][1]==1 and map[6+j][1] ==1:
            return map[0+j][0]
    for j in range(0,3,2):
        if map[0+j][1] ==0 and map[4][1]==1 and map[8-j][1] ==1:
            return map[0+j][0]
    for j in range(0,7,3):
        if map[0+j][1] ==1 and map[1+j][1]==0 and map[2+j][1] ==1:
            return map[1+j][0]
    for j in range(3):
        if map[0+j][1] ==1 and map[3+j][1]==0 and map[6+j][1] ==1:
            return map[3+j][0]
    for j in range(0,3,2):
        if map[0+j][1] ==1 and map[4][1]==0 and map[8-j][1] ==1:
            return map[4][0]
    else:
        return random.choice(new_list)

