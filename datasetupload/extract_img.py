import os
import xml.etree.ElementTree as ET
from PIL import Image
from tqdm import tqdm


# To get file names from path.
def get_filenames_from_path(path):
    img_file_names = [file for file in sorted(os.listdir(path)) if file.endswith('.jpg')]
    xml_file_names = [file for file in sorted(os.listdir(path)) if file.endswith('.xml')]

    return img_file_names, xml_file_names


# To get selection location with the help of parse xml.
def parse_xml(xml_file_type, extract_type):
    tree = ET.parse(xml_file_type)
    root = tree.getroot()
    coordinates = []

    for obj in root.findall('object'):
        name = obj.find('name').text
        if name == extract_type:
            box = obj.find('bndbox')
            xmin = int(box.find('xmin').text)
            ymin = int(box.find('ymin').text)
            xmax = int(box.find('xmax').text)
            ymax = int(box.find('ymax').text)
            coordinates.append((xmin, ymin, xmax, ymax))

    return coordinates


# To extract and save images.
def extract_and_save_images(xml_file_path, image_file, extract_type, image_size):
    coordinates = parse_xml(xml_file_path, extract_type)
    img_name = os.path.basename(image_file).split(".")[0]  # Get the file name section
    image_file = Image.open(image_file)

    for i, coord in enumerate(coordinates):
        cropped_image = image_file.crop(coord).resize((image_size, image_size))

        # Build the complete save path and file name.
        save_directory = f'datasetupload/{extract_type}/'
        file_name = f"{img_name}_cropped{i + 1}.jpg"
        file_save_path = os.path.join(save_directory, file_name)  # build the full file path

        # Check if the directory exists, create it if it doesn't.
        if not os.path.exists(os.path.dirname(file_save_path)):
            os.makedirs(os.path.dirname(file_save_path))

        # Save the image to the specified path.
        cropped_image.save(file_save_path)


if __name__ == '__main__':
    # Specify the path of the extracted file and the category of the extracted image.
    file_path = 'datasetupload/trainimg/'
    img_type = 'logo'
    # TODO: The image size is calculated based on the data in the XML file.
    img_size = 160

    # Get the file path and the total number of files.
    img_files, xml_files = get_filenames_from_path(file_path)
    total_files = len(img_files)

    # Extract and save the image.
    for img_file, xml_file in tqdm(zip(img_files, xml_files), total=total_files, desc="Processing"):
        xml_file = file_path + xml_file
        img_file = file_path + img_file
        extract_and_save_images(xml_file, img_file, img_type, img_size)

    print(f"Total images: {total_files}\nImage path: {img_type}/{file_path}\nImage size: {img_size}*{img_size}")