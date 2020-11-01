import imaplib, email, re
import os.path
from libs.imap import Imap
from libs.attachments import parse_attachments
from ui import UI
import sys
import math
import time
import threading

address = 'eonae.white@gmail.com'
password = 'pvjomphvchdftuiz'
url = 'imap.gmail.com'

# def get_uids_and_count (imap, folders):
#     all_uids = {}
#     for folder in folders:
#         try:
#             imap.select(folder)
#             uids = imap.get_uids()
#             all_uids[folder] = uids
#             print(f'Messages in {folder}: {len(uids)}')
#         except Exception as ex:
#             print(f'Error while processing folder {folder}', ex)
#     total = len([uids for uids in all_uids.values() for uid in uids])
#     print('TOTAL:', total)
#     return all_uids

# Add events
# Curried functions instead ui class
def process_messages(folder, ui: UI):
    with Imap(url) as imap:
        ui.add_folder(folder)
        imap.login(address, password)
        downloaded = 0
        imap.select(folder)
        uids = imap.get_uids()
        # print(f'Downloading attachments from {folder}... ')
        n = len(uids)
        ui.set_messages_count(folder, n)
        for i, uid in enumerate(uids):
            message = imap.get_message(uid)
            if not message:
                print(f'Message {uid} is none')
                continue
            for attachment in parse_attachments(message):
                try:
                    attachment.save()
                except Exception as ex:
                    pass
                downloaded += 1
                ui.update_current(attachment.filename)
            ui.set_progress(folder, i, n)
        ui.set_result(folder, 'OK')
        # ui.log(f'\nFolder: {folder} - Downloaded {downloaded} attachments from {n} messages.')

def main ():
    with Imap(url) as imap:
        imap.login(address, password)
        print('Logged in')
        folders = imap.get_folders()
        # print('Found folders:', len(folders))
        # all_uids = get_uids_and_count(imap, folders)
    ui = UI()
    for folder in folders:
        process_messages(folder, ui)

if __name__ == '__main__':
    main()