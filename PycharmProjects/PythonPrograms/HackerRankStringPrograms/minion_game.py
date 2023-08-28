def minion_game(string):
    # your code goes here
    length=len(string)
    vow=0
    con=0
    for i in range(length):
        if string[i] in 'AEIOU':
            vow=vow+(length-i)
        else:
            con=con+(length-i)
    if(con>vow):
        print('Stuart {}'.format(con))
    elif(con==vow):
        print("Draw")
    else:
        print('Kevin {}'.format(vow))

if __name__ == '__main__':
    s = input()
    minion_game(s)