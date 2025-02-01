import requests
import time
import os

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Get Facebook Access Token from User
def get_token():
    os.system("clear")
    print(f"{CYAN}🔹 Facebook Security Scanner v2.0 🔹{RESET}")
    token = input(f"{YELLOW}🔑 Enter your Facebook Access Token: {RESET}")
    return token

# Check Facebook App Permissions
def check_facebook_apps(token):
    url = f"https://graph.facebook.com/me/permissions?access_token={token}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        permissions = data.get("data", [])

        if permissions:
            print(f"\n{CYAN}🔍 Authorized Permissions on Your Facebook Account:{RESET}\n")
            
            risky_permissions = [
                "email", "manage_pages", "publish_pages", "ads_management",
                "user_friends", "user_posts", "user_photos", "user_videos"
            ]
            risky_found = False

            for perm in permissions:
                status = perm["status"]
                color = GREEN if status == "granted" else RED
                print(f"{color}✅ {perm['permission']} - {status}{RESET}")

                if perm["permission"] in risky_permissions and status == "granted":
                    print(f"{RED}⚠️ WARNING: '{perm['permission']}' might be risky! Please check.{RESET}")
                    risky_found = True

            if risky_found:
                print(f"\n{RED}🚨 Please remove suspicious apps from **Facebook Settings > Apps & Websites**!{RESET}")
            else:
                print(f"\n{GREEN}✅ No risky permissions found. Your account is safe!{RESET}")

        else:
            print(f"{GREEN}✅ No authorized apps found on your account.{RESET}")
    elif response.status_code == 400:
        print(f"{RED}❌ Invalid Token! Please enter a valid Access Token.{RESET}")
    else:
        print(f"{RED}❌ Failed to fetch data from Facebook API. Check your Access Token.{RESET}")

# Main Menu
def menu():
    while True:
        os.system("clear")
        print(f"""{CYAN}
🔹🔹 Facebook Security Scanner v2.0 🔹🔹
====================================
{WHITE}1️⃣ Check Facebook App Permissions
2️⃣ View Facebook Security Guide
3️⃣ Exit
===================================={RESET}
        """)
        choice = input(f"{YELLOW}📌 Enter your choice (1/2/3): {RESET}")

        if choice == "1":
            token = get_token()
            check_facebook_apps(token)
            input(f"\n{CYAN}🔘 Press Enter to return to the menu...{RESET}")

        elif choice == "2":
            os.system("clear")
            print(f"""{GREEN}
🔹🔹 Facebook Security Guide 🔹🔹
=================================
✅ Remove suspicious apps from **Settings > Apps & Websites**
✅ Enable **Two-Factor Authentication (2FA)**
✅ Turn on **Login Alerts**
✅ Use a **strong and unique password**
================================={RESET}
            """)
            input(f"{CYAN}🔘 Press Enter to return to the menu...{RESET}")

        elif choice == "3":
            print(f"{GREEN}✅ Exiting program...{RESET}")
            time.sleep(1)
            exit()
        else:
            print(f"{RED}❌ Invalid input! Please enter 1, 2, or 3.{RESET}")
            time.sleep(1)

# Run the program
menu()