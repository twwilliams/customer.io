"""
Script that answers three questions about customer.io's public repositories:

1. How many total open issues are there across all repositories?
2. Sort the repositories by date updated in descending order.
3. Which repository has the most watchers?
"""
from collections import namedtuple
from operator import attrgetter

import requests

Repository = namedtuple('Repository',
                        'name url updated open_issues watchers')


def get_next_page_link(link_header):
    """
    The link_header will be of the form:
    <(url)>; rel="(relation)", <(url2)>; rel="<(relation2)>"

    Where:
    (url) will be a pointer to a page on GitHub's API
    (relation) will be first, next, prev, or last
    (url2) will be a pointer to a different page on GitHub's API

    A link_header will always have two pairs of URLs. Next and last are
    paired and first and prev are paired.

    :param link_header: The content of the Link: header from GitHub API
    :return: url for the next page of the API results or None if no next link
    """
    next_page_url = None
    for url in link_header.split(', '):
        if 'rel="next"' in url:
            next_page_url = url.split('; ')[0].strip('<>')

    return next_page_url


def all_repos_data(url):
    """
    Gets all repos for a given user/organization and returns the full data
    set as a generator.
    :param url: URL to begin querying the GitHub API
    :return: Generator with full set of data for all repositories
    """
    more_pages = True

    while more_pages:
        repos_response = requests.get(url)
        repos = repos_response.json()

        for repo in repos:
            yield repo

        link_header = repos_response.headers.get('Link', None)

        if link_header:
            url = get_next_page_link(repos_response.headers['Link'])
            if not url:
                more_pages = False
        else:
            more_pages = False


def all_repos_filtered(start_url):
    """
    Filter data for repositories from GitHub API down to relevant data
    :param start_url: The URL for the customerio repositories
    :return: Repository namedtuple
    """
    for repo in all_repos_data(start_url):
        yield Repository(
            repo['full_name'],
            repo['url'],
            repo['updated_at'],
            repo['open_issues'],
            repo['watchers']
        )


def main():
    """
    Entry point to the script. Prints desired output to the console.
    """

    repos_first_page_url = 'https://api.github.com/orgs/customerio/repos'

    repos = all_repos_filtered(repos_first_page_url)

    issues_count = 0
    watchers_max = {'name': '', 'watchers': 0}

    # No need to convert to datetime object thanks to sortable format
    # returned by GitHub API
    repos = sorted(repos, key=attrgetter('updated'), reverse=True)

    for repo in repos:
        issues_count += repo.open_issues

        if repo.watchers > watchers_max['watchers']:
            watchers_max['name'] = repo.name
            watchers_max['watchers'] = repo.watchers

        # Would technically be more efficient to print the repo names
        # here. To provide the output in the correct order, need to do it
        # separately. It's a small list, though, and the performance difference
        # is negligible, especially compared to the time to retrieve the
        # repos from the GitHub API.

    # Note that the GitHub API considers pull requests to be issues even
    # though the UI shows them separately
    print("#1: Open issues across all public repositories:", issues_count)
    print("----------------")

    print("#2: List of all repositories sorted in descending order")
    for repo in repos:
        print(repo.name)
    print("----------------")

    print("#3: Repo with most watchers:", watchers_max['name'])
    print("    It has", watchers_max['watchers'], "watchers.")


if __name__ == '__main__':
    main()
