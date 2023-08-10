import cv2

# Load the main image
main_image = cv2.imread('C:\\Users\\91984\\Pictures\\Screenshots\\Screenshot 2023-08-08 114348.png')

# Load the watermark image
watermark = cv2.imread('C:\\Users\\91984\\Pictures\\Screenshots\\Screenshot 2023-08-10 083301.png', -1)

# Get the dimensions of the watermark image
watermark_height, watermark_width, _ = watermark.shape

# Define the position to place the watermark (top-left corner)
x_position = 10
y_position = 10

# Define the opacity level (0.0 to 1.0)
opacity = 0.5  # Adjust this value to change opacity

# Resize the watermark to match the desired height and width
watermark_resized = cv2.resize(watermark, (watermark_width, watermark_height))

# Overlay the watermark on the main image with reduced opacity
for c in range(0, 3):
    main_image[y_position:y_position + watermark_height, x_position:x_position + watermark_width, c] = (
        opacity * watermark_resized[:, :, c] + (1.0 - opacity) * main_image[
            y_position:y_position + watermark_height, x_position:x_position + watermark_width, c]
    )

# Save the result
cv2.imwrite('output_image.jpg', main_image)

# Display the result
cv2.imshow('Watermarked Image', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
