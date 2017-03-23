# -*- coding: utf-8 -*-  

roles = []
with open('../dict_files/roles.csv', 'r') as f:
    for line in f:
        if line.find('、'):
            for s in line.split('、'):
                roles.append(s)
        else:
            roles.append(s)

x = []
with open('../dict_files/roles-processed.csv', 'w') as f:
    for r in sorted(set(roles)):
        print(r)
        if len(r) > 0:
            r = r.split(',')[0]
            if len(r) > 0:
                f.write(r + '\n')
                x.append(r)

x = []
with open('../dict_files/comp-query.csv', 'r') as f:
    x = f.readlines()

# 广播、电视、电影和影视录音制作业
# 文化艺术业
query = 'MATCH (n:Company) where %s RETURN n'
scope = ''
start = True
with open('../dict_files/company-query.txt', 'w') as f:
    for r in x:
        if start:
            start = False
        else:
            scope += ' OR '

        scope += 'n.businessScope contains \"%s\"' % r.strip()

    scope += ' OR n.industry contains \"广播、电视、电影和影视录音制作业\"'

    f.write(query%scope)
