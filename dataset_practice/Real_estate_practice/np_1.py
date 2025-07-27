import numpy as np
path=r"D:\Full_Stack_AI\Work\week3\dataset_practice\datasets\RealEstate-USA.csv"
brokered, price, bed, bath=np.genfromtxt(
    path,
    delimiter=',',
    usecols=(0 ,2 ,3 ,4 ),
    unpack=True,
    skip_header=1,
    dtype=int,
    invalid_raise=False

)
print(price)
print(bed)
print(bath)

add=bed+bath
sub=bed-bath
div=bed/bath

print(sub)
print(add)
print(div)

D2bedbath = np.array([bed,
                  bath])

print (" Lat - 2 dimentional arrary - " ,D2bedbath)


print("  - 2 dimentional arrary - dimension" , D2bedbath.ndim)

print("  - 2 dimentional arrary - size" , D2bedbath.size)

print("  - 2 dimentional arrary - size in each dimension" , D2bedbath.shape)

print("  - 2 dimentional arrary - data type" , D2bedbath.dtype)




# Splicing array
D2bedbathSlice=  D2bedbath[:1,:5]
print(D2bedbathSlice)

# Indexing array
D2bedbathSliceItemOnly=  D2bedbathSlice[0,1]
print(D2bedbathSliceItemOnly)


D2bedbath1TO298 = np.reshape(D2bedbath, (4, 100))

print (" t - 2 dimentional arrary - " ,D2bedbath1TO298)


print("  - dimension" , D2bedbath1TO298)

print("   - size" , D2bedbath1TO298)

print("   - size in each dimension" , D2bedbath1TO298)

print("   - data type" , D2bedbath1TO298)