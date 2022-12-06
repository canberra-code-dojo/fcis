import datetime, json, requests

def user_count(posts):
    return len({post["userId"] for post in posts})

def summarise(post_count, user_count):
    return json.dumps({
        "posts": post_count,
        "users": user_count,
        "mean_posts_per_user": round(post_count / user_count)
    })

def store_cms_summary_report():
    print("Getting CMS data")
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        try:
            posts = json.loads(response.text)
            print("CMS data has %s records" % len(posts))
        except Exception as e:
            print('No valid JSON response from CMS, error %s' % type(e).__name__)
        today = datetime.date.today().isoformat()
        report_filename = "cms-" + today + ".json"
        with open(report_filename, "w") as summary_file:
            summary_file.write(summarise(len(posts), user_count(posts)))
            print("Wrote CMS report", flush=True)
    else:
        print('Error getting data from CMS, response code %s' % response.status_code)


if __name__ == '__main__':
    store_cms_summary_report()
