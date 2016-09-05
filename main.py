from instagram.client import InstagramAPI

access_token = "51630459.7575c75.acd77a3dd0fa40f984da85f5415f993f"
client_secret = "db47fc3eb69a4b57af98cd807f078deb"
client_id = "7575c756ac4240d89de542cc4b651143"

api = InstagramAPI(access_token=access_token, client_id=client_id, client_secret=client_secret)
user = api.user_search('drefaeli1')[0].id
print(user)

# generator = api.user_followed_by(as_generator=True, max_pages=None)
# for page in generator:
#         print(page)
#
# recent_media, next_ = api.user_recent_media(user_id=user, count=10)
# for media in recent_media:
#    print(media.caption)
#
# followers = []
# Get the followers list
# for p in api.user_followed_by(user_id=user, as_generator=True, max_pages=None):
#     followers.extend(p[0])


follows = api.user_follows(user)
follower = api.user_followed_by(user)
print(follower, follows)

