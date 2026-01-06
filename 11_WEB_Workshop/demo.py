import requests


BASE_URL = "https://jsonplaceholder.typicode.com"
POSTS_ENDPOINT = f"{BASE_URL}/posts"


def get_all_posts():
    response = requests.get(f"{POSTS_ENDPOINT}")
    response.raise_for_status()
    return response.json()


def get_posts_with_query_params(params):
    response = requests.get(POSTS_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def get_post(post_id):
    response = requests.get(f"{POSTS_ENDPOINT}/{post_id}")
    response.raise_for_status()
    return response.json()


def create_post(user_id, title, body):
    payload = {
        "userId": user_id,
        "title": title,
        "body": body,
    }

    response = requests.post(POSTS_ENDPOINT, json=payload)
    response.raise_for_status()
    return response.json()


def update_post(post_id, user_id, title, body):
    payload = {
        "id": post_id,
        "userId": user_id,
        "title": title,
        "body": body,
    }

    response = requests.put(f"{POSTS_ENDPOINT}/{post_id}", json=payload)
    response.raise_for_status()
    return response.json()


def patch_post(post_id, fields):
    response = requests.patch(f"{POSTS_ENDPOINT}/{post_id}", json=fields)
    response.raise_for_status()
    return response.json()


def delete_post(post_id):
    response = requests.delete(f"{POSTS_ENDPOINT}/{post_id}")
    response.raise_for_status()
    return response.status_code


# GET single post
post = get_post(4)
print("GET post:", post)


# GET all posts
posts = get_all_posts()
print("GET posts:", posts)


# POST
new_post = create_post(
    user_id=1,
    title="Wow new title!",
    body="NEW POST body",
)

print("Created post:", new_post)


# PUT
updated_post = update_post(
    post_id=4,
    user_id=1,
    title="Updated title",
    body="Updated body",
)

print("Updated post:", updated_post)


# PATCH
patched_post = patch_post(4, {"userId": 5})

print("Patched post:", patched_post)


# DELETE
status = delete_post(3)

print("Delete status code:", status)


# QUERY PARAMS
filtered_posts = get_posts_with_query_params({
    "userId": 2,
    "title": "et ea vero quia laudantium autem",
})

print("Filtered posts:", filtered_posts)