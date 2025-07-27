import numpy as np
path=r"D:\Full_Stack_AI\Work\week3\dataset_practice\datasets\Startups in 2021 end.csv"
Company,Valuation,City,Industry=np.genfromtxt(
    path,
    delimiter=",",
    unpack=True,
    dtype=None,
    usecols=(1,2,5,6),
    skip_header=1,
    invalid_raise=False,
    encoding="utf-8",

)

print(Company)
print(Valuation)
# Clean and convert valuation strings to float
Valuation_float = np.array([float(v.replace('$', '').replace(',', '')) for v in Valuation])

# Now Valuation_float is a NumPy array of floats
print("Converted Valuation Column:", Valuation_float[:5])

add=Valuation_float+Valuation_float

print(add)

sub=Valuation_float-Valuation_float
print(sub)


D2vf = np.array([Valuation_float,
                  Valuation_float])

print (" Lat - 2 dimentional arrary - " ,D2vf)


print("  - 2 dimentional arrary - dimension" , D2vf.ndim)

print("  - 2 dimentional arrary - size" , D2vf.size)

print("  - 2 dimentional arrary - size in each dimension" , D2vf.shape)

print("  - 2 dimentional arrary - data type" , D2vf.dtype)

# Splicing array
D2bedbathSlice=  D2vf[:1,:5]
print(D2bedbathSlice)

# Indexing array
D2bedbathSliceItemOnly=  D2bedbathSlice[0,1]
print(D2bedbathSliceItemOnly)


D2vf1to1872 = np.reshape(D2vf, (1, 1872))

print (" t - 2 dimentional arrary - " ,D2vf1to1872)


print("  - dimension" , D2vf1to1872)

print("   - size" , D2vf1to1872)

print("   - size in each dimension" , D2vf1to1872)

print("   - data type" , D2vf1to1872)