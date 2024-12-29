from PIL import Image, ImageDraw
import imageio
import numpy as np
import os

# Function to create a single frame
def create_frame(size, frame_number):
    """Creates a single frame for the animation.

    Args:
        size (tuple): Width and height of the frame.
        frame_number (int): The current frame number.

    Returns:
        Image: A PIL Image object representing the frame.
    """
    img = Image.new("L", size, "white")  # "L" mode is for grayscale
    draw = ImageDraw.Draw(img)

    # Example animation: Moving and growing circle
    radius = 20 + (frame_number % 30)
    x = 50 + (5 * frame_number)
    y = size[1] // 2

    # Draw a circle
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill="black")

    # Add some lines for extra effect
    for i in range(0, size[0], 20):
        draw.line([(i, 0), (i + frame_number % 20, size[1])], fill="gray", width=1)

    return img

# Function to create a directory for saving frames
def ensure_directory(path):
    """Ensures the specified directory exists.

    Args:
        path (str): The path to the directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)

# Save individual frames as images
def save_frames_as_images(output_dir, frame_count, size):
    """Saves each frame as an individual image.

    Args:
        output_dir (str): Directory to save frames.
        frame_count (int): Number of frames to generate.
        size (tuple): Size of each frame.
    """
    ensure_directory(output_dir)
    for i in range(frame_count):
        frame = create_frame(size, i)
        frame.save(os.path.join(output_dir, f"frame_{i:03d}.png"))

# Create an animated GIF
def generate_gif(output_file, frame_count=50, size=(200, 200), output_dir="frames"):
    """Generates an animated GIF from frames.

    Args:
        output_file (str): Path to the output GIF file.
        frame_count (int): Number of frames in the animation.
        size (tuple): Size of each frame.
        output_dir (str): Directory to save frames before creating GIF.
    """
    frames = []

    # Save frames as images
    save_frames_as_images(output_dir, frame_count, size)

    # Collect frames into an animated GIF
    for i in range(frame_count):
        frame_path = os.path.join(output_dir, f"frame_{i:03d}.png")
        frames.append(imageio.imread(frame_path))

    imageio.mimsave(output_file, frames, duration=0.1)  # duration = seconds per frame

# Main script
def main():
    """Main function to generate an animated GIF."""
    output_file = "animated_black_white.gif"
    frame_count = 50
    size = (200, 200)
    output_dir = "frames"

    print("Generating animated GIF...")
    generate_gif(output_file, frame_count, size, output_dir)
    print(f"Animated GIF saved as {output_file}")

# Entry point
if __name__ == "__main__":
    main()
