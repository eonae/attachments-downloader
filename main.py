import imaplib, email, re
from imap import Imap

address = 'eonae.white@gmail.com'
password = 'pvjomphvchdftuiz'
url = 'imap.gmail.com'

try:
    with Imap(url) as imap:
        imap.login(address, password)
        folders = imap.get_folders()
        print('Found folders:', len(folders))
        all_uids = []
        for folder in folders[0:2]:
            try:
                imap.select(folder)
                uids = imap.get_uids()
                for uid in uids:
                    all_uids.append(uid)
            except Exception as ex:
                print(f'Error while processing folder {folder}', ex)
        print('Total messages:', len(all_uids))
        with open('results', 'w') as file:
            for uid in all_uids[:10]:
                message = imap.get_message(uid)
                file.write(message.as_string())

except Exception as ex:
    print(ex)
