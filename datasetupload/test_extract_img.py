import unittest

from datasetupload.extract_img import get_filenames_from_path, parse_xml, extract_and_save_images


class TestExtractImg(unittest.TestCase):
    def test_get_filenames_from_path(self):
        file_path = 'testimg/'

        # Get JPG and XML file names
        img_files, xml_files = get_filenames_from_path(file_path)

        for img_file, xml_file in zip(img_files, xml_files):
            img_prefix = img_file.split('.')[0]  # get the first of img_file previous section.
            xml_prefix = xml_file.split('.')[0]  # get the first of xml_file previous section.
            self.assertEqual(img_prefix, xml_prefix)  # to check whether the file names are the same
            print(f"JPG file: {img_file} | XML file: {xml_file}")

    def test_parse_xml(self):
        _, xml_files = get_filenames_from_path('testimg/')
        extract_type = "logo"

        for xml_file in xml_files:
            xml_file = "testimg/" + xml_file

            coordinates = parse_xml(xml_file, extract_type)
            if coordinates:
                print(xml_file)
                print(coordinates)

    def test_extract_and_save_logo(self):
        img_files, xml_files = get_filenames_from_path(path='testimg/')
        for img_file, xml_file in zip(img_files, xml_files):
            xml_file = "testimg/" + xml_file
            img_file = "testimg/" + img_file
            extract_and_save_images(xml_file, img_file, extract_type="logo")


if __name__ == '__main__':
    unittest.main()
