# coding: utf-8
import numpy as npy
import matplotlib.pyplot as plt
import copy
from scipy import signal
g = npy.zeros((10,100))
def gaussian(x, mu, sig):
    return npy.exp(-npy.power(x - mu, 2.) / (2 * npy.power(sig, 2.)))
for i in range(0,10):
    g[i] = gaussian(npy.linspace(0,1,100),float(i)/10,0.1)
    
for i in range(0,10):
    plt.plot(npy.linspace(0,1,100),g[i])
    
plt.show()
g = npy.zeros((20,100))
for i in range(0,20):
    g[i] = gaussian(npy.linspace(0,1,100),float(i)/20,0.1)
    
for i in range(0,20):
    plt.plot(npy.linspace(0,1,100),g[i])
    
plt.show()
range(10)
float(range(10))
range(10).astype(float)
npy.array(range(10))
npy.array(range(10)).astype(float)
npy.array(range(10)).astype(float)/10
get_ipython().magic(u'ls ')
s
is
get_ipython().magic(u'pinfo npy.diff')
sd]\\
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Research/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Code/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd RRM/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pinfo npy.diff')
range(10)
10-range(10)
10-npy.array(range(10))
12-npy.array(range(10))
diff(12-npy.array(range(10)),npy.array(range(10)))
npy.diff(12-npy.array(range(10)),npy.array(range(10)))
npy.diff(range(10))
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ActionPrimitives/')
get_ipython().magic(u'ls ')
Traj = npy.loadtxt("Trajectories_SQ.txt")
Traj.shape
Traj = Traj.reshape(100,100,2)
Traj.shape
traj = Traj[0:10,:,:]
T = 20
sub_traj = npy.zeros((20,20,2))
sub_traj = npy.zeros((10,20,2))
for i in range(0,9):
    print(i)
    
for i in range(0,9):
    sub_traj[i,:,:] = traj[0,i*10:i*10+T,:]
    
get_ipython().magic(u'ls ')
gaussian_ker = npy.zeros((20,2))
gaussian_ker[:,0]=0.1
gaussian_ker[:,1]=npy.array(range(20)).astype(float)/20
gaussian_ker
for i in range(0,20):
    plt.plot(npy.linspace(0,1,20),gaussian_ker[:,1])
    
plt.show()
K = 100
D = 2*10
T 
alpha = 1
theta = 1
w = npy.zeros(20)
w
get_ipython().magic(u'ls ')
ka
def calc_phase(time):
    return npy.exp(-time/T)
calc_phase(3)
calc_phase(91)
calc_phase(19)
calc_phase(20)
def calc_phase(time):
    return npy.exp(-float(time)/T)
    
calc_phase(20)
T
npy.exp(-1)
calc_phase(0)
calc_phase(1)
sub_traj
pos = sub_traj[0]
pos
vel = npy.diff(pos)
vel
vel = npy.diff(pos,0)
vel
get_ipython().magic(u'pinfo npy.diff')
vel = npy.diff(pos,axis=0)
vel
acc = npy.diff(vel,axis=0)
def calc_target_force(time):
    return (1./(pos[T-1]-pos[0]))*(-K*pos[time]+D*vel[time]+T*acc[time])
def basis(index,time):
    return npy.exp(- gaussian_ker[index,0]*(calc_phase(time)-gaussian_ker[index,1]))
def calc_force(time):
    ret = 0
    den = 0
    for i in range(0,20):
        ret += w[i]*basis(i,time)*calc_phase(time)
        det += basis(i,time)
    ret /= den
    return ret
phi
phi = npy.zeros((20,20))
get_ipython().magic(u'ls ')
target_forces = npy.zeros(20)
for t in range(0,20):
    target_forces[i]=calc_target_force(t+1)
    
for t in range(0,20):
    print(calc_target_force(t+1))
    
    
c
w = npy.ones((20,2))
target_forces = npy.zeros((20,2))
for t in range(0,20):
    target_forces[i,:]=calc_target_force(t+1)
    
