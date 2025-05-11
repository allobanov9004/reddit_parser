import praw
from datetime import datetime, timedelta
from collections import Counter
from settings import CLIENT_ID, CLIENT_SECRET


reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent='User_agent'
)

subreddit_name = input("Введите название сабреддита: ")
subreddit = reddit.subreddit(subreddit_name)


three_days_ago = datetime.now() - timedelta(days=3)
timestamp_three_days_ago = int(three_days_ago.timestamp())


comment_counts = Counter()
post_counts = Counter()

for submission in subreddit.new(limit=None):
    if submission.created_utc < timestamp_three_days_ago:
        break
    

    if submission.author:
        post_counts[submission.author.name] += 1
    

    submission.comments.replace_more(limit=0)  
    for comment in submission.comments.list():
        if comment.author:
            comment_counts[comment.author.name] += 1


print("\nТоп-5 пользователей по количеству комментариев:")
for user, count in comment_counts.most_common(5):
    print(f"{user}: {count} комментариев")


print("\nТоп-5 пользователей по количеству постов:")
for user, count in post_counts.most_common(5):
    print(f"{user}: {count} постов")