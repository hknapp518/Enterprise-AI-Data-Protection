# Enterprise AI Data Protection Platform

## The Problem

Organizations are rapidly adopting AI assistants and Retrieval-Augmented Generation (RAG) applications to improve productivity. However, these systems introduce a significant security challenge: AI can inadvertently retrieve or expose sensitive business data if proper access controls and data protection policies are not enforced.

Traditional AI applications often lack awareness of document sensitivity, user permissions, and organizational data protection requirements. This creates a risk of exposing confidential information such as protected health information (PHI), financial records, intellectual property, and internal business documents.

This project demonstrates how Microsoft Purview and Microsoft Entra ID can be integrated with a RAG application to ensure enterprise AI only retrieves and returns data that users are authorized to access while enforcing Data Loss Prevention (DLP), sensitivity labels, and comprehensive audit logging.

## The Solution

This project simulates a clinical research organization that uses Microsoft Purview, Microsoft Entra ID, and a Retrieval-Augmented Generation (RAG) application to protect sensitive organizational data.

The platform enforces role-based access control, applies Microsoft Purview sensitivity labels, evaluates prompts and responses against DLP policies, and records every interaction for security auditing and compliance investigations.

## Architecture

<img width="1536" height="1024" alt="ChatGPT Image Jul 29, 2026, 04_04_25 PM" src="https://github.com/user-attachments/assets/a4d56e4f-4557-4bc2-a372-fdc7f1aa1021" />

## Environment

This project was built within a Microsoft 365 developer tenant to simulate a secure enterprise environment for a fictional clinical research organization. The environment combines IAM, data governance, AI powered document retrieval, and security monitoring to demonstrate how sensitive organizational data can be protected throughout the AI lifecycle.

The environment uses Microsoft Entra ID for identity and RBAC, Microsoft Purview for data classification and Data Loss Prevention (DLP), Azure AI Search and Azure OpenAI for Retrieval-Augmented Generation (RAG), and Microsoft Sentinel with Log Analytics for centralized auditing and security monitoring.

## Technologies

| Category | Technologies |
|----------|--------------|
| Identity & Access | Microsoft Entra ID |
| Data Protection | Microsoft Purview, Microsoft Purview Information Protection, Data Loss Prevention (DLP), Sensitivity Labels |
| AI & Search | Azure OpenAI, Azure AI Search, Retrieval-Augmented Generation (RAG) |
| Security Monitoring | Microsoft Sentinel, Azure Log Analytics, Kusto Query Language (KQL) |
| Automation | Azure Logic Apps |
| Development | Python, Visual Studio Code, Git, GitHub |

## Key Features

- Microsoft Entra ID authentication and RBAC
- Microsoft Purview sensitivity labels and DLP policies
- Secure Retrieval-Augmented Generation (RAG)
- AI response filtering (Allow, Redact, or Block)
- Centralized audit logging with Microsoft Sentinel and Log Analytics
- KQL telemetry for security investigations

  ## Repo Structure

```
Architecture/        High-level architecture and design diagrams
Application/         Python RAG application
Documents/           Sample enterprise documents
Policies/            DLP and sensitivity label configurations
Purview/             Microsoft Purview implementation and documentation
Logs/                Sample audit logs
Dashboard/           Reporting and monitoring
Screenshots/         Project screenshots
```
 ## Future Enhancements

 - Automated Incident Response – Integrate Microsoft Sentinel and Azure Logic Apps to automatically generate incidents, notify security teams, and initiate response workflows when high-severity DLP policy violations occur.