def calc_target_force(time):
    return (1./(pos[T-1]-pos[0]))*(-K*pos[time]+D*vel[min(time,vel.shape[0])]+T*acc[min(time,acc.shape[0])])
    
for t in range(0,20):
    target_forces[i,:]=calc_target_force(t+1)
    
pos
pos.shape
vel.shape
acc.shape
acc.shape[0]
def calc_target_force(time):
    return (1./(pos[T-1]-pos[0]))*(-K*pos[time]+D*vel[min(time,vel.shape[0]-1)]+T*acc[min(time,acc.shape[0]-1)])
    
    
for t in range(0,20):
    target_forces[i,:]=calc_target_force(t+1)
    
for t in range(0,20):
    target_forces[i,:]=calc_target_force(t)
    
pos
1./[2,3]
1. / npy.array([2,3])
sub_traj[1]
pos = sub_traj[1]
vel = npy.diff(pos,axis=0) 
acc = npy.diff(vel,axis=0)
vel
acc
for t in range(0,20):
    target_forces[i,:]=calc_target_force(t)
    
target_forces
for t in range(0,20):
    target_forces[t,:]=calc_target_force(t)
    
target
target_forces
w
phi
for i in range(0,20):
    for t in range(0,20):
        phi[i,t] = 
for i in range(0,20):
    for t in range(0,20):
        phi[i,t] = 
for i in range(0,20):
    for t in range(0,20):
        den = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
