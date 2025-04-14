while True:
    user=input()
    ls=list(user)
    if int(user)==0:
        break
    else:
        ls_r=ls.copy()
        ls_r.reverse()
        print('yes') if ls==ls_r else print('no')