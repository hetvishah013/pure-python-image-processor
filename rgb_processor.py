def invert_rgb_image(image):
    """Invert the colors of an RGB image."""
    result = []

    for row in image:
        new_row = []
        for pixel in row:
            red = 255 - pixel[0]
            green = 255 - pixel[1]
            blue = 255 - pixel[2]
            new_row.append((red, green, blue))
        result.append(new_row)
    return result

def adjust_rgb_brighntess(image, amount):
    """Increase or decrease RGB brightness."""
    result = []

    for row in image:
        new_row = []
        for pixel in row:
           new_pixel=[]
           for channel in pixel:
               value = max(0, min(255, channel + amount))
               new_pixel.append(value)
        new_row.append(new_pixel)
        result.append(new_row)
    return result

def flip_horizontal_rgb(image):
    result = []
    for row in image:
        new_row=[]

        for pixel in row[::-1]:
            new_row.append(pixel)
        result.append(new_row)
    return result

def rotate_clockwise_rgb(image):
    if not image or not image[0]:
        return []

    rows=len(image)
    cols=len(image[0])
    result=[]

    for col in range(cols):
        new_row=[]
        for row in range(rows-1,-1,-1):
            new_row.append(image[row][col])
        result.append(new_row)
    return result

def blur_rgb_image(image):
    if not image or not image[0]:
        return []

    rows = len(image)
    cols = len(image[0])
    result = []

    for r in range(rows):
        new_row = []
        for c in range(cols):
            # Calculate the average of the surrounding pixels
            total_red = 0
            total_green = 0
            total_blue = 0
            count = 0

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    

                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        pixel = image[nr][nc]
                        total_red += pixel[0]   
                        total_green += pixel[1]
                        total_blue += pixel[2]
                        count += 1

                        new_pixel=[
                            round(total_red / count),
                            round(total_green / count),
                            round(total_blue / count)
                        ]
            new_row.append(new_pixel)
        result.append(new_row)
    return result
