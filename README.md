# Listing-Unused-Projects

## How to list all Dataiku Projects which is not commited in last 365 days in Dataiku?

To list all Dataiku projects that have not been committed in the last year, you can follow these steps. This process involves using the Dataiku API and scripting to query project data.

#### Prerequisites:
##### 1 -- Dataiku API Access: Make sure you have the necessary access to use the Dataiku API.
##### 2 -- Python: You will be using Python to interact with the Dataiku API.
##### 3 -- Admin Permissions: You should have appropriate permissions to access project information.

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

### **Conclusion**:
By automating the process of identifying inactive projects, this Python script provides significant benefits in resource management, operational efficiency, compliance, and cost control. Organizations can use it to ensure that their Dataiku projects are being managed effectively, with unnecessary projects being archived or reassigned, thus keeping the system clean and efficient for active use cases.
