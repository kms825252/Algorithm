from sys import stdin as ss

'''42676KB 192ms'''
points = ss.readlines()[1:]
points.sort(key=lambda y:int(y.split()[1]))
points.sort(key=lambda x:int(x.split()[0]))
print(''.join(points))
