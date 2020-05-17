import praw
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)
print()
print("Delete comments/posts with negative/zero karma")
reddit = praw.Reddit(client_id='',
             client_secret='',
             password='',
             user_agent='comment viewer / deleter',
             username='')

comments = reddit.user.me().comments.new(limit=None)
i=0
print("Start deleting comments...")
for comment in comments:
    if comment.score <= 0:
        i=i+1
        print("[",comment.body,"]","is being deleted.")
        comment.delete()
print(i," Comment(s) completed")
print("Start deleting posts...")
i=0
posts=reddit.user.me().submissions.new(limit=None)
for post in posts:
    if post.score <= 0:
       i=i+1
       print("[",post.title,"]","is being deleted.")
       post.delete()
print(i," Post(s) completed")
print()

