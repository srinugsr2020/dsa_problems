"""
=============================================================================
PYTHON ARRAYS - COMPREHENSIVE GUIDE
=============================================================================

Python provides multiple ways to work with arrays:
1. array module - Space-efficient arrays of basic types
2. lists - General-purpose dynamic arrays (covered in lists.py)
3. NumPy arrays - High-performance numerical arrays (external library)

This tutorial focuses on the built-in array module and compares it with lists.

Key Characteristics of array module:
- Type-constrained: All elements must be same basic type
- Memory efficient: Uses less memory than lists for numeric data
- Faster for bulk operations on numeric data
- Interoperable with C arrays
=============================================================================
"""

import array
import sys

# =============================================================================
# SECTION 1: CREATING ARRAYS
# =============================================================================

print("=" * 60)
print("SECTION 1: CREATING ARRAYS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Type codes - specify the type of elements
# -----------------------------------------------------------------------------
print("\n1.1 Type codes:")
print("""
    Type Code   C Type              Python Type     Min Size
    ---------------------------------------------------------
    'b'         signed char         int             1 byte
    'B'         unsigned char       int             1 byte
    'u'         wchar_t             Unicode char    2 bytes
    'h'         signed short        int             2 bytes
    'H'         unsigned short      int             2 bytes
    'i'         signed int          int             2 bytes
    'I'         unsigned int        int             2 bytes
    'l'         signed long         int             4 bytes
    'L'         unsigned long       int             4 bytes
    'q'         signed long long    int             8 bytes
    'Q'         unsigned long long  int             8 bytes
    'f'         float               float           4 bytes
    'd'         double              float           8 bytes
""")

# -----------------------------------------------------------------------------
# Creating arrays with different type codes
# -----------------------------------------------------------------------------
print("\n1.2 Creating arrays:")

# Integer arrays
int_array = array.array('i', [1, 2, 3, 4, 5])
print(f"    array('i', [1,2,3,4,5]) = {int_array}")

# Float arrays
float_array = array.array('f', [1.5, 2.5, 3.5])
print(f"    array('f', [1.5,2.5,3.5]) = {float_array}")

# Double precision
double_array = array.array('d', [1.1, 2.2, 3.3])
print(f"    array('d', [1.1,2.2,3.3]) = {double_array}")

# Unsigned integers (for non-negative numbers)
unsigned = array.array('I', [100, 200, 300])
print(f"    array('I', [100,200,300]) = {unsigned}")

# -----------------------------------------------------------------------------
# Creating from other iterables
# -----------------------------------------------------------------------------
print("\n1.3 Creating from iterables:")
from_range = array.array('i', range(1, 6))
print(f"    array('i', range(1,6)) = {from_range}")

from_generator = array.array('i', (x * x for x in range(5)))
print(f"    array('i', (x*x for x in range(5))) = {from_generator}")


# =============================================================================
# SECTION 2: MEMORY EFFICIENCY
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: MEMORY EFFICIENCY")
print("=" * 60)

# -----------------------------------------------------------------------------
# Compare memory usage: array vs list
# -----------------------------------------------------------------------------
print("\n2.1 Memory comparison (1000 integers):")

# List of integers
int_list = list(range(1000))
list_size = sys.getsizeof(int_list) + sum(sys.getsizeof(x) for x in int_list)

# Array of integers
int_arr = array.array('i', range(1000))
array_size = sys.getsizeof(int_arr)

print(f"    List:  {list_size:,} bytes")
print(f"    Array: {array_size:,} bytes")
print(f"    Savings: {(1 - array_size/list_size) * 100:.1f}%")

# -----------------------------------------------------------------------------
# Type information
# -----------------------------------------------------------------------------
print("\n2.2 Array properties:")
arr = array.array('d', [1.1, 2.2, 3.3])
print(f"    arr = {arr}")
print(f"    arr.typecode = '{arr.typecode}'")
print(f"    arr.itemsize = {arr.itemsize} bytes")
print(f"    len(arr) = {len(arr)}")
print(f"    Buffer size = {arr.buffer_info()}")


# =============================================================================
# SECTION 3: ACCESSING AND MODIFYING ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: ACCESSING AND MODIFYING ELEMENTS")
print("=" * 60)

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"\n    arr = {arr}")

