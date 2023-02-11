#! /usr/bin/en python3
"""Client for messaging server."""
# Sources used:
# - https://www.twilio.com/blog/5-ways-http-requests-python
# - https://www.geeksforgeeks.org/get-post-requests-using-python/
# - https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
# - https://blog.hubspot.com/website/what-is-rest-api

import os
import requests


# Global Constants:
PORT = os.getenv("PORT")
URL = f"http://localhost:{PORT}/sendMsg"


def main():
    """Request a message from message microservice"""
    print("=== Gradebook Service Demo ===")

    print(f"\nSending GET message request...")
    r = requests.get(URL)

    print(f"\nMessage recieved...")
    print(f"Msg: {r.text}")


if __name__ == "__main__":
    main()

    # print(f"url: {r.url}")                      # localhost:PORT/sendMsg
    # print(f"content: {r.content}")              # raw binary string