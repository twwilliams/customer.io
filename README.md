# Customer.io application question

Code for customer.io question in application. This code answers three questions:

1. How many total open issues are there across all repositories?
2. Sort the repositories by date updated in descending order.
3. Which repository has the most watchers?

## Requirements

- Python 3
- pip
- _Optional:_ virtualenv module

## To run this code

1. Clone this repository
2. _(Optional, though recommended):_ Create a virtual environment to hold
   the dependencies and activate it. If you need more instructions on
   virtual environments in Python, see
   [Python Virtual Environments - a Primer](https://realpython.com/blog/python/python-virtual-environments-a-primer/)
3. Run `pip install -r requirements.txt`
4. Run the program with `python3 repo_info.py`

## Future enhancements
- **Add tests.** I wasn't sure how far to go with this exercise so I
  timeboxed it. Proper unit testing would have required mocking the
  network calls to the GitHub API.

- **Cache the results from the GitHub API.** Since this is not using
  any authentication, it is rate-limited to 60 requests per hour. The
  data returned isn't likely to change that often, either, so there is
  no need to always query live data.

