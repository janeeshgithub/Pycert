from PIL import Image, ImageDraw, ImageFont
import os

names = ["Janeesh P","Ava", "Liam", "Sophia", "Noah", "Mia", "Elijah", "Isabella", "Mason", "Harper", "Lucas"]


# Paths
template_path = '1.png'  # Path to your certificate template
font_path = 'GreatVibes-Regular.ttf'  # Path to your downloaded font file
output_dir = 'certificates'  # Output directory for the generated certificates

# Gold color in RGB
gold_color = (212, 175, 55)

# Function to generate certificate
def generate_certificate(name):
    # Open the certificate template
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Font settings
    font_size_name = 100  # Adjust font size for the name
    font_name = ImageFont.truetype(font_path, font_size_name)

    # Define text positions (adjust based on your template)
    name_position = (840, 650)  # Example position for the name

    # Add name to the image
    draw.text(name_position, name, font=font_name, fill=gold_color)

    # Save the certificate
    output_path = f'{output_dir}/{name}_certificate.png'
    img.save(output_path)
    print(f'Certificate generated for {name} and saved to {output_path}')

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate certificates for all names
for name in names:
    generate_certificate(name)
