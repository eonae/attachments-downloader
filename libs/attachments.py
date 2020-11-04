from email.message import EmailMessage, Message
import email.header

import base64
import re
import os
import sys
import logging

class Attachment:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content
        self.unique_id = 0

    def save (self):
        ext = get_extension(self.filename)
        dirname = os.path.join('./attachments', ext[1:] if ext else '!other').lower()
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        fullpath = os.path.join(dirname, self.filename)
        if os.path.exists(fullpath):
            self.unique_id += 1
            fullpath += f'-{self.unique_id}'
        with open(fullpath, 'wb') as file:
            file.write(self.content)


def get_extension (filename: str):
    _, ext = os.path.splitext(filename)
    return ext


def is_attachment (part: Message):
    return part.get_content_disposition() == 'attachment'

def decode_filename (filename):
    """
        May need to decode from base64 and then from UTF-8 or KOI8-R.
        Besides filename can be splitted into parts.
    """
    mime_words = email.header.decode_header(filename)
    result = ''.join([ 
        word.decode(encoding or 'utf-8') if isinstance(word, bytes) else word
        for word, encoding in mime_words ])
    return result;

def parse_attachments (message: Message):
    result = []
    for i, part in enumerate(message.walk()):
        try:
            if is_attachment(part):
                filename = decode_filename(part.get_filename())
                content = part.get_payload(decode=True)
                result.append(Attachment(filename, content))
        except Exception as ex:
            logging.error(ex)
    return result