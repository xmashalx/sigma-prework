#https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1 
#Office I - outed
#the following is the solution to the above challenge from codewars
def outed(meet, boss):
    total=0
    for member, happines in meet.items():
        if member==boss:
            total+=2*happines
        else:
            total+=happines
    total_score=total/len(meet)
    if total_score<=5:
        str='Get Out Now!'
    else:
        str='Nice Work Champ!'
    return str

#https://www.codewars.com/kata/57ed4cef7b45ef8774000014
#Office II - boredom score
#the following is the solution the above challenge from codewars
def boredom(staff):
    boredom_score=0
    for department in staff.values():
        if department=='accounts':
            boredom_score+=1
        elif department=='finance':
            boredom_score+=2
        elif department=='canteen':
            boredom_score+=10
        elif department=='regulation':
            boredom_score+=3
        elif department=='trading' or department=='change':
            boredom_score+=6
        elif department=='IS':
            boredom_score+=8
        elif department=='retail':
            boredom_score+=5
        elif department=='cleaning':
            boredom_score+=4
        else:
            boredom_score+=25
    if boredom_score<=80:
        msg='kill me now'
    elif boredom_score>=100:
        msg='party time!!'
    else:
        msg='i can handle this'
    return msg 
