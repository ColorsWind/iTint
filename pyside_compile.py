import glob
import os
if __name__ == "__main__":
    for qrc_file in glob.glob("*.ui"):
        file_name = qrc_file[:-3]
        os.system(f"pyside2-uic {qrc_file} -o {file_name}.py")
    for qrc_file in glob.glob("*.qrc"):
        file_name = qrc_file[:-4]
        os.system(f"pyside2-rcc {qrc_file} -o {file_name}_rc.py")