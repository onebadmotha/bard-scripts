import io
import json

from googleapiclient.discovery import build
import google.oauth2.service_account as service_account

# Set the path to the service account credentials file
service_account_credentials_file = "credentials.json"

# Load the service account credentials file
with open(service_account_credentials_file, "r") as f:
    service_account_credentials = json.load(f)

# Create a Google Analytics service account credential object
credentials = service_account.Credentials.from_service_account_info(
    service_account_credentials
)

# Build the Google Analytics service object
service = build("analytics", "v4", credentials=credentials)

# Set the start and end dates for the report
start_date = "2023-06-01"
end_date = "2023-11-30"

# Set the dimensions and metrics for the report
dimensions = ["source", "medium", "month"]
metrics = ["sessions"]

# Set the filter for the report
filters = "(month >= '2023-11-01' AND month <= '2023-11-30') AND ((source == 'google.com') OR (medium == 'image'))"

# Make the request to the Google Analytics API
response = service.data().ga().get(
    ids="ga:YOUR_GA_ID",
    start_date=start_date,
    end_date=end_date,
    dimensions=dimensions,
    metrics=metrics,
    filters=filters,
).execute()

# Get the results from the response
results = response["rows"]

# Print the results
for row in results:
    print(row)