phi
target_forces
phi.sahpe
phi.shape
target_forces.shape
weights = npy.linalg.pinv(phi)*target_forces
phi*target_forces
weights = npy.zeros((20,2))
weights[:,0]=npy.linalg.pinv(phi)*target_forces[:,0]
phi*target_forces[:,0]
npy.linalg.inv(phi)
npy.linalg.inv(phi).shape
npy.linalg.inv(phi)*target_forces[:,0]
npy.linalg.pinv(phi)*target_forces[:,0]
npy.linalg.pinv(phi)*target_forces[:,0].shape
(npy.linalg.pinv(phi)*target_forces[:,0]).shape
(npy.linalg.pinv(phi)).shape
phi_plus = npy.linalg.pinv(phi)
phi_plus.shape
weights[:,0].shape
phi_plus*target_forces[:,0]
(phi_plus*target_forces[:,0]).shape
(phi_plus*target_forces[:,0]').shape
(phi_plus*npy.transpose(target_forces[:,0])).shape
npy.ones((20,20))*npy.ones(20)
npy.ones((20,20))*npy.ones((1,20))
npy.ones((20,20))*npy.ones((20,1))
npy.multiply(npy.ones((20,20)),npy.ones(20))
npy.random.rand(4,3)
npy.random.rand(4,3)*npy.random.rand(3)
npy.random.rand(4,3)*npy.ones(3)
x = npy.random.rand(4,3)
y = npy.ones(3)
y
x
x*y
x*npy.transpose(y)
npy.transpose(x)*y
npy.dot(x,y)
npy.dot(phi_plus,target_forces).shape
weights = npy.dot(phi_plus,target_forces)
weights[:,0]
weights[:,1]
weights1 = copy.deepcopy(weights)
sub_traj[1]
sub_traj[0]
pos
pos
get_ipython().magic(u'ls ')
get_ipython().magic(u'mkdir Data')
get_ipython().magic(u'cd Data/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'mkdir trial_1')
get_ipython().magic(u'cd trial_1/')
get_ipython().magic(u'ls ')
with file('pos.txt','w') as outfile:
    npy.savetxt(outfile,pos,fmt='%i')
    
with file('target_forces.txt','w') as outfile:
    npy.savetxt(outfile,target_forces,fmt='%-7.5f')
    
with file('weights.txt','w') as outfile:
    npy.savetxt(outfile,weights,fmt='%-7.5f')
    
pos = npy.zeros((20,2))
pos
pos[:,0]=range(3,23)
pos
pos[:,1]=range(5,25)
pos
vel = npy.diff(pos,axis=0)
vl
vel
acc = npy.diff(vel,axis=0)
acc
for t in range(0,20):
    target_forces[t,:]=calc_target_force(t)
    
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force(t)
    
target_forces
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
phi[:,:]=0
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
phi
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd lines/')
with file('weights_line1.txt','w') as outfile:
    npy.savetxt(outfile,weights,fmt='%-7.5f')
    
    
with file('target_forces_line1.txt','w') as outfile:
    npy.savetxt(outfile,target_forces,fmt='%-7.5f')
    
with file('pos_line1.txt','w') as outfile:
    npy.savetxt(outfile,pos,fmt='%i')
    
pos
pos[:,:]=0
pos[:,0]=30-range(3,23)
pos[:,0]=30-npy.array(range(3,23))
pos
pos[:,1]=range(9,29)
pos
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
for t in range(0,20):
    target_forces[t,:]=calc_target_force(t)
    
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force(t)
    
phi[:,:]=0
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
with file('pos_line2.txt','w') as outfile:
    npy.savetxt(outfile,pos,fmt='%i')
    
with file('target_forces_line2.txt','w') as outfile:
    npy.savetxt(outfile,target_forces,fmt='%-7.5f')
    
with file('weights_line2.txt','w') as outfile:
    npy.savetxt(outfile,weights,fmt='%-7.5f')
    
    
npy.linspace(2,42,2)
npy.linspace(2,42,20)
pos[:,0]=npy.linspace(2,42,20)
pos[:,1]=npy.linspace(4,16,20)
target_forces[:,:]=0
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
for t in range(0,20):
    target_forces[t,:]=calc_target_force(t)
    
phi[:,:]=0
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
with file('target_forces_line3.txt','w') as outfile:
    npy.savetxt(outfile,target_forces,fmt='%-7.5f')
    
with file('weights_line3.txt','w') as outfile:
    npy.savetxt(outfile,weights,fmt='%-7.5f')
    
    
with file('pos_line3.txt','w') as outfile:
    npy.savetxt(outfile,pos,fmt='%i')
    
w1 = npy.loadtxt('weights_line3.txt')
w1 = npy.loadtxt('weights_line1.txt')
w3 = npy.loadtxt('weights_line3.txt')
w2 = npy.loadtxt('weights_line2.txt')
w1
w2
w3
f1 = npy.loadtxt('target_forces_line1.txt')
f2 = npy.loadtxt('target_forces_line2.txt')
f3 = npy.loadtxt('target_forces_line3.txt')
f1
f2
f3
get_ipython().magic(u'ls ')
w
w2
w1
w3
pos1 = npy.loadtxt('pos_line1.txt')
pos2 = npy.loadtxt('pos_line2.txt')
pos3 = npy.loadtxt('pos_line3.txt')
pos1
pos2
pos3
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd //')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd scls')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ')
get_ipython().magic(u'cd Research/Code/ActionPrimitives/scripts/')
get_ipython().magic(u'save learn_DMP_trial.py 1-290')
get_ipython().magic(u'ls ')
def calc_target_force(time):
    return (1./(pos[T-1]-pos[0]))*(-K*pos[time]+D*vel[min(time,vel.shape[0]-1)]+T*acc[min(time,acc.shape[0]-1)])    
def calc_target_force_pastor(time):
    return -(pos[T-1]-pos[time])+(pos[T-1]-pos[0])*calc_phase(time)+(T*acc[min(time,acc.shape[0)]-1]-D*vel[min(time,vel.shape[0]-1)])/K
    
 
def calc_target_force_pastor(time):
    return -(pos[T-1]-pos[time])+(pos[T-1]-pos[0])*calc_phase(time)+(T*acc[min(time,acc.shape[0]-1])-D*vel[min(time,vel.shape[0]-1)])/K
 
def calc_target_force_pastor(time):
    return -(pos[T-1]-pos[time])+(pos[T-1]-pos[0])*calc_phase(time)+(T*acc[min(time,acc.shape[0]-1)]-D*vel[min(time,vel.shape[0]-1)])/K
    
    
 
p1
pos1
pos = pos1
wpwd
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd Data/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd lines/')
get_ipython().magic(u'ls ')
pos
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
for t in range(0,20):
    target_forces[t,:]=calc_target_force_pastor(t)
    
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_pastor(t)
    
phi = npy.zeros((20,20))
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
phi
weights
weights[:,:]=-
weights[:,:]=0
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
w1 = weights
f1 = target_forces
f1
pos = pos2
pos = pos3
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
pos = pos2
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_pastor(t)
    
phi[:,:]=0
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
w1
pos
pos1
pso2
po2
pos2
pos
pos1
pos = pos1
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_pastor(t)
    
phi[:,:]=0
for i
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
w1=weights
pos = pos2
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
f1 = target_forces
f1
target_forces[:,:]=0
f1
for t in range(0,20):
    target_forces[t,:]=calc_target_force_pastor(t)
    
phi[:,:]=0
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_pastor(t)
    
target_forces
def calc_target_force_pastor(time):
    return -(pos[T-1]-pos[time])+(pos[T-1]-pos[0])*calc_phase(time)+(T*acc[min(time,acc.shape[0]-1)]-D*vel[min(time,vel.shape[0]-1)])/K
pos = pos2
vel = npy.diff(pos,axis=0)
vel
pos2
acc = npy.diff(vel,axis=0) 
target_forces
f1
pos = pos3
vel
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
vel
acc 
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_pastor(t)
    
phi[:,:]=0
for i
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
w1
get_ipython().magic(u'ls ')
alphaz = 1
betaz = 0.25
def calc_target_force_pastor(time):
    return -(pos[T-1]-pos[time])+(pos[T-1]-pos[0])*calc_phase(time)+(T*acc[min(time,acc.shape[0]-1)]-D*vel[min(time,vel.shape[0]-1)])/K
def calc_target_force_auke(time):
    return T*acc[min(time,acc.shape[0]-1)] - alphaz*(betaz*(pos[T-1]-pos[time])-vel[min(time,vel.shape[0]-1)])
pos
pos = pos1
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_auke(t)
    
targ
target_forces
phi[:,:]=0
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)*(pos[T-1]-pos[0])/det
            
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)*(pos[T-1]-pos[0])/det
            
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
for t in range(0,20):
    target_forces[t,:]=calc_target_force_auke(t)/(pos[T-1]-pos[0])
    
    
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_auke(t)/(pos[T-1]-pos[0])
    
    
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
pos
pos1
pos = pos3
pos = pos2
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_auke(t)/(pos[T-1]-pos[0])
    
    
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
pos = pos3 
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_auke(t)/(pos[T-1]-pos[0])
    
    
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
def calc_target_force_auke(time):
    return (T**2)*acc[min(time,acc.shape[0]-1)] - alphaz*(betaz*(pos[T-1]-pos[time])-T*vel[min(time,vel.shape[0]-1)])
target_forces[:,:]=0
pos
pos1
pos=pos1
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
target_forces[:,:]=0
for t in range(0,20):
    target_forces[t,:]=calc_target_force_auke(t)/(pos[T-1]-pos[0])
    
    
phi[:,:]=0
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
pos 
pos1
pos = pos2
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0) 
for t in range(0,20):
    target_forces[t,:]=calc_target_force_auke(t)/(pos[T-1]-pos[0])
    
    
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
weights = npy.dot(npy.linalg.pinv(phi),target_forces) 
weights
pos
for i in range(0,20):
    for t in range(0,20):
        det = 0
        for j in range(0,20):
            det += basis(j,t)
        phi[i,t] = basis(i,t)*calc_phase(t)/det
            
for t in range(0,20):
    target_forces[t,:]=calc_target_force_auke(t)/(pos[T-1]-pos[0])
    
    
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd scripts/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'save learn_DMP_trial_2.py 1-290')
get_ipython().magic(u'save learn_DMP_trial_2.py 1-466')
