# Enterprise AI Data Protection Platform

> **A security platform that enables organizations to safely adopt enterprise AI by enforcing Microsoft Entra ID identity controls, Microsoft Purview data governance, and policy-driven access decisions before AI responses are returned.**

<p align="center">
  <img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/bd032d1d-17c0-4b6f-aa89-243627341637" />
</p>


# Business Problem

Organizations are rapidly adopting enterprise AI solutions such as Microsoft 365 Copilot, ChatGPT Enterprise, and custom Retrieval-Augmented Generation (RAG) applications to improve productivity.

While these platforms provide significant business value, they also introduce a critical security challenge.

> **How do organizations allow employees to use AI without exposing sensitive corporate information to unauthorized users?**

Traditional access controls and document permissions alone are not enough. AI applications require an additional security layer capable of evaluating user identity, document sensitivity, organizational policies, and regulatory requirements before generating a response.

Without these controls, organizations risk:

- Unauthorized disclosure of sensitive information
- Leakage of PHI, PCI, and confidential business data
- Insider threats and privilege misuse
- Lack of audit visibility into AI interactions
- Regulatory compliance violations (HIPAA, PCI DSS, SOX, GDPR)

---

# Solution

The Enterprise AI Data Protection Platform acts as a security layer between employees and enterprise AI.

Every AI request is evaluated before a response is returned.

The platform:

- Authenticates users with Microsoft Entra ID
- Validates Role-Based Access Control (RBAC)
- Evaluates Microsoft Purview sensitivity labels
- Applies DLP policy enforcement
- Retrieves only authorized enterprise knowledge
- Allows, redacts, or blocks responses
- Records every interaction for auditing
- Sends security events to Splunk Enterprise
- Enables SOC investigation and automated response workflows

---

# Solution Architecture

The platform is designed around a **policy-driven security engine** that evaluates every AI interaction before a response is generated.

**Core workflow:**

```
User
    │
    ▼
Microsoft Entra ID
(Authentication & RBAC)
    │
    ▼
Enterprise AI Application
(Python + RAG)
    │
    ▼
Azure AI Search
(Knowledge Base)
    │
    ▼
Enterprise AI Security Policy Engine
────────────────────────────────────
✔ Identity Validation
✔ RBAC Evaluation
✔ Microsoft Purview Labels
✔ DLP Policy Evaluation
✔ Prompt Inspection
✔ Risk Scoring
────────────────────────────────────
          │
 ┌────────┼─────────┐
 │        │         │
 ▼        ▼         ▼
Allow   Redact    Block
          │
          ▼
AI Response
```

Every decision (Allow, Redact, or Block) is logged and forwarded to Splunk Enterprise for monitoring, correlation, and incident response.

---

# Example Scenario

### User Request

> "Show me every employee's salary and Social Security Number."

### Security Evaluation

1. User identity is verified through Microsoft Entra ID.
2. Azure AI Search retrieves relevant enterprise documents.
3. The Enterprise AI Security Policy Engine evaluates:
   - RBAC permissions
   - Microsoft Purview sensitivity labels
   - DLP policy requirements
   - Prompt risk indicators
4. The request is **blocked** because the user is not authorized.
5. The event is logged and forwarded to Splunk Enterprise.
6. Correlation rules determine whether additional investigation or automated response is required.

---

# Key Features

## Identity & Access

- Microsoft Entra ID Authentication
- Multi-Factor Authentication (MFA)
- Role-Based Access Control (RBAC)
- Group Membership Validation
- Least Privilege Enforcement

## AI Security

- Prompt Inspection
- Secure Document Retrieval
- Context-Aware Authorization
- AI Response Governance
- Allow / Redact / Block Decision Engine

## Data Protection

- Microsoft Purview
- Sensitivity Labels
- Data Classification
- DLP Policy Enforcement
- Protected Enterprise Knowledge Base

## Security Operations

- Centralized Audit Logging
- Splunk Enterprise Integration
- Correlation Searches
- Risk Scoring
- SOAR Automation
- Security Investigations

---

# Business Value

This project demonstrates how organizations can safely adopt enterprise AI while maintaining strong security and governance controls.

Business outcomes include:

- Reduce the risk of AI-driven data leakage
- Enforce least-privilege access to enterprise knowledge
- Improve AI governance and regulatory compliance
- Increase SOC visibility into AI interactions
- Detect unauthorized attempts to access sensitive information
- Provide complete auditability for security investigations

---

# Technology Stack

| Category | Technologies |
|-----------|--------------|
| Identity | Microsoft Entra ID |
| AI | Python, Azure AI Search, Azure OpenAI / OpenAI |
| Data Protection | Microsoft Purview, Sensitivity Labels, DLP |
| Monitoring | Splunk Enterprise |
| Automation | Azure Logic Apps |
| APIs | Microsoft Graph API |

---

# Future Enhancements

- Real-time Microsoft Graph integration
- Live Microsoft Purview label retrieval
- Splunk dashboards for AI governance
- Insider risk behavior analytics
- AI risk scoring and anomaly detection
- ServiceNow incident creation through SOAR automation

---

# Project Goal

The objective of this project is to demonstrate how enterprise organizations can securely adopt AI by combining identity, governance, data protection, and security operations into a unified architecture.

Rather than functioning as a traditional chatbot, this platform serves as a **security layer** that evaluates every AI interaction before sensitive information is returned to the user.
