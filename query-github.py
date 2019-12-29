from github import Github

class PRData:
    def __init__(self, 
                 user, 
                 list_of_changed_files,
                 list_of_contributors):
        self.user = user
        self.list_of_changed_files = list_of_changed_files
        self.list_of_contributors = list_of_contributors

class GitHubData:
    def __init__(self, repo):
        self.github = Github("015ca5700387a73a1696b9d46fb17cfac6c7e5d6")
        self.repo = self.github.get_repo(repo)
    
    def print_users_with_comments(self, pr):
        unique_users = []
        for issue in pr.get_issue_comments():
            unique_users.append(issue.user.login)
    
        for name in set(unique_users):
            print(name)

    def print_open_pull_requests(self):
        pulls = self.repo.get_pulls(state='open', sort='created', base='master')
        for pr in pulls:
            print(pr.number)
            print("----")
            print("This PR is from: {}".format(pr.user))
            print("This PR has: {}".format(pr.comments))
            print("This PR number of changed files is: ", pr.get_files().totalCount)
            self.print_users_with_comments(pr)
            print("*******")

#    def __str__()
#        "The PR number is {0}, the number of comments is: "

# using username and password
#g = Github("015ca5700387a73a1696b9d46fb17cfac6c7e5d6")



# Then play with your Github objects:
#for repo in g.get_user().get_repos():
#    print(repo.name)

#repositories = g.search_repositories(query='language:python')
#for repo in repositories:
#    print(repo)

#def print_changed_files(pr):
#    for file in pr.get_files():
#        print(file.filename)

#def print_issue_comments(pr):
#    for issue in pr.get_issue_comments():
#        print(issue.body)

#def print_users_with_comments(pr):
#    unique_users = []
#    for issue in pr.get_issue_comments():
#        unique_users.append(issue.user.login)
    
#    for name in set(unique_users):
#        print(name)

#repo = g.get_repo("tensorflow/tensorflow")

github = GitHubData("tensorflow/tensorflow")
github.print_open_pull_requests()

#
#get_commits(sha=NotSet, path=NotSet, since=NotSet, until=NotSet, author=NotSet)
#GET /repos/:owner/:repo/commits

#Parameters:	
#sha – string
#path – string
#since – datetime.datetime
#until – datetime.datetime
#author – string or github.NamedUser.NamedUser or github.AuthenticatedUser.AuthenticatedUser
#Return type:	
#github.PaginatedList.PaginatedList of github.Commit.Commit
#


#for commits in repo.get_commits():
#    for f in commits.files:
#        if f.filename == '.bazelversion':
#            print(commits.author.login)

#pulls = repo.get_pulls(state='open', sort='created', base='master')
#for pr in pulls:
#    print(pr.number)
#    print("----")
#    print("This PR is from: ", pr.user)
#    print("This PR has: ", pr.comments)
#    print("This PR number of changed files is: ", pr.get_files().totalCount)
#    print_users_with_comments(pr)
#    print("*******")
    
    
# function that looks at scope of one change and evaluates who touched those files

# features
# - changed files
# - list of contributors for each file
# - number of changed files
# - author
# - 
