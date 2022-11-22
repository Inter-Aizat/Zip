import sys, os, shutil
import zipfile
import pyzipper

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

main_dir = application_path.split("\\")[-1]

zipPath = os.path.join(application_path, "ZIP")
copy_dir = zipPath.split("\\")[-1]

def unzip_file(file_path, decrypt_path):
    try:
        with pyzipper.AESZipFile(file_path) as f:
            # print(file_path)
            zip_filename = file_path.split("\\")[-1]
            zip_password = zip_filename.replace('.zip','')
            zip_password = zip_password.encode('utf-8')
            f.extractall(path=decrypt_path, pwd=b'Mbb@'+zip_password)
            # print(f.infolist())
            # file_content = f.read('testfile.txt')
    except:
        for dirpath, dirnames, filenames in os.walk(application_path):
            if "venv" in dirnames:
                dirnames.remove("venv")
            sub_dir = dirpath.split("\\")[-1]
            # print(sub_dir)
            if main_dir in sub_dir or "CYCLE" in sub_dir or "DAILY" in sub_dir or "MONTHLY" in sub_dir or "CHARGE CARD" in sub_dir or "PURCHASING" in sub_dir:
                continue
            job_list = dirpath.split("\\")[3]
            if "CYCLE" not in job_list and "DAILY" not in job_list and "MONTHLY" not in job_list:
                continue
            # print(filenames)
            # if "CHARGE CARD" in sub_dir or "PURCHASING" in sub_dir:
            #     for filename in filenames:
            #         print(folder_date)
            # print(dirpath.split("\\")[-1])
            # print(dirpath)
            folder_date = dirpath.split("\\")[-1]
            folder_date = folder_date.encode('utf-8')
            try:
                with pyzipper.AESZipFile(file_path) as f:
                    f.extractall(path=decrypt_path, pwd=b'Mbb@'+folder_date)
                os.remove(file_path)
            except Exception as e:
                print(e)
    else:
        os.remove(file_path)

for dirpath, dirnames, filenames in os.walk(application_path,):
    if "venv" in dirnames:
        dirnames.remove("venv")
    if "DECRYPT" not in dirpath:
        continue
    # print(dirpath)
    for filename in filenames:
        if ".zip" not in filename:
            continue
        # print(fr"{dirpath}\{filename}")
        unzip_file(fr"{dirpath}\{filename}", dirpath)
        # with pyzipper.AESZipFile(fr"{dirpath}\{filename}") as f:
        #     f.pwd = b'Mbb@011122'
        #     print(f.infolist())