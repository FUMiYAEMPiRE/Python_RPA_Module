import requests
import mimetypes
from logging import getLogger

logger = getLogger(__name__)


class Chatwork(object):
    def __init__(self, token):
        self.token = token

    def post_message(self, room_id, post_text):
        post_message_api_url = f'https://api.chatwork.com/v2/rooms/{room_id}/messages'
        header = {'X-ChatWorkToken': self.token}
        param = {'body': post_text}

        requests.post(post_message_api_url, headers=header, params=param)
    
    def post_file(self, room_id: str, file_path: str, post_name: str, post_text: str):
        mime = mimetypes.guess_type(file_path)[0]
        url = f'https://api.chatwork.com/v2/rooms/{room_id}/files'
        file_bin = open(file_path, 'rb')
        headers = {'X-ChatWorkToken': self.token}
        files = {
            'file': (f"{post_name}.{mime.split('/')[1]}", file_bin, mime),
            'message': post_text,
        }
        requests.post(url, headers=headers, files=files)
