from github import Github

class FileData:
    def __init__(self,
                commit, 
                author,
                datetime):
        self.commit = commit
        self.author = author
        self.datetime = datetime
    
    def __str__(self):
        return 'Commit {} from user: {} on date: {}'\
            .format(self.commit, self.author, self.datetime)

class FileChanges:
    def __init__(self):
        self.fileChanges = {}
    
    def add_change(self, filename, filedata):
        self.fileChanges[filename] = filedata
    
    def __str__(self):
        str = ''
        for filechanges in self.fileChanges:
            str += 'filename is : {} and file data is: {}'.format(filechanges, self.fileChanges[filechanges])
        return str
    


class PRData:
    def __init__(self,
                number,
                user,
                comments,
                list_of_changed_files,
                list_of_contributors = 0):
        self.number = number
        self.user = user
        self.comments = comments
        self.list_of_changed_files = list_of_changed_files
        #self.list_of_contributors = list_of_contributors
    
    def __str__(self):
        return 'The PR number is {} from user: {}'\
            .format(self.number, self.user)

class GitHubData:
    def __init__(self, repo):
        #self.github = Github("015ca5700387a73a1696b9d46fb17cfac6c7e5d6")
        #self.repo = self.github.get_repo(repo)
        #self.prData = []
        #self.biggest_contributor_with_prs = None
        self.files = {}
    
    def calculate_biggest_contributor_with_prs(self):
        pulls = self.repo.get_pulls()
        prs = {}
        for pull in pulls:
            try:
                prs[pull.user] = prs[pull.user] + 1
            except:
                prs[pull.user] = 1
        return prs
    
    def create_contributors(self):
        return ''
        #commits = self.repo.get_commits()
        #for commit in commits:
            #fileData = FileData(commit.commit, commit.author)
            #for file in commit.files:
            #    if(self.files.get(file.filename) == None):
            #        self.files[file.filename] = [fileData]
            #    else:
            #        self.files[file.filename] = \
            #            self.files[file.filename].append(fileData)
    
    def print_contributors(self):
        for k in self.files:
            print('file is {}'.format(k))
            print('contet is {}'.format(self.files[k]))
            #for elem in self.files[k]:
            #    print('file data is {}'.format(elem))
    
    def print_users_with_comments(self, pr):
        unique_users = []
        for issue in pr.get_issue_comments(base='master'):
            unique_users.append(issue.user.login)
    
        for name in set(unique_users):
            print(name)

    def print_open_pull_requests(self):
        pulls = self.repo.get_pulls(state='open', sort='created', base='master')
        for pr in pulls:
            somePr = PRData(pr.number, pr.user, pr.comments, pr.get_files())
            self.prData.append(somePr)
        
        for data in self.prData:
            print(data)


github = GitHubData("multiformats/py-multicodec")
#github.print_open_pull_requests()
#prs = github.calculate_biggest_contributor_with_prs()
#for pr in prs:
#    print(pr)
#print(max(prs.items(), key=lambda x: x[1]))
github.create_contributors()
github.print_contributors()


def test_answer():
    assert True

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
