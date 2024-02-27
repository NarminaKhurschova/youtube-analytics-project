import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.get_channel()['items'][0]['snippet']['title']
        self.description = self.get_channel()['items'][0]['snippet']['description']
        self.video_count = self.get_channel()['items'][0]['statistics']['videoCount']
        self.followers_count = self.get_channel()['items'][0]['statistics']['subscriberCount']
        self.views_count = self.get_channel()['items'][0]['statistics']['viewCount']
        self.url = 'https://www.youtube.com/channel/' + self.channel_id

    @staticmethod
    def get_service():
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    @property
    def channel_id(self):
        return self.__channel_id

    def j_text (self, text):
        j_text = json.dumps(text, indent=2, ensure_ascii=False)
        return j_text

    def get_channel(self):
        channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        ch_info = self.get_channel()
        print(self.j_text(ch_info))

    def to_json(self):
        attrs = vars(self)
        with open('channels_data', 'w') as file:
            json.dump(attrs, file, ensure_ascii=False)





