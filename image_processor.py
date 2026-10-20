# Pure Python Image Processor
# No NumPy, OpenCV, or Pillow

#1. Represent a grayscale image as a 5*5 grid 
original_image = [
    [0, 40, 80, 120, 160],
    [40, 80, 120, 160, 200],
    [80, 120, 160, 200, 240],
    [120, 160, 200, 240, 255],
    [160, 200, 240, 255, 255]
] 

# Display the image in the terminal
def print_image(image):
    for row in image:
        print(" ".join(f"{pixel:3}" for pixel in row))
    print()

#2. Pixel-wise operation: invert the image
def invert_image(image):
    return [[255 - pixel for pixel in row] for row in image]

#3. Pixel-wise operation: adjust brightness
def adjust_brightness(image, amount):
    return[
        [max(0, min(255, pixel + amount)) for pixel in row] for row in image
    ]

#4. Pixel-wise operation: thresholding
def threshold_image(image, threshold):
    return [[255 if pixel >= threshold else 0 for pixel in row] for row in image]

#5. Geometric operation: horizontal flip
def horizontal_flip(image):
    return [row[::-1] for row in image]

#6. Geometric operation: rotate 90 degrees clockwise
def rotate_90_clockwise(image):
    return [[image[row][col] for row in range(len(image)-1, -1, -1)] for col in range(len(image[0]))]

#7. Neighborhood operation: 3*3 averaging blur
def blur_image(image):
    height = len(image)
    width = len(image[0])
    result= []

    for row in range(height):
        new_row = []
        for col in range(width):
            total = 0
            count = 0

            #Vist valid neighbours in the 3*3 window
            for r in range(max(0, row-1), min(height, row+2)):
                for c in range(max(0, col-1), min(width, col+2)):
                    total += image[r][c]
                    count += 1

            new_row.append(total // count)
        result.append(new_row)
    return result
# Print the input and output for every operation
def show_operation(name, image, operation):
    print("=" * 45)
    print(name)
    print("Bfeore:")
    print_image(image)
    result = operation(image)
    print("After:")
    print_image(result) 
    return result

# Main program
if __name__ == "__main__":
    print("ORIGINAL GRAYSCALE IMAGE")
    print_image(original_image)
    show_operation("Invert Image", original_image, invert_image)

    show_operation("2.Adjust Brightness by +30", original_image, lambda img: adjust_brightness(img, 30)
                                     )

    show_operation("3.Threshold at 128", original_image, lambda img: threshold_image(img, 128)
                                     )
    show_operation("4.Horizontal Flip", original_image, horizontal_flip
                                      )
    show_operation("5.Rotate 90 Degrees Clockwise", original_image, rotate_90_clockwise
                    )
    show_operation("6.3*3 Averaging Blur", original_image, blur_image)

    print("ORIGINAL IMAGE AFTER ALL OPERATIONS")
    print_image(original_image)
          