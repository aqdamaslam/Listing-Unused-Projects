# Listing-Unused-Projects

### **Use Case: Monitoring and Archiving Inactive Dataiku Projects**

**Background**:
In large organizations, Dataiku is often used for data science and machine learning projects. Over time, some projects may become inactive or are no longer updated. Identifying such projects is crucial for managing resources efficiently, archiving obsolete projects, or taking action to re-engage project owners.

**Problem**:
Many organizations using Dataiku may have hundreds or thousands of projects, making it difficult to track which projects are still active or being regularly worked on. Manually tracking project activity is not efficient, especially as time goes by and projects pile up.

**Solution**:
Automating the process of identifying Dataiku projects that haven't had any commits in the past year can save time and improve operational efficiency. By using the Python script described earlier, the system can automatically identify and list inactive projects, allowing teams to take necessary actions (e.g., archiving, cleaning up resources, or reassigning them).

---

### **Benefits of the Automation Python Script**

1. **Improved Resource Management**: 
   - **Archiving Unused Projects**: Projects that are not being actively worked on can be archived to save storage and reduce clutter. This makes it easier to focus on active projects.
   - **Optimizing System Resources**: Identifying inactive projects allows you to shut down or reallocate compute resources that were assigned to these projects, which can lead to cost savings on infrastructure.
   
2. **Increased Operational Efficiency**:
   - **Time-saving**: The script automates the process of checking commit history, saving valuable time compared to manual tracking.
   - **Reduced Manual Oversight**: Data teams no longer need to manually check each project’s activity. The script provides an automated solution, reducing human error and ensuring that projects are accurately monitored.

3. **Enhanced Collaboration and Project Ownership**:
   - **Re-engagement Opportunity**: If projects haven't been committed in a year, it may signal a need for renewed collaboration or reassignment. This script can help project owners realize if their projects are inactive and provide a prompt for re-engagement.
   - **Better Project Tracking**: Teams can track which projects are active and which are stagnant, helping management understand the health of their data science or machine learning initiatives.

4. **Compliance and Audit**:
   - **Tracking Project Activity for Compliance**: For industries where project audits are required, having a system to track project activity is essential. This script can help maintain an accurate record of when each project was last updated, supporting compliance with internal and external regulations.
   
5. **Dataiku Governance**:
   - **Centralized Project Oversight**: The script ensures that project activity is continuously monitored across your entire Dataiku instance, allowing for better oversight of all data science projects.
   - **Reducing Project Debt**: Inactive projects that are no longer useful can contribute to "technical debt." Identifying and archiving them helps in maintaining the cleanliness and relevance of the project repository.

6. **Cost Control**:
   - **Minimizing Unnecessary Costs**: If Dataiku projects are consuming cloud resources or compute clusters, inactive projects should be flagged and removed or archived. This helps in minimizing the consumption of unnecessary resources, leading to cost savings in terms of server or cloud usage.

7. **Support for Scalability**:
   - **Scalable Monitoring**: As organizations scale their data science efforts, the number of Dataiku projects can increase exponentially. This script scales well, making it easier to monitor large datasets and multiple projects without manual oversight.
   - **Future-proofing**: As the organization grows, this script will continue to function efficiently even with thousands of projects, ensuring that no project becomes "lost" in the system.

---

#### **1. Introduction**
This Python script connects to a Dataiku instance via its REST API to fetch a list of projects that have not been committed to in the last 365 days (1 year). The script uses the Git commit history of each project to check when the last commit occurred.

#### **2. Requirements**
- **Dataiku API Client**: You need the `dataiku-api-client` package to interact with the Dataiku API.
    - Install it using `pip install dataiku-api-client`.
- **Dataiku API Key**: You need an API key for authentication. This can be generated in the user settings under **API Keys** in Dataiku.
- **Python Environment**: The script requires Python 3.x.

#### **3. Steps and Flow**

##### **Step 1: Authenticate with Dataiku API**
The script begins by authenticating to your Dataiku instance using the provided `dataiku_url` (URL of the Dataiku instance) and `api_key` (your API key). The `api_client.DataikuAPIClient` is used to create the connection.

##### **Step 2: Fetch All Projects**
The `list_projects()` method is called on the `client` object to fetch all the available projects in the Dataiku instance.

##### **Step 3: Define the One Year Threshold**
We calculate the threshold date for one year ago by subtracting 365 days from the current date.

##### **Step 4: Loop Through Each Project**
The script loops through each project and retrieves its commit history by calling the `get_git_commit_log()` method.

##### **Step 5: Check Last Commit Date**
For each project, the script checks the date of the most recent commit:
- If there are commits available, it checks if the last commit date is older than one year.
- If the last commit date is older than the defined threshold (365 days), the project is added to the list of uncommitted projects.

##### **Step 6: Output the Results**
Finally, the script outputs a list of projects that have not been committed to in the last year. For each project, the project key and last commit date are printed.

#### **4. Output Format**
The script prints the following details for each uncommitted project:
- **Project Key**: Unique identifier for the Dataiku project.
- **Last Commit Date**: The date when the last commit was made to the project.

#### **5. Error Handling**
The script includes basic error handling to manage issues like API connection failures or missing data. If any errors occur during execution, an error message is printed, and an empty list is returned.

#### **6. Customization**
- **Dataiku URL**: Replace `"http://your-dataiku-instance-url"` with the actual URL of your Dataiku instance.
- **API Key**: Replace `"your-api-key"` with your actual Dataiku API key.

You can further customize the script to output results to a file (e.g., CSV or JSON), or integrate it into a larger automated process for monitoring Dataiku project activities.

#### **7. Future Enhancements**
- You could add additional filtering based on project status (e.g., only active projects).
- Extend the script to send an email or a Slack notification for projects not updated in the past year.

This should give you a fully functional and well-documented script to list uncommitted projects in Dataiku. Let me know if you'd like any further adjustments! 
