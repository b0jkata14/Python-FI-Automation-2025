import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts(limit=3):
    params = {
        "_limit": limit
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        print("Request URL:", response.url)
        print("Status code:", response.status_code)

        response.raise_for_status()  # автоматично вдига exception при 4xx / 5xx

        data = response.json()
        print("Response type:", type(data))

        for post in data:
            print(f"- {post['id']}: {post['title']}")

    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
    except requests.exceptions.Timeout:
        print("Request timed out!")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


def timeout_demo():
    try:
        print("\nCalling delayed endpoint...")
        requests.get("https://httpbin.org/delay/3", timeout=1)
    except requests.exceptions.Timeout:
        print("Request timed out!")


fetch_posts(limit=3)
timeout_demo()
