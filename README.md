# FNOL Claims Processing Agent

## Problem Statement
The goal of this project is to build a lightweight autonomous agent that processes
FNOL (First Notice of Loss) documents. The agent extracts key claim information,
identifies missing or suspicious data, classifies claims, and routes them to the
appropriate workflow with a clear explanation.

---

## Solution Overview
This project implements a Python-based FNOL claims processing agent that:
- Reads FNOL documents in PDF format
- Extracts structured claim fields
- Validates mandatory information
- Applies business routing rules
- Produces a structured JSON output with reasoning

The solution simulates real-world insurance claim automation workflows.

---

## Features
- PDF FNOL document parsing
- Key field extraction (policy, incident, asset, claim details)
- Mandatory field validation
- Fraud / investigation keyword detection
- Claim routing logic
- JSON-based structured output

---

## Extracted Fields
- Policy Number
- Policyholder Name
- Incident Date
- Location
- Description
- Estimated Damage
- Claim Type

---

## Routing Rules
The agent routes claims based on the following rules:

1. **Manual Review**
   - If any mandatory field is missing

2. **Investigation Flag**
   - If the description contains keywords such as:
     - fraud
     - staged
     - inconsistent

3. **Fast-track**
   - If estimated damage is below ₹25,000
   - And no fraud indicators are present

4. **Manual Review (Default)**
   - For high-value or unclear claims

---

## Project Structure
