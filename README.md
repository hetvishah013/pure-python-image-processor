# Pure Python Image Processor

## Objective
To build a basic grayscale image processor using only core Python,without Numpy, OpenCV, or Pillow.

## Image Representation
The image is represented as a 5*5 list of lists.
Each pixel is an integer between 0 and 255.
0 represents black and 255 represents white.

## Functions implemented
1. print_image()- Displays the image in the terminal
2. invert_image()-Inverts each pixel using 255-pixel.
3. adjust_brightness()-Changes brightness and keeps value between 0 to 255
4. threhold_image()-Converts the image into black and white using a specific threshold
5. flip_horizontal() -Flips the image horizontally
6. rotate_clockwise()-Rotates the image 90 degree clockwise
7. blur_image() -Applies a 3*3 averaging blur.

## Border Handling
The blur uses only valid neighboring pixels.At image borders,the number of pixels included in the average is smaller.

## Output
The programme prints the original image and the image before and after each operation.It also prints the original image again to verify that it was not modified.
 ## Technologies
 -Python 3.10+
 -Core Python only 

 ## How to Run 
 Run the following command in the project dirctory:

python3 image_processor.py
