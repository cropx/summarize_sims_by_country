import time

import PyInstaller.__main__
import zipfile
import os
import shutil
from gui import Gui

gui = Gui()

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--icon=icon.ico',
    '--noconsole',
    '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\main.py;.',
    '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\gui.py;.',
    '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\icon.ico;.',
    '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\picture_logo.png;.',
    '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\cropx_logo.png;.',
    '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\'
                  'read_ext_files.py;.',
    # '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\'
    #               'TELE2_pdf_converted_to_excel.xlsx;.',
    # '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\'
    #               'Telit Next Profile 2 - Global.xlsx;.'
    # '--add-data', 'C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\'
    #               'compare_country_table.xlsx;.'
])


def rename_main():
    time.sleep(3)
    os.rename('dist\\main.exe', 'dist\\SimBa.exe')


def copy_files_to_dist():
    source = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\main.py"
    target = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\dist\\main.py"
    shutil.copyfile(source, target)
    source = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\gui.py"
    target = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\dist\\gui.py"
    shutil.copyfile(source, target)
    source = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\icon.ico"
    target = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\dist\\icon.ico"
    shutil.copyfile(source, target)
    source = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\picture_logo.png"
    target = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\dist\\picture_logo.png"
    shutil.copyfile(source, target)
    source = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\cropx_logo.png"
    target = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\dist\\cropx_logo.png"
    shutil.copyfile(source, target)
    source = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\read_ext_files.py"
    target = r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\dist\\read_ext_files.py"
    shutil.copyfile(source, target)
    source = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"compare_country_table.xlsx")
    target = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\dist\\"
              r"compare_country_table.xlsx")
    shutil.copyfile(source, target)
    source = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"TELE2_pdf_converted_to_excel.xlsx")
    target = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"dist\\TELE2_pdf_converted_to_excel.xlsx")
    shutil.copyfile(source, target)
    source = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"Telit Next Profile 2 - Global.xlsx")
    target = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"dist\\Telit Next Profile 2 - Global.xlsx")
    shutil.copyfile(source, target)
    source = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"countries")
    target = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"dist\\countries")
    shutil.copytree(source, target)
    source = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"APPENDIX II - AREA OF TERRITORY Tele 2 Type 1_01062024_.pdf")
    target = (r"C:\\Users\\TalorKeren\\OneDrive - CropX\\Talor\\scripts\\select_sim_by_country\\"
              r"dist\\APPENDIX II - AREA OF TERRITORY Tele 2 Type 1_01062024_.pdf")
    shutil.copyfile(source, target)


def zip_dist_folder(dist_folder_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dist_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, dist_folder_path))


version = gui.version_def()
rename_main()
copy_files_to_dist()

# Assuming your dist folder is at './dist' and you want to create 'dist.zip'
zip_dist_folder('./dist', f'SimBa_ver_{version}.zip')
