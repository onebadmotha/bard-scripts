import io
import json

from googleapiclient.discovery import build

# Set the Google Analytics service account credentials
credentials = service_account.Credentials.from_service_account_info(
    json.load(io.open("path/to/your/service-account-credentials.json"))
)

# Build the Google Analytics service object
service = build("analytics", "v4", credentials=credentials)

# Set the start and end dates for the report
start_date = "2023-11-01"
end_date = "2023-11-09"

# Set the dimensions and metrics for the report
dimensions = ["source", "medium"]
metrics = ["sessions"]

# Set the filter for the report
filters = "((source == 'google.com') OR (medium == 'image'))"

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