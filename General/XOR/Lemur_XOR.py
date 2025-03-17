from PIL import Image

# Load the two encrypted images
lemur = Image.open('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
flag = Image.open('flag_7ae18c704272532658c10b5faad06d74.png')

# Ensure both images are the same size
if lemur.size != flag.size:
    raise ValueError("Images must be the same size")

# Create a new image to store the XOR result
xor_image = Image.new('RGB', lemur.size)
lemur_pixels = lemur.load()
flag_pixels = flag.load()
xor_pixels = xor_image.load()

# Iterate through each pixel and XOR the RGB values
for x in range(lemur.size[0]):
    for y in range(lemur.size[1]):
        lr, lg, lb = lemur_pixels[x, y]
        fr, fg, fb = flag_pixels[x, y]
        xor_pixels[x, y] = (lr ^ fr, lg ^ fg, lb ^ fb)

# Save the resulting image
xor_image.save('xor_result.png')
print("XOR result saved as xor_result.png. Check this image for the flag!")