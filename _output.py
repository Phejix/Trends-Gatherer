import folder_merge
import os

trends_folder = os.path.join(os.getcwd(), "temp")

#Intialize directory for dumping csv files if it doesn't already exist
if not os.path.isdir(trends_folder):
    os.makedirs(trends_folder)

folder = folder_merge.Folder(trends_folder)
folder.filename = ""


def output_trends_frame(trends_frame, filename):
    filename = clean_filename(filename = filename)

    if folder.filename == "":
        folder.filename = filename

    trends_frame.to_csv(os.path.join(trends_folder, filename))


def merge_trends():
    folder.merge(output_path = folder.filename)
    return folder.filename


def clear_temp_folder():
    folder.clear_folder()


def clean_filename(filename):
    filename = filename.replace(":", "")
    filename = filename.replace("-", "")
    return filename

