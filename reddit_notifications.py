import praw
import webbrowser
from praw.models import Comment
class Py3status:

    def reddit_notifications(self):
        reddit = praw.Reddit(client_id='CLIENTIDGOESHERE',
                 client_secret='SECRETGOESHERE',
                 user_agent='RedditNotifications by /u/MindfulProtons and /u/Sollybird',
                 username='USERNAME',
                 password='PASSWORD')
        message_count = 0
        for item in reddit.inbox.unread(limit=None):
            message_count += 1
        if message_count == 1:
            final_message = str(message_count) + " reddit notification"
        else:
            final_message = str(message_count) + " reddit notifications"
        return {
            'full_text': final_message,
            'cached_until': self.py3.time_in(10)
        }
    def on_click(self, event):
        webbrowser.open('https://reddit.com/message/inbox')
