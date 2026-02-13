from PIL import Image
import numpy as np

def convert_to_greyscale(input_path, output_path):
    # Load the image and convert to a NumPy array
    color_img = Image.open(input_path).convert('RGB')
    data = np.array(color_img)

    # Get dimensions (height, width, channels)
    height, width, channels = data.shape
    
    # Create an empty array for the grayscale output
    # Using 'uint8' because pixel values are integers from 0-255
    bw_data = np.zeros((height, width), dtype=np.uint8)

    # Iterate through every pixel
    for y in range(height):
        for x in range(width):
            r, g, b = data[y, x]
            
            # Apply the luminance formula
            grey = int(0.299 * r + 0.587 * g + 0.114 * b)

            # Assign to the new array
            bw_data[y, x] = grey

    # Convert the array back to a PIL image and save
    bw_img = Image.fromarray(bw_data)
    bw_img.save(output_path)
    print(f"Image saved successfully to {output_path}")

# Usage
convert_to_greyscale('image.jpg', 'output_bw.jpg')

