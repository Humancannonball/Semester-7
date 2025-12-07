# Thesis Proposal: AI-Powered Scam Detection System

**Topic:** Design and Implementation of a Real-Time AI-Based Scam Detection System for User-Generated Content

**Student:** Mark Mikula

---

### 1. Problem Statement
The proliferation of scam content and phishing attempts on user-generated content platforms (e.g., YouTube) poses a significant security risk to users. Traditional regex-based filters are easily bypassed by evolving social engineering tactics, while manual moderation cannot keep pace with the volume of comments. Large Language Models (LLMs) offer high detection accuracy but introduce challenges regarding latency, cost, and integration into real-time browsing experiences. There is a need for a system that balances high-accuracy AI detection with the performance requirements of a browser-based tool.

### 2. Primary Research Questions
1.  **Detection Efficacy vs. Latency:** What is the trade-off between detection accuracy (F1-score) and system latency when using lightweight LLMs (e.g., GPT-4o-mini) versus heuristic methods for real-time content scanning?
2.  **False Positive Mitigation:** How can a hybrid detection approach (combining allow-lists, heuristics, and AI) minimize false positives to ensure legitimate user communication is not disrupted?
3.  **System Scalability:** How does a cloud-native architecture handle burst traffic from high-volume comment sections while maintaining cost-efficiency?

### 3. Methodology & Technologies
*   **Development:**
    *   **Frontend:** Cross-browser extension (Manifest V3) using JavaScript/TypeScript for real-time DOM observation and user interaction.
    *   **Backend:** Node.js/Express API for centralized detection logic and rate limiting.
    *   **AI/ML:** Integration with OpenAI API for semantic analysis of potential scam content.
*   **Infrastructure & Deployment:**
    *   **Infrastructure as Code:** Provisioning scalable cloud resources (AWS EC2/RDS) using **Terraform**.
    *   **Data Persistence:** PostgreSQL for storing detection events, user feedback, and whitelist/blacklist configurations.
    *   **CI/CD:** Automated testing and deployment pipelines to ensure system reliability.

### 4. Expected Contributions and Outcomes
1.  **Software Artifact:** A fully functional, open-source browser extension and backend API capable of detecting scam comments on YouTube in real-time.
2.  **Performance Analysis:** A quantitative report comparing the latency and accuracy of the AI-based approach against standard keyword blocking.
3.  **Hybrid Detection Algorithm:** A documented algorithm that optimizes the cost/accuracy ratio by filtering obvious cases before invoking the AI model.
4.  **Thesis Report:** A formal academic paper presenting the system architecture, implementation details, and evaluation results.

---

### Why this is a strong thesis topic:
*   **Relevance:** It addresses a current, widespread cybersecurity problem (Social Engineering).
*   **Complexity:** It involves full-stack development, cloud infrastructure, and AI integration.
*   **Measurable Results:** You can easily measure success through accuracy rates, latency metrics, and user feedback.
