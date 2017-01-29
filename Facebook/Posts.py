import facebook
import json

access_token = 'EAACEdEose0cBAJC9Tfi2c3IFX6O4yFAKkvbIZCtFOMS9DPQH5fZABJpqi8' \
               'uDQdoBugBhwNwQvwpVC7tkq7Jf4OU3TLidjgPZBFvbJq6YhYV3yijpgJaKYO' \
               'yWw7VQi1YRzQwBK5jZBylzpBdy1jumugtdYUVCphLapjNGCJh3LAZDZD'
user = "me"
fb_posts_storage_file = 'posts.txt'
graph = facebook.GraphAPI(access_token)

profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts', limit=100)

with open(fb_posts_storage_file, 'w', encoding='utf8') as f:
    try:
        for post in posts['data']:
            f.write(post['message'] + '\n')
    except KeyError:
        print("the following post has no message:")
        print(post)
        pass
