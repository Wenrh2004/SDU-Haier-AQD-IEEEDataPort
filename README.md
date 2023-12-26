# SDU-Haier-AQD-IEEEDataPort
> by **KingYen.**  
> from **QIT Software Studio**

## How to run it
- get command help
    ```shell
    make help 
    ```
- get the project run env
    ```shell
    make install
    ```
- run extract image data  
    > To choose your dataset path image type to extract and the image size to save in datasetupload/extract_img.py
    ```python
    file_path = 'datasetupload/trainimg/'
    img_type = 'logo'
    img_size = 160
    ```
    ```shell
    make run
    ```