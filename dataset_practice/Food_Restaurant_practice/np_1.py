import numpy as np

path = r'D:\Full_Stack_AI\Work\week3\dataset_practice\datasets\FastFoodRestaurants.csv'

# Read all as strings
add, city, long, lat = np.genfromtxt(
    path,
    delimiter=',',
    usecols=(0, 1, 5, 7),     # Make sure these are correct: 4 = longitude, 5 = latitude
    unpack=True,
    dtype=str,
    skip_header=1,
    encoding='utf-8',
    invalid_raise=False
)

# Define safe float checker
def is_float(s):
    try:
        float(s)
        return True
    except:
        return False

# Print bad values (optional debug)
for i, (lon, la) in enumerate(zip(long, lat)):
    if not is_float(lon) or not is_float(la):
        print(f"Skipping Row {i}: long = {lon}, lat = {la}")

# Create a boolean mask for valid rows
mask = np.array([is_float(lon) and is_float(la) for lon, la in zip(long, lat)])

# Apply mask
long = long[mask].astype(float)
lat = lat[mask].astype(float)
add = add[mask]
city = city[mask]

# Now it's safe to compute
print("Sample Longitude:", long[:5])
print("Sample Latitude:", lat[:5])
print("Long + Lat:", (long + lat)[:5])
subtraction = long - lat
multiplication = long * lat
division = long / lat


print("  Long - lat - Subtraction:", subtraction)
print("  Long - lat - Multiplication:", multiplication)
print("  Long - lat - Division:", division)

D2LongLat = np.array([long,
                  lat])

print (" Lat - 2 dimentional arrary - " ,D2LongLat)


print(" Long Plus Lat - 2 dimentional arrary - dimension" , D2LongLat.ndim)

print(" Long Plus Lat - 2 dimentional arrary - size" , D2LongLat.size)

print(" Long Plus Lat - 2 dimentional arrary - size in each dimension" , D2LongLat.shape)

print(" Long Plus Lat - 2 dimentional arrary - data type" , D2LongLat.dtype)


# Splicing array
D2LongLatSlice=  D2LongLat[:1,:5]
print(D2LongLatSlice)

# Indexing array
D2LongLatSliceItemOnly=  D2LongLatSlice[0,1]
print(D2LongLatSliceItemOnly)

#print each value

# for elem in np.nditer(D2LongLat):
#     print(elem)

#to reshape
D2LongLat1TO298 = np.reshape(D2LongLat, (1, 19670))

print (" Lat - 2 dimentional arrary - " ,D2LongLat1TO298)


print(" Long Plus Lat  - dimension" , D2LongLat1TO298)

print(" Long Plus Lat  - size" , D2LongLat1TO298)

print(" Long Plus Lat  - size in each dimension" , D2LongLat1TO298)

print(" Long Plus Lat  - data type" , D2LongLat1TO298)