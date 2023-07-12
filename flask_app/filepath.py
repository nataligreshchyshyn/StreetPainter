import os

def process_shapefiles(directory_path):
    """
    Processes shapefiles in a given directory and returns the path of the first shapefile found.

    Args:
        directory_path (str): The path to the directory containing the shapefiles.

    Returns:
        str: The path of the first shapefile found, or None if no shapefiles are found.
    """
    files = os.listdir(directory_path)

    for file_name in files:
        if file_name.endswith(".shp"):
            file_path = os.path.join(directory_path, file_name)
            return file_path

    return None
