import imaplib, email, re
import os.path
from libs.imap import Imap
from libs.attachments import parse_attachments
import sys
import math
import time

address = 'eonae.white@gmail.com'
password = 'pvjomphvchdftuiz'
url = 'imap.gmail.com'

def get_uids_and_count (imap, folders):
    all_uids = {}
    for folder in folders:
        try:
            imap.select(folder)
            uids = imap.get_uids()
            all_uids[folder] = uids
            print(f'Messages in {folder}: {len(uids)}')
        except Exception as ex:
            print(f'Error while processing folder {folder}', ex)
    total = len([uids for uids in all_uids.values() for uid in uids])
    print('TOTAL:', total)
    return all_uids

def update_progress_bar (x, n):
    percent = math.ceil((x + 1) * 100/ n)
    sys.stdout.write('\u001b[1000D' + 'Processed: ' + str(percent) + '%')
    sys.stdout.flush()

def main ():
    with Imap(url) as imap:
        imap.login(address, password)
        print('Logged in')
        folders = imap.get_folders()
        print('Found folders:', len(folders))
        all_uids = get_uids_and_count(imap, folders)
        for folder in folders:
            downloaded = 0
            imap.select(folder)
            print(f'Downloading attachments from {folder}... ')
            n = len(all_uids[folder])
            for i, uid in enumerate(all_uids[folder]):
                message = imap.get_message(uid)
                if not message:
                    print(f'Message {uid} is none')
                    continue
                for attachment in parse_attachments(message):
                    try:
                        attachment.save()
                    except Exception as ex:
                        print(ex, attachment)
                    downloaded += 1
                update_progress_bar(i, n)
            print(f'\nDownloaded {downloaded} attachments from {n} messages.')

if __name__ == '__main__':
    main()