# -----------------------------------------------------------------------------
# Indexing (same as lists)
# -----------------------------------------------------------------------------
print("\n3.1 Indexing:")
print(f"    arr[0] = {arr[0]}")
print(f"    arr[-1] = {arr[-1]}")
print(f"    arr[2] = {arr[2]}")

# -----------------------------------------------------------------------------
# Slicing (returns new array)
# -----------------------------------------------------------------------------
print("\n3.2 Slicing:")
print(f"    arr[1:4] = {arr[1:4]}")
print(f"    arr[::2] = {arr[::2]}")
print(f"    arr[::-1] = {arr[::-1]}")

# -----------------------------------------------------------------------------
# Modifying elements
# -----------------------------------------------------------------------------
print("\n3.3 Modifying elements:")
arr[0] = 100
print(f"    arr[0] = 100 -> {arr}")

arr[1:3] = array.array('i', [200, 300])
print(f"    arr[1:3] = array('i', [200, 300]) -> {arr}")


# =============================================================================
# SECTION 4: ARRAY METHODS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: ARRAY METHODS")
print("=" * 60)

# -----------------------------------------------------------------------------
# append() - Add single element to end
# -----------------------------------------------------------------------------
arr = array.array('i', [1, 2, 3])
print(f"\n    Original: {arr}")

arr.append(4)
print(f"\n4.1 append(4): {arr}")

# -----------------------------------------------------------------------------
# extend() - Add multiple elements from iterable
# -----------------------------------------------------------------------------
arr.extend([5, 6, 7])
print(f"4.2 extend([5,6,7]): {arr}")

# -----------------------------------------------------------------------------
# insert() - Insert element at index
# -----------------------------------------------------------------------------
arr.insert(0, 0)
print(f"4.3 insert(0, 0): {arr}")

# -----------------------------------------------------------------------------
# remove() - Remove first occurrence of value
# -----------------------------------------------------------------------------
arr.remove(0)
print(f"4.4 remove(0): {arr}")

# -----------------------------------------------------------------------------
# pop() - Remove and return element at index
# -----------------------------------------------------------------------------
popped = arr.pop()
print(f"4.5 pop(): returned {popped}, arr = {arr}")

popped = arr.pop(0)
print(f"4.6 pop(0): returned {popped}, arr = {arr}")

# -----------------------------------------------------------------------------
# index() - Find index of first occurrence
# -----------------------------------------------------------------------------
arr = array.array('i', [1, 2, 3, 2, 4])
print(f"\n4.7 index() on {arr}:")
print(f"    index(2) = {arr.index(2)}")
print(f"    index(2, 2) = {arr.index(2, 2)}")  # Start from index 2

# -----------------------------------------------------------------------------
# count() - Count occurrences
# -----------------------------------------------------------------------------
print(f"\n4.8 count():")
print(f"    count(2) = {arr.count(2)}")

# -----------------------------------------------------------------------------
# reverse() - Reverse in place
# -----------------------------------------------------------------------------
arr = array.array('i', [1, 2, 3, 4, 5])
arr.reverse()
print(f"\n4.9 reverse(): {arr}")


# =============================================================================
# SECTION 5: CONVERTING TO/FROM OTHER TYPES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: CONVERTING TO/FROM OTHER TYPES")
print("=" * 60)

# -----------------------------------------------------------------------------
# tolist() - Convert to Python list
# -----------------------------------------------------------------------------
arr = array.array('i', [1, 2, 3, 4, 5])
lst = arr.tolist()
print(f"\n5.1 tolist():")
print(f"    {arr}.tolist() = {lst}")
print(f"    type: {type(lst)}")

# -----------------------------------------------------------------------------
# frombytes() and tobytes() - Binary conversion
# -----------------------------------------------------------------------------
print("\n5.2 Binary conversion:")
arr = array.array('i', [1, 2, 3])
binary = arr.tobytes()
print(f"    {arr}.tobytes() = {binary}")

new_arr = array.array('i')
new_arr.frombytes(binary)
print(f"    frombytes() -> {new_arr}")

# -----------------------------------------------------------------------------
# fromlist() - Append elements from list
# -----------------------------------------------------------------------------
print("\n5.3 fromlist():")
arr = array.array('i', [1, 2])
arr.fromlist([3, 4, 5])
print(f"    [1,2].fromlist([3,4,5]) = {arr}")


