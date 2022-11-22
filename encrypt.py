import sys, os, shutil
import zipfile
import pyzipper


if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

# print(application_path)
main_dir = application_path.split("\\")[-1]
# print(main_dir)
# print(main_dir)

zipPath = os.path.join(application_path, "ZIP")
copy_dir = zipPath.split("\\")[-1]
# print(application_path)
# print(copy_dir)

def zip_folder(folder_path, output_path, password):
    zip_password = password.encode('utf-8')
    parent_folder = os.path.dirname(folder_path)
    contents = os.walk(folder_path)
    # print(parent_folder)
    try:
        zip_file = pyzipper.AESZipFile(f'{folder_path}.zip','w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES)
        zip_file.pwd=b'Mbb@'+zip_password
        print(zip_file.pwd)
        for root, folders, files in contents:
#             # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                # print ("Adding '%s' to archive." % absolute_path)
                zip_file.write(absolute_path, relative_path)
        # print ("'%s' created successfully." % output_path)

    except IOError as message:
        print (message)
        sys.exit(1)
    except OSError as message:
        print(message)
        sys.exit(1)
    except zipfile.BadZipfile as message:
        print (message)
        sys.exit(1)
    finally:
        zip_file.close()
        shutil.rmtree(folder_path)

for dirpath, dirnames, filenames in os.walk(application_path,):
    if "venv" in dirnames:
        dirnames.remove("venv")
    sub_dir = dirpath.split("\\")[-1]
    if main_dir in sub_dir or "CYCLE" in sub_dir or "DAILY" in sub_dir or "MONTHLY" in sub_dir or "CHARGE CARD" in sub_dir or "PURCHASING" in sub_dir:
        continue
    job_list = dirpath.split("\\")[3]
    if "CYCLE" not in job_list and "DAILY" not in job_list and "MONTHLY" not in job_list:
        continue
    if job_list == "CYCLE":
        date_dir = dirpath.split("\\")[5]
    else:
        date_dir = dirpath.split("\\")[4]
    try:
        if dirpath.split("\\")[6]:
            continue
    except:
        pass
    if sub_dir == date_dir:
        continue
    # print(dirpath + " " + date_dir)
    zip_folder(dirpath, dirpath+".zip", date_dir)