import cv2
import numpy as np
import random
import os

def add_dust_effect(image, num_circles=20, min_radius=15, max_radius=50, alpha=0.2, beta=0.5):
    # Make a copy of the image to draw the dust circles
    output = image.copy()
    height, width = image.shape[:2]

    # Create an overlay to draw the circles on
    overlay = np.zeros((height, width, 3), dtype=np.uint8)

    for _ in range(num_circles):
        # Random center for the dust circle
        center_x = random.randint(0, width - 1)
        center_y = random.randint(0, height - 1)

        # Random radius for the dust circle
        radius = random.randint(min_radius, max_radius)

        # Random intensity for the dust circle color
        intensity = random.randint(100, 256)  # Vary intensity between 100 and 256
        circle_color = (intensity, intensity, intensity)  # Gray color for the circles in BGR

        # Draw the circle on the overlay with the specified color
        cv2.circle(overlay, (center_x, center_y), radius, circle_color, -1, lineType=cv2.FILLED)

    # Apply a Gaussian blur to make the circles look more cloudy
    blurred_overlay = cv2.GaussianBlur(overlay, (51, 51), 0)
    blurred_overlay = cv2.bitwise_not(blurred_overlay)

    # Increase the alpha blending to make the circles less noticeable
    cv2.addWeighted(blurred_overlay, alpha, output, beta, 0, output)

    return output

def generate_random_gradient_masks(image_shape):
    height, width, _ = image_shape

    # Randomly choose the gradient direction
    direction = random.choice(['horizontal', 'vertical'])

    if direction == 'horizontal':
        # Horizontal gradient from left to right
        mask1 = np.repeat(np.tile(np.linspace(1, 0, width), (height, 1))[:, :, np.newaxis], 3, axis=2)
        mask2 = np.repeat(np.tile(np.linspace(0, 1, width), (height, 1))[:, :, np.newaxis], 3, axis=2)
    else:
        # Vertical gradient from top to bottom
        mask1 = np.repeat(np.tile(np.linspace(1, 0, height), (width, 1)).T[:, :, np.newaxis], 3, axis=2)
        mask2 = np.repeat(np.tile(np.linspace(0, 1, height), (width, 1)).T[:, :, np.newaxis], 3, axis=2)

    return mask1, mask2

def blend_images(img1, img2):
    # Generate random gradient masks
    mask1, mask2 = generate_random_gradient_masks(img1.shape)

    # Blend images using masks
    final = np.uint8(img1 * mask1 + img2 * mask2)

    return final

def process_images_in_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):  # You can add other image formats if needed
            image_path = os.path.join(input_folder, filename)

            # Load the image
            image = cv2.imread(image_path)

            if image is None:
                print(f"Failed to load image {image_path}")
                continue

            # Add dust effect
            image_with_dust = add_dust_effect(image)

            # Create a black image for the gradient transition
            black_image = np.zeros_like(image_with_dust)

            # Blend images with gradient
            blended_image = blend_images(image_with_dust, black_image)

            # Save the result to the output folder
            output_path = os.path.join(output_folder, f'dust_{filename}')
            cv2.imwrite(output_path, blended_image)
            print(f"Processed and saved {output_path}")

# Specify the input and output folder paths
input_folder = '/home/rosalie/Desktop/livecell/images/livecell_test_images/livecell_test_png'
output_folder = '/home/rosalie/Desktop/livecell/images/livecell_test_images/processed_images'

# Process all images in the input folder and save them to the output folder
process_images_in_folder(input_folder, output_folder)

