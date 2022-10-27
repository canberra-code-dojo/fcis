# Contributing

Contributions are welcome. If you would like to contribute an implementation of the base (unrefactored) code in another language, please send a PR, putting the new language code in its own folder as I have done with the Node example. The code should follow the same kind of naive, imperative, mixed together - i.e. unmodularised - style that the other implementations do.

I will link your implementation in this README and mention you as the author by git username, and any other identification you wish me to provide.

## Contribution Requirements

In order to help contributors with providing a compliant version of the base kata, here are the requirements that the original was developed against:

1. The summary report generator (GENERATOR) MUST get CMS data from the following URI: http://jsonplaceholder.typicode.com/posts 
1. The GENERATOR MUST calculate i) the number of posts, ii) the number of distinct users, iii) the mean number of posts per user (rounded to nearest whole number)
1. The summary report (REPORT) MUST be written to a file on disk with the name `cms-<date>.json` where date is today's date in the form YYYY-MM-DD
1. The REPORT MUST be formatted as a JSON object of the form '{ "posts": 0, "users": 0, "mean_posts_per_user": 0 }'
1. The GENERATOR MUST log the string 'Getting CMS data' when getting the data from the CMS
1. The GENERATOR MUST log the string 'CMS data has: <n> records', where n is the number of posts
1. The GENERATOR MUST log the string 'Wrote CMS report' after the REPORT is written to disk
1. If the GENERATOR cannot contact the CMS an error MUST be reported
1. If the GENERATOR does not recieve valid JSON data from the CMS an error MUST be reported
1. If the GENERATOR cannot write the report to disk an error MUST be reported
1. The summary report generator test suite (TESTS) MUST delete a previous run's REPORT before running the GENERATOR
1. The TESTS MUST test that a REPORT of the right name `cms-<date>.json` is written
1. The TESTS MUST test that the report correctly contains 100 posts and 10 users
1. The TESTS MUST test that the mean number of posts per user is correctly calculated to be 10
