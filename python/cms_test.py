import datetime, json, os, unittest
import cms

today = datetime.date.today().isoformat()
print("todays date is %s" % today)
report_filename = "cms-" + today + ".json"

print("Deleting report file")
try:
    os.remove(report_filename)
except Exception as e:
    print("No report file to remove")

class TestCMS(unittest.TestCase):
    cms.store_cms_summary_report()

    def test_cms_writes_report_file(self):
        with open(report_filename, "r") as report_file:
            report = json.load(report_file)
        self.assertIn("posts", report, "report file not found")

    def test_report_file_contains_cms_data(self):
        with open(report_filename, "r") as report_file:
            report = json.load(report_file)
        self.assertEqual(100, report["posts"], "posts should be 100")
        self.assertEqual(10, report["users"], "users should be 10")

    def test_calculate_mean_users(self):
        with open(report_filename, "r") as report_file:
            report = json.load(report_file)
        self.assertEqual(10, report["mean_posts_per_user"], "average posts per user should be 10")

    def test_user_count(self):
        posts_with_one_user = [{"userId": 1}]
        self.assertEqual(1, cms.user_count(posts_with_one_user), "user count should be 1")

        posts_with_two_users = [{"userId": 1}, {"userId": 2}, {"userId": 1}]
        self.assertEqual(2, cms.user_count(posts_with_two_users), "user count should be 2")

if __name__ == '__main__':
    unittest.main()
