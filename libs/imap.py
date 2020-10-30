from imaplib import IMAP4_SSL
import email
import re

class Imap(IMAP4_SSL):
        
    def get_folders (self):
        _, raw = super().list()
        return [re.search(r'"[^"]*"$', r.decode()).group() for r in raw]

    def get_uids (self):
        _, raw = super().uid('search', None, 'ALL')
        return raw[-1].split()

    def get_message(self, uid):
        # print(f'Getting {uid}')
        _, raw = super().uid('fetch', uid, '(RFC822)')
        content = raw[0]
        return email.message_from_bytes(content[1]) if content else None