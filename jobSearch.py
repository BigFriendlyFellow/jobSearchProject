import json

import requests

# Replace with your actual Adzuna API credentials
app_id = "8096cc84"
app_key = "60e5cd6b55ac2038930f11e5301a4b0c"

# Construct the API URL with the provided parameters
url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"
params = {
    'app_id': app_id,
    'app_key': app_key,
    'results_per_page': 20,
    'what': 'python',
    #'what_phrase': 'python',
    'what_exclude': 'sales senior',
    'where': '63129',
    'distance': '30',
    #'sort_dir': 'up',  #doesn't seem to work
    'sort_by': 'date',
    'salary_max': '80000',
    'content-type': 'application/json'
}

# Send the GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    job_data = response.json()
    
    # Print out the job results (you can modify this part to process the data as needed)
    for job in job_data.get('results', []):
        print(f"Job Title: {job['title']}")
        try:
            print(f"Company: {job['company']['display_name']}")
        except KeyError:
            print("Company: Not Available")
        print(f"Location: {job['location']['display_name']}")
        print(f"Salary: {job['salary_min']} - {job['salary_max']}")
        print(f"URL: {job['redirect_url']}")
        print("=" * 40)
else:
    print(f"Error: Unable to retrieve data (Status code: {response.status_code})")