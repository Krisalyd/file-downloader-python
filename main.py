import requests
from zipfile import ZipFile
import os

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def main():
    # The "downloads" directory will be created in the project's current directory
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    # A GET request will be made for each URL in the list, if the request succeed (Status code == 200), the file will be
    # downloaded and go through Unzip process to obtain the csv file. At the end the .Zip will be deleted.
    for file_url in download_uris:
        file_name = file_url[file_url.rfind('/') + 1:]
        web_path = requests.get(file_url)
        if web_path.status_code == 200:
            print(f"file {file_name} OK: {web_path}")
            open(f'downloads/{file_name}', "wb").write(web_path.content)
            with ZipFile(f'downloads/{file_name}', 'r') as zip_object:
                zip_object.extract(file_name.replace('.zip', '.csv'), 'downloads/')
            os.remove(f'downloads/{file_name}')

        else:
            print(f"Possible connection error with file {file_name}: {web_path}")
    pass


if __name__ == '__main__':
    main()
