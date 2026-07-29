
# Microsoft Purview Auto-Labeling Policy

## Objective
The goal of this project was to automatically identify and classify sensitive organizational data using Microsoft Purview auto-labeling policies.

This implementation helps reduce human error by automatically applying sensitivity labels when sensitive information is detected across Microsoft 365 services.

---

# Technologies Used
- Microsoft Purview
- Microsoft 365 Compliance Portal
- Sensitivity Labels
- Data Loss Prevention (DLP)
- Exchange Online
- SharePoint Online
- OneDrive

---

# Auto-Labeling Configuration

An auto-labeling policy was created to detect sensitive information and automatically apply classification labels to organizational data.

The policy was configured in simulation mode first to safely evaluate detection accuracy before moving into production enforcement.

## Locations Protected
- Exchange Online
- SharePoint Online
- OneDrive

## Labels Applied
- Confidential – PHI Data
- Confidential – Financial Data
- Highly Confidential – PCI Data

---

# Sensitive Information Detection

The policy was configured to identify sensitive financial and regulated data types including:

- Credit Card Numbers
- SWIFT Codes
- International Banking Account Numbers (IBAN)
- U.S. Bank Account Numbers

Confidence levels were adjusted to help reduce false positives while improving detection accuracy.

---

# Security Value

This implementation demonstrates how organizations can:
- Reduce accidental data exposure
- Improve regulatory compliance
- Automate data governance
- Protect sensitive financial and healthcare information
- Reduce reliance on manual user classification

---

# Compliance Alignment

This project aligns with security and compliance frameworks including:

- NIST SP 800-171
- CMMC Level 2
- HIPAA
- PCI-DSS

<img width="1220" height="593" alt="Purview Auto labeling policy" src="https://github.com/user-attachments/assets/5628aa20-73bc-4deb-b586-8a249f72d3b9" />


