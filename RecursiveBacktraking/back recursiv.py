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


def back_mountain(s, sol, desc, k, save_k, n):
    if save_k > n:
        return
    if(save_k <= n):
        if(valid(s, sol, desc, k) and k < len(s)-1):
            sol.append(s[k])
            if(solution(sol, desc)):
                string = ''
                for i in sol:
                    string += str(i) + ' '
                print(string)
            back_mountain(s, sol, desc, k+1 , save_k, n)
        else:
            sol = []
            save_k += 1
            k = save_k
            desc[0] = 0
            back_mountain(s, sol, desc, k, save_k, n)

s = [1, 2, -12, 5, 2, 4, 10, 9, -2, 3]
k = 0
desc = [0]
save_k = 0
sol = []
n = len(s)
back_mountain(s, sol, desc, k, save_k, n)