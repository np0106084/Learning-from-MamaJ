
import os
import json


def youtube_util():
    """
    1. download youtube playlist
    2. get playlist information from googleapi
    3. get file details from the download folder
    4. create folder using the same name as playlist
    5. move files to the new playlist folder
    6. rename files with playlist item order
    """
    download_dir = "C:\\Users\\mdari\\Downloads\\python_learning_download"
    playlist_id = 'PL-osiE80TeTuRUfjRe54Eea17-YfnOOAx'
    playlist_file_info = "C:\\source\\001_learning\\resource\\git_playlistItems.json"
    folder_name = 'Git Tutorial'
    file_details = get_file_details(download_dir)
    playlist_info = get_playlist_info(playlist_id, playlist_file_info)
    move_files_to_folder(file_details, playlist_info)



def dl_youtube():
    pass


def get_playlist_info(playlist_id, playlist_file_info):
    playlist_info = {}
    with open(playlist_file_info, 'r', encoding="utf8") as f:
        data = json.load(f)
        print(len(data['items']))
        for item in data['items']:
            title = item["snippet"]['title'].strip()
            video_id = item["snippet"]["resourceId"]["videoId"].strip()
            playlist_info[video_id] = title
    # print(playlist_info)
    return playlist_info



def get_file_details(download_dir): # passing by location
    print(os.getcwd())
    os.chdir(download_dir)
    file_details = dict()

    for f in os.listdir():
        f_titleId, f_ext = os.path.splitext(f)
        try:
            # ind_und = f_titleId[::-1].index('-')
            ind_und = 11
        except:
            print(f, 'will be skipped')
            continue
        ind_last_und = (len(f_titleId)-ind_und)
        f_title = f_titleId[:(ind_last_und-1)]
        f_id = f_titleId[ind_last_und:]
        file_details[f_id] = [f_title, f]
        
    # print(file_details)
    return file_details





def move_files_to_folder(file_details, playlist_info):
    # print(file_details.keys())
    # print(playlist_info.keys())
    # create folder - get folder name as arg
    for key, value in playlist_info.items():
        # print(key, len(key))
        if key in file_details.keys():
            print(key, ' - key found in file_details')
            # build new_file_name
            # rename and move file into the folder
        else:
            print(key, ' - key not found in file_details')

      



def renaming_files():
    pass


if __name__ == "__main__":
    youtube_util()
