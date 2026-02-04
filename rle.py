#import numpy as np

def run_length_encode(data):
    """Compresses a 1D list using RLE."""
    encoding = []
    if not data:
        return encoding

    prev_pixel = data[0]
    count = 0

    for pixel in data:
        if pixel == prev_pixel:
            count += 1
        else:
            encoding.append((count, prev_pixel))
            count = 1
            prev_pixel = pixel
    
    # Append the last run
    encoding.append((count, prev_pixel))
    return encoding

# 1. Create a simple 10x10 "Bitmap" (0 = White, 1 = Black)
# This represents a simple smiley face shape
bitmap = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,0,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

# 2. Flatten the 2D image into a 1D stream of data
flattened_data = [pixel for row in bitmap for pixel in row]

# 3. Perform Compression
compressed_data = run_length_encode(flattened_data)

# --- Display Results ---
print("--- Original Bitmap ---")
for row in bitmap:
    print(" ".join(['#' if p == 1 else '.' for p in row]))

print(f"\nOriginal Size: {len(flattened_data)} integers")
print(f"Compressed Size: {len(compressed_data)} pairs")
print(f"Compression Ratio: {len(flattened_data) / (len(compressed_data) * 2):.2f}x")

print("\n--- Compressed Data (Count, Value) ---")
print(compressed_data[:10], "...") # Showing first 10 runs