# =============================================================================
# SECTION 6: FILE OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: FILE OPERATIONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Writing array to file
# -----------------------------------------------------------------------------
print("\n6.1 Writing array to binary file:")
arr = array.array('i', [1, 2, 3, 4, 5])
print(f"    Writing {arr} to 'array_data.bin'")

# Note: Commented to avoid file creation in demo
# with open('array_data.bin', 'wb') as f:
#     arr.tofile(f)

# -----------------------------------------------------------------------------
# Reading array from file
# -----------------------------------------------------------------------------
print("\n6.2 Reading array from binary file:")
print("""
    # Reading from binary file
    new_arr = array.array('i')
    with open('array_data.bin', 'rb') as f:
        new_arr.fromfile(f, 5)  # Read 5 elements
    print(new_arr)
""")


# =============================================================================
# SECTION 7: ARRAY VS LIST PERFORMANCE
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: ARRAY VS LIST PERFORMANCE")
print("=" * 60)

import time

# -----------------------------------------------------------------------------
# Creation performance
# -----------------------------------------------------------------------------
print("\n7.1 Creation performance (1 million integers):")

start = time.perf_counter()
lst = list(range(1000000))
list_time = time.perf_counter() - start

start = time.perf_counter()
arr = array.array('i', range(1000000))
array_time = time.perf_counter() - start

print(f"    List:  {list_time:.4f} seconds")
print(f"    Array: {array_time:.4f} seconds")

# -----------------------------------------------------------------------------
# Iteration performance
# -----------------------------------------------------------------------------
print("\n7.2 Iteration performance:")

start = time.perf_counter()
total = sum(lst)
list_time = time.perf_counter() - start

start = time.perf_counter()
total = sum(arr)
array_time = time.perf_counter() - start

print(f"    List sum:  {list_time:.4f} seconds")
print(f"    Array sum: {array_time:.4f} seconds")

# -----------------------------------------------------------------------------
# When to use each
# -----------------------------------------------------------------------------
print("\n7.3 When to use each:")
print("""
    USE array.array WHEN:
    ✅ Storing large amounts of numeric data
    ✅ Memory efficiency is important
    ✅ Interacting with C code or binary files
    ✅ All elements are the same basic type
    
    USE list WHEN:
    ✅ Need mixed types in collection
    ✅ Need fast append/pop from end
    ✅ Collection is small to medium size
    ✅ Need more flexibility
    
    USE NumPy arrays WHEN:
    ✅ Need mathematical operations
    ✅ Need multidimensional arrays
    ✅ Need broadcasting and vectorization
    ✅ Doing scientific/numerical computing
""")


# =============================================================================
# SECTION 8: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: PRACTICAL EXAMPLES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Example 1: Processing binary sensor data
# -----------------------------------------------------------------------------
print("\n8.1 Processing binary sensor data:")

def process_sensor_data():
    """Simulate reading temperature sensor data."""
    # Simulate sensor readings (in tenths of degrees)
    readings = array.array('h', [235, 238, 240, 242, 239, 237])
    
    # Convert to actual temperatures
    temps = [r / 10 for r in readings]
    
    print(f"    Raw readings: {readings.tolist()}")
    print(f"    Temperatures: {temps}")
    print(f"    Average: {sum(temps) / len(temps):.1f}°C")

process_sensor_data()

# -----------------------------------------------------------------------------
# Example 2: Efficient storage of flags/bits
# -----------------------------------------------------------------------------
print("\n8.2 Efficient bit flags storage:")

def bit_flags_example():
    """Store boolean flags efficiently using bytes."""
    # Each byte can store 8 flags
    # For 1000 flags, we need 125 bytes instead of 1000+ bytes for a list
    
    flags = array.array('B', [0] * 125)  # 125 bytes = 1000 bits
    
    def set_flag(flags, index):
        byte_idx = index // 8
        bit_idx = index % 8
        flags[byte_idx] |= (1 << bit_idx)
    
    def get_flag(flags, index):
        byte_idx = index // 8
        bit_idx = index % 8
        return bool(flags[byte_idx] & (1 << bit_idx))
    
    # Set some flags
    set_flag(flags, 0)
    set_flag(flags, 5)
    set_flag(flags, 100)
    
    print(f"    Flag 0: {get_flag(flags, 0)}")
    print(f"    Flag 5: {get_flag(flags, 5)}")
    print(f"    Flag 50: {get_flag(flags, 50)}")
    print(f"    Flag 100: {get_flag(flags, 100)}")
    print(f"    Memory: {sys.getsizeof(flags)} bytes for 1000 flags")

