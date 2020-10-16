def solution(record):
    answer = []
    user={}
    for i in record:
        sp=i.split()
        if sp[0]=='Enter' or sp[0]=='Change':
            user[sp[1]]=sp[2]
    for i in record:
        sp=i.split()
        if sp[0]=='Enter':
            answer.append('{0}님이 들어왔습니다.'.format(user[sp[1]]))
        elif sp[0]=='Leave':
            answer.append('{0}님이 나갔습니다.'.format(user[sp[1]]))
    return answer