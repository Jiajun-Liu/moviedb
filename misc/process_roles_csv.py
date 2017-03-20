# -*- coding: utf-8 -*-  

roles=[]
with open('../dict_files/roles.csv','r') as f:
	for line in f:
		if line.find('、'):
			for s in line.split('、'):
				roles.append(s)
		else:
			roles.append(s)


with open('../dict_files/roles-processed.csv','w') as f:
	for r in sorted(set(roles)):
		print(r)
		if len(r)>0:	
			r=r.split(',')[0]
			if len(r)>0:	
				f.write(r+'\n')


