import json
from datetime import datetime

class IssueTracker:
    def __init__(self, filename="issues.json"):
        self.filename = filename
        self.issues = []
        self.load_issues()

    def add_issue(self, title, description, priority="Medium"):
        issue = {
            "id": len(self.issues) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "status": "Open",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.issues.append(issue)
        self.save_issues()
        print("✅ Issue added.")

    def list_issues(self, status_filter=None):
        print("\n📋 Issues:")
        for issue in self.issues:
            if status_filter and issue["status"] != status_filter:
                continue
            print(f"[#{issue['id']}] {issue['title']} ({issue['priority']}) - {issue['status']}")
            print(f"    📝 {issue['description']}")
            print(f"    📅 Created: {issue['created_at']}\n")

    def resolve_issue(self, issue_id):
        for issue in self.issues:
            if issue["id"] == issue_id:
                issue["status"] = "Closed"
                self.save_issues()
                print(f"✅ Issue #{issue_id} marked as resolved.")
                return
        print("❌ Issue not found.")

    def save_issues(self):
        with open(self.filename, "w") as f:
            json.dump(self.issues, f, indent=4)

    def load_issues(self):
        try:
            with open(self.filename, "r") as f:
                self.issues = json.load(f)
        except FileNotFoundError:
            self.issues = []

def main():
    tracker = IssueTracker()

    while True:
        print("\n=== Issue Tracker ===")
        print("1. Add Issue")
        print("2. View All Issues")
        print("3. View Open Issues")
        print("4. View Closed Issues")
        print("5. Resolve Issue")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter issue title: ")
            description = input("Enter issue description: ")
            priority = input("Enter priority (Low/Medium/High): ").capitalize()
            tracker.add_issue(title, description, priority)

        elif choice == "2":
            tracker.list_issues()

        elif choice == "3":
            tracker.list_issues(status_filter="Open")

        elif choice == "4":
            tracker.list_issues(status_filter="Closed")

        elif choice == "5":
            try:
                issue_id = int(input("Enter issue ID to resolve: "))
                tracker.resolve_issue(issue_id)
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == "6":
            print("👋 Exiting Issue Tracker.")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()



