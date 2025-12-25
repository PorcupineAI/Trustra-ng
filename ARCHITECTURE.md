# Trustra-NG System Architecture

## 1. Entry Points
- WhatsApp messages
- Frontend web UI
- Admin dashboard

## 2. Core Services
- Escrow Service
- Trust Scoring Service
- Verification Service
- Dispute Resolution Service
- Notification Service

## 3. Trust Score Flow
User Action → Event Logged → Trust Engine → Score Normalized → Trust Label Generated

## 4. Data Separation
- PII isolated
- Trust metrics anonymized
- Public trust labels only

## 5. Security
- Webhook signature verification
- Role-based access control
- Immutable escrow logs

## 6. Scalability
- Stateless API
- Async workers for WhatsApp
- Database indexing for trust events
