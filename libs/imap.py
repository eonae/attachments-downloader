from imaplib import IMAP4_SSL
import email
import re

from retry import retry

class Imap(IMAP4_SSL):
        
    @retry(1, 10)
    def get_folders (self):
        _, raw = super().list()
        return [re.search(r'"[^"]*"$', r.decode()).group() for r in raw]

    @retry(1, 10)
    def get_uids (self):
        _, raw = super().uid('search', None, 'ALL')
        return raw[-1].split()

    @retry(1, 10)
    def get_message(self, uid):
        # print(f'Getting {uid}')
        _, raw = super().uid('fetch', uid, '(RFC822)')
        content = raw[0]
        return email.message_from_bytes(content[1]) if content else None