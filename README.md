# Gray Level Slicing in Image Processing

This script demonstrates Gray Level Slicing techniques in Computer Vision. It enhances specific ranges of gray levels in an image, isolating features of interest, and visualizes the results with and without retaining the original background.

## Prerequisites

Ensure you have the required Python libraries installed:

    pip install opencv-python matplotlib numpy

## How to Use

1. Update the image path in the script. It currently reads from `/content/drive/MyDrive/womancat.webp`. Change this to your local image path:
       
       img = cv2.imread('path/to/your/image.webp', 0)
       
2. Adjust the desired intensity range `r_min` and `r_max` if needed.
3. Run the script in your terminal or Python environment.
### Note: You can directly open the `.ipynb` file in Colab or Jupyter Notebook.

## How it Works

1. **Image Loading**: The image is loaded directly in grayscale mode.
2. **Gray Level Slicing (Without Background)**: A binary-like mask is created where pixels within the target intensity range `[r_min, r_max]` are set to 255 (white), and all other pixels are set to 0 (black).
3. **Gray Level Slicing (With Background)**: The pixels within the target range are highlighted by setting them to 255 (white), but the remaining pixels retain their original intensity values.
4. **Visualization**: Uses Matplotlib to display the original image along with the two different gray-level sliced outputs.
