import datetime
import textwrap
import random

# =========================
# CONFIG SECTION
# =========================

APP_NAME = "Global War News Console"
APP_VERSION = "1.0"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "pwd1234"


# =========================
# UTILITY FUNCTIONS
# =========================

def divider():
    print("=" * 70)

def title(text):
    divider()
    print(text.center(70))
    divider()

def slow_print(text):
    for line in text.split("\n"):
        print(line)

def format_news(text):
    return textwrap.fill(text, width=68)


# =========================
# LOGIN SYSTEM
# =========================

def login(username, password):
    """Basic login function"""
    print("login attempt")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        log_event("LOGIN_SUCCESS", username)
        return True
    else:
        log_event("LOGIN_FAIL", username)
        return False


def login_prompt():
    title("LOGIN REQUIRED")

    username = input("Username: ")
    password = input("Password: ")

    if login(username, password):
        print("\nLogin success!\n")
        return True
    else:
        print("\nLogin failed\n")
        return False


# =========================
# LOGGING SYSTEM
# =========================

logs = []

def log_event(event_type, user):
    logs.append({
        "time": datetime.datetime.now(),
        "type": event_type,
        "user": user
    })


def show_logs():
    title("SYSTEM LOGS")

    for log in logs:
        print(f"{log['time']} | {log['type']} | {log['user']}")


# =========================
# WAR NEWS DATABASE
# =========================

news_db = [

    {
        "title": "Eastern Front Escalation",
        "region": "Europe",
        "content": """Heavy fighting continued along the eastern frontline today.
Multiple armored divisions were reported moving toward contested cities.
Military analysts warn the conflict could expand further if reinforcements
continue arriving in the region."""
    },

    {
        "title": "Naval Clash in Strategic Sea Route",
        "region": "Asia-Pacific",
        "content": """Naval forces from multiple countries were spotted conducting
high-intensity maneuvers in disputed waters. Satellite images indicate several
destroyers and submarines operating in close proximity."""
    },

    {
        "title": "Air Defense Systems Activated",
        "region": "Middle East",
        "content": """Air defense networks were activated across several major
cities after unidentified aircraft entered monitored airspace.
Officials claim the situation is under control."""
    },

    {
        "title": "Cyber Warfare Intensifies",
        "region": "Global",
        "content": """Cybersecurity agencies reported a surge of coordinated
attacks targeting infrastructure, financial systems, and government networks.
Experts believe the attacks may be linked to ongoing geopolitical conflicts."""
    }

]


# =========================
# NEWS FUNCTIONS
# =========================

def show_all_news():
    title("GLOBAL WAR NEWS")

    for i, news in enumerate(news_db):

        print(f"\n[{i+1}] {news['title']} ({news['region']})")
        print("-" * 70)
        print(format_news(news["content"]))


def show_news_by_region():
    region = input("Enter region: ")

    title(f"NEWS IN {region.upper()}")

    found = False

    for news in news_db:
        if news["region"].lower() == region.lower():
            print("\n" + news["title"])
            print("-" * 70)
            print(format_news(news["content"]))
            found = True

    if not found:
        print("No news found in that region.")


def random_news():
    news = random.choice(news_db)

    title("BREAKING NEWS")

    print(news["title"])
    print("-" * 70)
    print(format_news(news["content"]))


# =========================
# REPORT SYSTEM
# =========================

def situation_report():

    title("GLOBAL SITUATION REPORT")

    regions = {}

    for news in news_db:
        regions.setdefault(news["region"], 0)
        regions[news["region"]] += 1

    for region, count in regions.items():
        print(f"{region:<20} : {count} events")


# =========================
# MAIN MENU
# =========================

def main_menu():

    while True:

        title(APP_NAME)

        print("1. Show All War News")
        print("2. Show News by Region")
        print("3. Random Breaking News")
        print("4. Situation Report")
        print("5. System Logs")
        print("6. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            show_all_news()

        elif choice == "2":
            show_news_by_region()

        elif choice == "3":
            random_news()

        elif choice == "4":
            situation_report()

        elif choice == "5":
            show_logs()

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid option")

        input("\nPress Enter to continue...")


# =========================
# APP BOOT
# =========================

def boot_screen():

    title(APP_NAME)
    print(f"Version: {APP_VERSION}")
    print("Initializing modules...")
    print("Loading news database...")
    print("Connecting intelligence feeds...")
    print("System ready.")


# =========================
# MAIN PROGRAM
# =========================

def main():

    boot_screen()

    if login_prompt():
        main_menu()
    else:
        print("Access denied.")


if __name__ == "__main__":
    main()