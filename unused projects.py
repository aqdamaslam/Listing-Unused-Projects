import dataiku
import git
from dataikuapi.dss.project import DSSProjec
from dataiku import api_client
from datetime import datetime, timedelta

# Get the list of all projects
client = dataiku.api.client()
projects = client.list_projects()
print(projects)

project_commit_dates = []
for project in projects:
  project_key = project['projectKey']
  project_name = project['name']
  projecct_owner = project['ownerLogin']
  try:
    # Get the projecct object
    project_obj = client.get_project(project_key)
    print(project_obj)
    project_name = project_name
    print(project_name)
    project_owner = project_owner
    print(project_owner)

    # Get the git last commit
    projectGit = project_obj.get_project_git()
    last_commit = projectGit.log(count=-1)['entries'][0]['timestamp']
    last = str(last_commit)
    print(last_commit)

    # Set the threshold date to 365 Days
    threshold_date = datetime.now() - timedelta(days=365)
    date = str(threshold_date)
    print(date)

    if last < date:
      project_commit_dates.append({
        'projectKey': project_key,
        'projectName': project_name,
        'projectOwner': project_owner,
        'lastCommitDate': last_commit
      })

  exception Exception as e:
      print(f"Error Processing project {project_key}: {e}")

# Display the list of unused projects

for project in project_commit_dates:
  print(f"Project Key: {project[projectKey]}, Project Name: {project[projectName]}, Project Owner: {project[projectOwner]}, Last Commit Date: {project[lastCommitDate]}")
