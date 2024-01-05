# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import ftplib
import os

from settings import server_ftp, login_ftp, password_ftp, url_site


def ftp_jobs(image):
    link = ''

    try:

        file_name = image.split(os.sep)[-1]

    except Exception as es:
        print(f'Не могу вытащить имя файла "{es}" из картинки для ftp')

        return link

    try:

        session = ftplib.FTP(server_ftp, login_ftp, password_ftp)

        file = open(image, 'rb')  # file to send

        session.storbinary(f"STOR {file_name}", file)  # send the file

        file.close()  # close file and FTP

        session.quit()

        link = f'{url_site}/{file_name}'

    except Exception as es:
        print(f'Не могу залить картинку на ftp сервер "{es}"')

        return link

    return link
