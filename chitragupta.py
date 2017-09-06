""" Chitragupta - The guy who tracks your contributions to the MetaKGP Github organisation!

Author : Rameshwar Bhaskaran
"""

import requests
import json

# get a list of all repositories in the MetaKGP org
r = requests.get("https://api.github.com/orgs/metakgp/repos")

if not r.ok:
    print "Looks like something is wrong"
    exit(0)
else:
    repos = json.loads(r.text)
    contributor_urls = {}
    for repo in repos:
       contributor_urls[repo['name']] = repo['contributors_url']
    contributors = {}
    for repo, url in contributor_urls.items():
        try:
            contributor_response = requests.get(url)
            contributors[repo] = set()
            repo_contributors = json.loads(contributor_response.text)
            for contributor in repo_contributors:
                contributors[repo].add(contributor['login'])
        except Exception as e:
            print "Failed due to ", str(e)
            pass

consolidated_list = set()
for repo in contributors:
    print repo, contributors[repo]
    consolidated_list = consolidated_list.union(contributors[repo])

print "Consolidated list"
print consolidated_list
