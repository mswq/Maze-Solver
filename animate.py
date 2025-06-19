from PIL import Image, ImageDraw, ImageFont
from run import *
import imageio

frames = []

for length in range(len(node_amt)):
    # Create an image for this step
    img = Image.new('RGB', (7, 5), color='white')
    draw = ImageDraw.Draw(img)
    # Draw your maze here...
    frames.append(img)

# Save as GIF
imageio.mimsave('maze_exploration.gif', frames, duration=0.2)
