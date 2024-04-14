from PIL import Image, ImageDraw, ImageFont
import os
# program to Text Input: take text from the folder in .txt only

def text_input():
    file_path = input("Enter the path of the input text file: ")
    if file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    else:
        raise ValueError("Invalid file format. Please provide a formatted_text file only.")

# PDF Generation: Convert the handwritten text into a PDF document with a white blank paper background.

def generate_pdf(text, font_path):
    # Open the paper image
    paper_image = Image.open("/path/resources/paper1.png")
    # Create a new image with the same size as the paper image
    image = Image.new('RGB', paper_image.size, color='white')
    # Paste the paper image onto the new image
    image.paste(paper_image, (0, 0))
    # Draw the image
    d = ImageDraw.Draw(image)
    # Load the font
    fnt = ImageFont.truetype(font_path, 23)
    # Write the text on the image
    d.text((10, 10), text, font=fnt, fill=(0, 0, 255))
    # Save the image as a PDF
    output_path = os.path.join(os.path.dirname(__file__), 'Output', 'handwritten_text.pdf')
    image.save(output_path)

if __name__ == "__main__":

    text = text_input()
    font_path = "/path/resources/Zapfino.ttf"
    generate_pdf(text, font_path)
    print("Check output folder for the PDF file.")
