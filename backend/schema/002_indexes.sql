-- USERS
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_trust_score ON users(trust_score);

-- ESCROW
CREATE INDEX IF NOT EXISTS idx_escrow_buyer_id ON escrow(buyer_id);
CREATE INDEX IF NOT EXISTS idx_escrow_seller_id ON escrow(seller_id);
CREATE INDEX IF NOT EXISTS idx_escrow_status ON escrow(status);

-- REVENUE
CREATE INDEX IF NOT EXISTS idx_revenue_type ON revenue(type);
CREATE INDEX IF NOT EXISTS idx_revenue_created_at ON revenue(created_at);
