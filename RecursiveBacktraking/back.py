#def get_sequence():
#    s = []
#    print('give a sequence of numbers; if you want to stop just input "x": ' )
#    x = input()
#    while x != 'x':
#        s.append(int(x))
#        x = input()



def valid(s, sol, desc, k):
    if(len(sol) == 0 ):
        return 1
    k1 = sol.pop()
    sol.append(k1)
    if desc[0] == -1 and k1 > s[k]:
        desc[0] = 1
    if desc[0] == 1:
        return k1 > s[k]
    desc[0] = -1
    return k1 < s[k]

def solution(sol, desc):
    if len(sol) >= 3 and desc[0] == 1:
        return 1
    return 0


def back_mountain(s):
    k = 0
    desc = [0]
    save_k = 0
    sol = []
    n = len(s)
    while(save_k <= n):
        if(valid(s, sol, desc, k) and k < len(s)-1):
            sol.append(s[k])
            if(solution(sol, desc)):
                string = ''
                for i in sol:
                    string += str(i) + ' '
                print(string)
            k += 1
        else:
            sol = []
            save_k += 1
            k = save_k
            desc[0] = 0

s = [1, 2, -12, 5, 2, 4, 10, 9, -2, 3]
back_mountain(s)