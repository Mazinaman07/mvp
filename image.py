# import os
# from PIL import Image

# def resize_and_convert_image(input_path, output_path, dimensions, output_format):
#     with Image.open(input_path) as img:
#         # Resize the image
#         img = img.resize(dimensions,Image.Resampling.LANCZOS)
        
#         # Determine the output file name and format
#         base_name = os.path.basename(input_path)
#         name, _ = os.path.splitext(base_name)
#         output_file = os.path.join(output_path, f"{name}.{output_format.lower()}")

#         # Convert and save the image
#         img.save(output_file, output_format.upper())
#         print(f"Saved: {output_file}")

# def process_directory(input_directory, output_directory, dimensions, output_format):
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     for filename in os.listdir(input_directory):
#         file_path = os.path.join(input_directory, filename)
#         if os.path.isfile(file_path):
#             resize_and_convert_image(file_path, output_directory, dimensions, output_format)

# def main():
#     input_path = input("Enter the input path (file or directory): C:\\Users\\mazin\\OneDrive\\Desktop\\Task 2\\th.jpg ").strip()
#     output_path = input("Enter the output directory: C:\\Users\\mazin\\OneDrive\\Desktop\\output ").strip()    
#     width = int(input("Enter the width:1200 "))
#     height = int(input("Enter the height: 800"))
#     dimensions = (width, height)
#     output_format = input("Enter the output format (e.g., JPEG, PNG): JPEG")

#     if os.path.isfile(input_path):
#         if not os.path.exists(output_path):
#             os.makedirs(output_path)
#         resize_and_convert_image(input_path, output_path, dimensions, output_format)
#     elif os.path.isdir(input_path):
#         process_directory(input_path, output_path, dimensions, output_format)
#     else:
#         print("Invalid input path. Please provide a valid file or directory.")

# if __name__ == "__main__":
#     main()








import os
from PIL import Image

def resize_and_convert_image(input_path, output_path, dimensions, output_format):
    try:
        with Image.open(input_path) as img:
            # Resize the image using the new Resampling method
            img = img.resize(dimensions, Image.Resampling.LANCZOS)
            
            # Determine the output file name and format
            base_name = os.path.basename(input_path)
            name, _ = os.path.splitext(base_name)
            output_file = os.path.join(output_path, f"{name}.{output_format.lower()}")

            # Convert and save the image
            img.save(output_file, output_format.upper())
            print(f"Saved: {output_file}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def process_directory(input_directory, output_directory, dimensions, output_format):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Supported image file extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(valid_extensions):
            resize_and_convert_image(file_path, output_directory, dimensions, output_format)
        else:
            print(f"Skipping non-image file: {filename}")

def main():
    input_path = input(r"Enter the input path (file or directory):C:\Users\mazin\OneDrive\Desktop\Task 2\th.jpg ").strip()
    if not input_path:
        input_path = r"C:\Users\mazin\OneDrive\Desktop\Task 2\th.jpg" 

    output_path = input(r"Enter the output directory:C:\Users\mazin\OneDrive\Desktop\output ").strip()
    if not output_path:
        output_path = r"C:\Users\mazin\OneDrive\Desktop\output"  

    width = int(input("Enter the width:600 "))
    height = int(input("Enter the height:800 "))
    dimensions = (width, height)
    output_format = input("Enter the output format (e.g., JPEG, PNG):JPEG ").strip()

    if os.path.isfile(input_path):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        if input_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
            resize_and_convert_image(input_path, output_path, dimensions, output_format)
        else:
            print("The input file is not a valid image.")
    elif os.path.isdir(input_path):
        process_directory(input_path, output_path, dimensions, output_format)
    else:
        print("Invalid input path. Please provide a valid file or directory.")

main()

