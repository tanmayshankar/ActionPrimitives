#!/usr/bin/env python
from headers import *
from DMP_Segment import *

FILE_DIR = "/home/tanmay/catkin_ws/src/Visualize_Primitives/Data/K2_Demos/Grid_Demo/D{0}"

lhlabel = [[] for i in range(10)]
rhlabel = [[] for i in range(10)]
lhseg = [[] for i in range(10)]
rhseg = [[] for i in range(10)]

for i in range(10):
    lhlabel[i] = npy.load(os.path.join(FILE_DIR.format(i+1),"LH_Label.npy"))
    rhlabel[i] = npy.load(os.path.join(FILE_DIR.format(i+1),"RH_Label.npy"))
    lhseg[i] = npy.load(os.path.join(FILE_DIR.format(i+1),"LH_Seg.npy"))
    rhseg[i] = npy.load(os.path.join(FILE_DIR.format(i+1),"RH_Seg.npy"))

action_list = npy.array(['Null','Reach','Place','Return','Pour'])

hc3 = [[] for i in range(10)]
lh = [[] for i in range(10)]
rh = [[] for i in range(10)]
lhs = [[] for i in range(10)]
rhs = [[] for i in range(10)]

for i in range(10):
    hc3[i] = npy.load(os.path.join(FILE_DIR.format(i+1),"Hand_Coordinates_3D.npy"))
    lh[i] = hc3[i][:,0,:]
    rh[i] = hc3[i][:,2,:]
    lhs[i] = hc3[i][:,1,:]
    rhs[i] = hc3[i][:,3,:]

consider = 'Reaching'
consider_ind = 1
consider = 'Return'
consider_ind = 3
consider = 'Pouring'
consider_ind = 4

seglist = [[] for i in range(10)]
ctr = 0
for k in range(10):
    for i in range(len(lhlabel[k])):
        if lhlabel[k][i]==consider_ind:
            ctr +=1
            seglist[k].append(i)
    
pos = [[] for i in range(ctr)]
ind = 0
for k in range(10):
    citr = 0
    for i in range(len(lhlabel[k])):
        if lhlabel[k][i]==consider_ind:
            print(k,i,lhseg[k][seglist[k][citr]],lhseg[k][seglist[k][citr]+1])
            pos[ind] = lh[k][lhseg[k][seglist[k][citr]]:lhseg[k][seglist[k][citr]+1]]
            ind +=1
            citr +=1

fig = plt.figure()
ax = fig.gca(projection='3d')
for i in range(ctr):
    ax.plot(pos[i][:,0],pos[i][:,1],pos[i][:,2],linewidth=1)
# plt.show()

rolltime = 100
dmps = [DMP(100) for i in range(ctr)]

for i in range(ctr):
    dmps[i].linear_interpolate(pos[i])
    dmps[i].initialize_variables()
    dmps[i].learn_DMP()
    dmps[i].rollout(dmps[i].demo_pos[0],dmps[i].demo_pos[-1],dmps[i].demo_vel[0])

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
for i in range(ctr):
    ax1.plot(dmps[i].pos_roll[:,0],dmps[i].pos_roll[:,1],dmps[i].pos_roll[:,2])

for i in range(ctr):
    dmps[i].rollout(npy.zeros(3),npy.ones(3),npy.zeros(3))

fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')
for i in range(ctr):
    ax2.plot(dmps[i].pos_roll[:,0],dmps[i].pos_roll[:,1],dmps[i].pos_roll[:,2])
plt.show()


