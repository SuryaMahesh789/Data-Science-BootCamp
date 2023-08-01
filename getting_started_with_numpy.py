import numpy as np

a=np.array([1,2,3])
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b)

print(a.ndim)
print(b.ndim)

print(a.shape)
print(b.shape)

print(a.dtype)
print(b.dtype)

print(a.itemsize)
print(b.itemsize)

print(a.size)
print(b.size)

print(a.nbytes)
print(b.nbytes)


a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a[1,5])

print(a[0,:])

print(a[:,2])


print(a[0,1:6])
print(a[0,1:6:1])
print(a[0,1:6:2])



print(a[0,1:-1:2])

print(a[1,5])

a[1,5]=100
print(a[1,5])

print(a)


a[:,2]=5
print(a)

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

print(b.size)
print(b.ndim)
print(b.dtype)
print(b.shape)
print(b.itemsize)
print(b.nbytes)


print(b[0,1,1])


print(b[:,1,:])

b[:,1,:]=[[9,9],[8,8]]

print(b)

print(np.zeros(5))

print(np.zeros((2,3)))

print(np.zeros((2,3,3)))

print(np.zeros((2,3,3,2)))

print(np.ones((2,2)))

print(np.ones((1,2,3)))

print(np.ones((2,2),dtype='int32'))

print(np.zeros((2,2),dtype='int32'))

print(np.full((2,2),99,dtype='int32'))

print(np.full((2,2),100,dtype='int32'))

print(a.shape)

print(np.full_like(a,4))

print(np.random.rand(4,2))

print(np.random.random_sample(a.shape))

print(np.random.randint(10,size=(3,3)))

print(np.random.randint(5,10,size=(4,4)))

print(np.random.randint(-4,8,size=(3,3)))

print(np.identity(3))

print(np.identity(2))

print(np.identity(4))

arr=np.array([1,2,3])

r1=np.repeat(arr,3,axis=0)
print(r1)

arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)

output=np.ones((5,5))

z=np.zeros((3,3))

print(output)
print(z)

z[1,1]=9

print(z)

output[1:4,1:4]=z
print(output)

a=np.array([1,2,3])
b=a.copy()

b[0]=1000

print(b)
print(a)

a=np.array([1,2,3,4,5])

print(a+2)
print(a-2)

print(a*2)
print(a/2)

a+=2
print(a)

b=np.array([1,2,3,4,5])
print(a+b)

print(b)
print(b**2)


print(np.sin(a))
print(np.cos(a))

a=np.ones((2,3),dtype='int32')
print(a)

b=np.full((3,2),2)
print(b)

c=np.matmul(a,b)
print(c)

c=np.full((3,2),3,dtype='int32')
print(c)


c=np.identity(3)

print(c)
print(np.linalg.det(c))


stats=np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))
print(np.max(stats))

print(np.min(stats,axis=1))

stats=np.array([[11,10,3],[4,15,6],[7,81,9]])
print(stats)

print(np.min(stats,axis=0))
print(np.max(stats,axis=1))

print(np.min(stats,axis=1))
print(np.max(stats,axis=1))

print(np.sum(stats,axis=0))
print(np.sum(stats,axis=1))



a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)

b=a.reshape((8,1))
print(b)

print(a)

b=a.reshape((4,2))
print(b)

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])

v3=np.vstack([v1,v2])
print(v3)

v4=np.vstack([v1,v2,v3])
print(v4)


v=np.vstack([v1,v2,v2,v1])
print(v)


h1=np.ones((2,4),dtype='int32')
h2=np.zeros((2,2),dtype='int32')

print(h1)
print(h2)

h=np.hstack((h1,h2))
print(h)


h=np.hstack((h2,h1))
print(h)