bit_flags_example()

# -----------------------------------------------------------------------------
# Example 3: Image pixel buffer
# -----------------------------------------------------------------------------
print("\n8.3 Image pixel buffer (grayscale):")

def image_buffer_example():
    """Simulate grayscale image processing."""
    # 10x10 grayscale image (0-255 values)
    width, height = 10, 10
    pixels = array.array('B', [0] * (width * height))
    
    # Draw a diagonal line
    for i in range(min(width, height)):
        pixels[i * width + i] = 255
    
    # Display image as ASCII art
    print("    Image (diagonal line):")
    for y in range(height):
        row = ""
        for x in range(width):
            row += "█" if pixels[y * width + x] > 128 else "."
        print(f"    {row}")

image_buffer_example()

# -----------------------------------------------------------------------------
# Example 4: Audio samples buffer
# -----------------------------------------------------------------------------
print("\n8.4 Audio samples (simulated):")

def audio_buffer_example():
    """Simulate audio sample processing."""
    import math
    
    # Generate sine wave samples (16-bit audio)
    sample_rate = 44100
    frequency = 440  # A4 note
    duration = 0.01  # 10ms
    
    samples = array.array('h')  # 16-bit signed integers
    
    for i in range(int(sample_rate * duration)):
        t = i / sample_rate
        value = int(32767 * math.sin(2 * math.pi * frequency * t))
        samples.append(value)
    
    print(f"    Sample rate: {sample_rate} Hz")
    print(f"    Frequency: {frequency} Hz")
    print(f"    Duration: {duration * 1000} ms")
    print(f"    Samples generated: {len(samples)}")
    print(f"    First 10 samples: {samples[:10].tolist()}")
    print(f"    Memory: {sys.getsizeof(samples)} bytes")

audio_buffer_example()


# =============================================================================
# SECTION 9: COMPARISON WITH NUMPY
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: COMPARISON WITH NUMPY")
print("=" * 60)

print("""
array.array vs NumPy array:

Feature                 array.array          NumPy
---------------------------------------------------------
Built-in               Yes                  No (external)
Multidimensional       No (1D only)         Yes
Math operations        No                   Yes
Broadcasting           No                   Yes
Memory efficiency      Good                 Excellent
Performance            Good                 Excellent
Use case               Simple storage       Scientific computing

When you need math operations, use NumPy:

    import numpy as np
    
    # Create NumPy array
    arr = np.array([1, 2, 3, 4, 5])
    
    # Element-wise operations
    doubled = arr * 2
    squared = arr ** 2
    
    # Statistics
    mean = arr.mean()
    std = arr.std()
    
    # Matrix operations
    matrix = arr.reshape(5, 1)
""")


# =============================================================================
# SECTION 10: SUMMARY
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: SUMMARY")
print("=" * 60)

print("""
ARRAY MODULE SUMMARY:

Creating:
    arr = array.array('i', [1, 2, 3])    # Signed integers
    arr = array.array('f', [1.0, 2.0])   # Floats
    arr = array.array('d', [1.0, 2.0])   # Doubles

Common Operations:
    arr.append(x)         # Add element
    arr.extend(iterable)  # Add multiple elements
    arr.insert(i, x)      # Insert at index
    arr.remove(x)         # Remove first occurrence
    arr.pop()             # Remove and return last
    arr.index(x)          # Find index
    arr.count(x)          # Count occurrences
    arr.reverse()         # Reverse in place

Conversion:
    arr.tolist()          # To Python list
    arr.tobytes()         # To bytes
    arr.frombytes(b)      # From bytes
    arr.fromlist(lst)     # Append from list

Properties:
    arr.typecode          # Type character
    arr.itemsize          # Bytes per element
    len(arr)              # Number of elements

BEST PRACTICES:
  1. Use array for large homogeneous numeric data
  2. Use list for general-purpose collections
  3. Use NumPy for mathematical operations
  4. Consider memory vs flexibility trade-offs
  5. Use appropriate type code for your data range
""")


print("\n" + "=" * 60)
print("END OF ARRAYS TUTORIAL")
print("=" * 60)
