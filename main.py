import imaplib, email, re
import os.path
from libs.imap import Imap
from libs.attachments import parse_attachments
from ui import UI
import sys
import math
import time
import logging
from thread_pool import ThreadPool

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
        try:
            ui.add_folder(folder)
            imap.login(address, password)
            downloaded = 0
            imap.select(folder)
            uids = imap.get_uids()
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
                        logging.error(ex)
                    downloaded += 1
                    ui.update_current(attachment.filename)
                ui.set_progress(folder, i, n)
            ui.set_result(folder, 'OK')
        except Exception as ex:
            logging.error(ex)
            ui.set_result(folder, 'FAILED')

def main ():
    logging.basicConfig(filename='debug.log', filemode='w')
    with Imap(url) as imap:
        imap.login(address, password)
        logging.info('Logged in')
        folders = imap.get_folders()
        # print('Found folders:', len(folders))
        # all_uids = get_uids_and_count(imap, folders)
    ui = UI()
    # 15 - imap simultaneous connections limit

    tasks = [(process_messages, (folder, ui)) for folder in folders]
    pool = ThreadPool(max=15)
    pool.run(tasks, delay=1)
    # threads = [
    #     threading.Thread(target=process_messages, args=(folder, ui))
    #     for folder in folders[:1]]
    # for thread in threads:
    #     thread.start()

    # while True:
    #     time.sleep(0.5)
    #     for thread in threads:
    #         print(thread.is_alive())

    # So we'll implement sort of thread pool. When we have max of 15 working threads.

if __name__ == '__main__':
    main()