import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(file_path):
    return cv2.imread(file_path, 1)

def resize_image(image, scale_factor=None, new_size=None, interpolation=cv2.INTER_LINEAR):
    if scale_factor:
        return cv2.resize(image, (0, 0), fx=scale_factor, fy=scale_factor)
    elif new_size:
        return cv2.resize(image, new_size, interpolation=interpolation)

def display_images(images, titles, rows, cols):
    count = len(images)
    for i in range(count):
        plt.subplot(rows, cols, i + 1)
        plt.title(titles[i])
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.show()

def save_image(image, file_path):
    cv2.imwrite(file_path, image)


def main():
    source = "q.jpg"
    destination = "newq.jpg"
    interpolated_destination = "interpolated_q.jpg"  # New line for saving the interpolated image

    # Load the original image
    original_image = load_image(source)

    # Resize images
    half_image = resize_image(original_image, scale_factor=0.1)
    bigger_image = resize_image(original_image, new_size=(1050, 1610))
    stretch_near_image = resize_image(original_image, new_size=(780, 540), interpolation=cv2.INTER_LINEAR)

    # Display resized images
    resized_images = [original_image, half_image, bigger_image, stretch_near_image]
    Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
    display_images(resized_images, Titles, rows=2, cols=2)

    # Save the interpolated image
    save_image(stretch_near_image, interpolated_destination)

    # Save the bigger image
    save_image(bigger_image, destination)

    # Load another image for HDR conversion (replace "image2.jpg" with your second image)
    image2 = load_image("image2.jpg")

    # Display HDR result
    Titles = ["Original", "HDR Result"]
    display_images([original_image, image2], Titles, rows=1, cols=2)

if __name__ == "__main__":
    main()
