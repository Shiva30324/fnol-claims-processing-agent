import json
import re
import os

# Step 1: File path
file_path = os.path.join("input", "fnol_sample.txt")

# Step 2: Check file exists
if not os.path.exists(file_path):
    print("ERROR: FNOL file not found")
    exit()

# Step 3: Read file
with open(file_path, "r") as file:
    text = file.read()

# Step 4: Field extraction function
def extract(pattern):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None

# Step 5: Extract FNOL fields
extracted_fields = {
    "policyNumber": extract(r"Policy Number:\s*(.*)"),
    "policyholderName": extract(r"Policyholder Name:\s*(.*)"),
    "incidentDate": extract(r"Date of Incident:\s*(.*)"),
    "location": extract(r"Location:\s*(.*)"),
    "description": extract(r"Description:\s*(.*)"),
    "estimatedDamage": extract(r"Estimated Damage:\s*(.*)"),
    "claimType": extract(r"Claim Type:\s*(.*)")
}

# Step 6: Mandatory field check
mandatory_fields = [
    "policyNumber",
    "policyholderName",
    "incidentDate",
    "location",
    "description",
    "claimType"
]

missing_fields = []
for field in mandatory_fields:
    if not extracted_fields.get(field):
        missing_fields.append(field)

# Step 7: Routing logic
# Convert description to lowercase for checking
description_text = (extracted_fields.get("description") or "").lower()

fraud_keywords = ["fraud", "staged", "inconsistent"]

if missing_fields:
    route = "Manual Review"
    reason = "Mandatory fields are missing"

elif any(word in description_text for word in fraud_keywords):
    route = "Investigation Flag"
    reason = "Suspicious keywords found in claim description"

elif extracted_fields["estimatedDamage"] and int(extracted_fields["estimatedDamage"]) < 25000:
    route = "Fast-track"
    reason = "Estimated damage is below ₹25,000"

else:
    route = "Manual Review"
    reason = "High value or unclear claim"


# Step 8: Final output
output = {
    "extractedFields": extracted_fields,
    "missingFields": missing_fields,
    "recommendedRoute": route,
    "reasoning": reason
}

print(json.dumps(output, indent=4))
