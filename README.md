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

Since this is a script and not a full-blown application or a reusable
library, I have kept the error-handling to a minimum and haven't added
tests so that the flow is clear.

As a script, it would be nice to make the **organization name a
command-line option** rather than requiring editing the script.

To go beyond a script to a library or richer application, I would need
to start with:

- **Add tests.** Proper unit testing would required mocking the
  network calls to the GitHub API and then we would need integration
  and end-to-end tests as well.

- **Add error handling.** While there is some precedent in Python to
  keep error handling to a minimum, it shouldn't be as minimal as I
  have left it here.

- **Cache the results from the GitHub API.** Since this is not using
  any authentication, it is rate-limited to 60 requests per hour. The
  data returned isn't likely to change that often, either, so there is
  no need to always query live data.

