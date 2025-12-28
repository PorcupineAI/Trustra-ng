CREATE TABLE IF NOT EXISTS fraud_signals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID,
    signal_type TEXT NOT NULL,
    severity INTEGER CHECK (severity BETWEEN 1 AND 10),
    resolved BOOLEAN DEFAULT FALSE,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_fraud_user ON fraud_signals(user_id);
CREATE INDEX IF NOT EXISTS idx_fraud_severity ON fraud_signals(severity);
