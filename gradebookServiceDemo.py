#! usr/bin/en python3
"""Demo of gradebook service."""
import os
import requests

# Sources used:
# - https://www.twilio.com/blog/5-ways-http-requests-python
# - https://www.geeksforgeeks.org/get-post-requests-using-python/
# - https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5


# Global Constants:
PORT = os.getenv("PORT")
KEY = os.environ.get("API_KEY")
FOLDER = os.environ.get("GRADE_FOLDER")

URL = f"http://localhost:{PORT}/files?api_key={KEY}"
# URL = f"http://localhost:{PORT}/files/fl22_bob.csv"
# URL = f"http://localhost:{PORT}/files/fl22_bob.csv?api_key={KEY}"
# IF ENGR SERVER:
# URL = http://flip1.engr.oregonstate.edu:{PORT}/files


def main():
    """Request a message from message microservice"""
    print("=== Gradebook Service Demo ===\n")

    # ? HOWTO: Request a list of files
    print(f"GET {URL}")
    response = requests.get(URL)
    #
    print(f"resp.text: {response.text}")
    files = response.text.split(",")
    print(f"Files: {files}\n\n")


    # ? HOWTO: Request a specific file
    file_url = f"http://localhost:{PORT}/files/fl22_bob.csv"
    #
    print(f"GET {file_url}")
    response = requests.get(file_url)
    #
    print(f"resp.text: {response.text}\n")
    print(f"Content-Type: {response.headers['Content-Type']}\n")


    # ? HOWTO: Create a new gradebook csv file
    new_file = {"header": "date,gpa\n", "grades": "2020-03-16,3.0\n2020-06-20,3.2\n2020-09-20,3.1\n2020-11-20,3.1\n"}
    post_url = f"http://localhost:{PORT}/files/sp20_test.csv/new"
    #
    print(f"POST {post_url}")
    response = requests.post(url = post_url, json = new_file)
    #
    print(f"resp.text: {response.text}")


    pause = input("\nHit enter to unpause: ")
    # ? HOWTO: Create a new gradebook csv file
    updated_file = {"grades": "2021-03-16,3.2\n2021-06-20,3.2\n2021-09-20,3.2\n2021-11-20,3.3\n"}
    post_url = f"http://localhost:{PORT}/files/sp20_test.csv/add"
    #
    print(f"\nPOST {post_url}")
    response = requests.post(url = post_url, json = updated_file)
    #
    print(f"resp.text: {response.text}")


    # ~ Verify new file was added/updated
    print(f"\nGET {URL}")
    response = requests.get(URL)
    #
    print(f"resp.text: {response.text}")
    files = response.text.split(",")
    print(f"Files: {files}\n\n")

    return


if __name__ == "__main__":
    main()

# print(f"url: {r.url}")                      # localhost:PORT/sendMsg
# print(f"content: {r.content}")              # raw binary string
