import csv
from random import randint
from random import choice
import subprocess
from typing import Dict, List, Tuple, Union
from blog.models import *
from witness.models import *
from blog.categories import categories

try:
    import faker
except ImportError:
    subprocess.check_call(['pip', 'install', 'faker'])
    import faker

ROLES = [
    'VIEWER',
    'EDITOR'
]

posts: List[Post] = []
comments: List[Comment] = []
viewers: List[Viewer] = []
editors: List[Editor] = []
total_users: List[User] = []

def generate_user_raw_data(role) -> Dict:
    random = faker.Faker()

    name = random.name().split(" ")
    first_name, last_name = name[0], name[1]
    username = f"{first_name}{last_name}{randint(1, 1000)}"
    password = f"{last_name}-{first_name}@{randint(1, 1000)}"
    email = f"{random.email()}"

    return {
        "role": role,
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "password": password,
        "email": email,
    }


def create_viewer(data: Dict):
    try:
        viewer: Viewer = Viewer.objects.create(**data)
        password = data['password']

        return viewer, password
    except Exception as e:
        print(e)


def create_editor(data: Dict):
    try:
        editor: Editor = Editor.objects.create(**data)
        password = data['password']
        return editor, password
    except Exception as e:
        print(e)


def create_viewers() -> List[Viewer]:
    users = []
    passwords = []
    for i in range(10):
        data: Dict = generate_user_raw_data('VIEWER')
        user, password = create_viewer(data)
        if user:
            users.append(user)
            passwords.append(password)
    return (users, passwords)


def create_editors() -> List[User]:
    users = []
    passwords = []
    for i in range(2):
        data: Dict = generate_user_raw_data('EDITOR')
        user, password = create_editor(data)
        if user:
            users.append(user)
            passwords.append(password)
    return (users, passwords)


def create_post(editors, c) -> Union[Post, None]:
    categories_ = [c[randint(0, len(c) - 10)] for i in range(randint(1, 3))]
    title = faker.Faker().text(10)
    try:
        post: Post = Post.objects.create(
            title=title,
            content=faker.Faker().text(1000),
            author=choice(editors),
        )
        post.categories.set(categories_)

        return post

    except Exception as e:
        print(e)
        return None


def create_posts(editors, c) -> List[Post]:
    posts = []

    for i in range(30):
        post = create_post(editors, c)
        if post:
            posts.append(post)

    return posts

def create_comment(total_users, posts):
    try:
        comment: Comment = Comment.objects.create(
            content=faker.Faker().text(10),
            author=choice(total_users),
            post=choice(posts)
        )
            

        return comment
    
    except Exception as e:
        print(e)
        return None
    
def create_comments(total_users, posts):
    for i in range(60):
        comments = []
        comment = create_comment(total_users, posts)
        if comment:
            comments.append(comment)

    return comments

def export_data(
    users: List[User],
    passwords: List[str],
    posts: List[Post]
) -> bool:
    
        with open("users.csv", "w") as csvf:

            writer = csv.writer(csvf, delimiter=",")

            header = ["id", "first_name", "last_name", "username",
                      "email", "password"]

            writer.writerow(header)

            for user, password in zip(users, passwords):
                row = []
                row.append(user.id)
                row.append(user.first_name)
                row.append(user.last_name)
                row.append(user.username)
                row.append(user.email)
                row.append(password)

                writer.writerow(row)

        with open("posts.csv", "w") as csvf:

            writer = csv.writer(csvf, delimiter=",")

            # header
            header = ["title", "date_posted", "date_modified", "content", "author"]
            writer.writerow(header)

            for post in posts:
                row = []
                row.append(post.title)
                row.append(post.date_posted)
                row.append(post.date_modified)
                row.append(post.content)
                row.append(post.author)

                writer.writerow(row)

        return True



def run():

    global state, school, areas, room_profiles, room_types, users, posts
    
    c: List[Category] = [Category.objects.create(name=name[1]) for name in categories]
    print("Data generation started")

    users_v, p1 = create_viewers()
    users_e, p2 = create_editors()

    viewers = users_v
    editors = users_e

    total_users = viewers + editors
    passwords = p1 + p2

    posts = create_posts(editors, c)
    comments = create_comments(total_users, posts)
    if export_data(total_users, passwords, posts):
        print("data generation completed")

    else:

        print("data generation failed")
