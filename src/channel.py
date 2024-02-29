import json
import os
from googleapiclient.discovery import build




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

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return int(self.followers_count) + int(other.followers_count)

    def __sub__(self, other):
        return int(self.followers_count) - int(other.followers_count)

    def __sub__(self, other):
        return int(other.followers_count) - int(self.followers_count)

    def __gt__(self, other):
        return int(self.followers_count) > int(other.followers_count)

    def __ge__(self, other):
        return int(self.followers_count) >= int(other.followers_count)

    def __lt__(self, other):
        return int(self.followers_count) < int(other.followers_count)

    def __le__(self, other):
        return int(self.followers_count) <= int(other.followers_count)

    def __eq__(self, other):
        return int(self.followers_count) == int(other.followers_count)

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))
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
        with open('moscowpython', 'w') as file:
            json.dump(attrs, file, ensure_ascii=False)





