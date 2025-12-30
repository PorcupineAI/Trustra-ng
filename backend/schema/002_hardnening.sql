ALTER TABLE users
ADD CONSTRAINT unique_phone UNIQUE (phone);

ALTER TABLE escrow
ADD CONSTRAINT positive_amount CHECK (amount > 0);

ALTER TABLE revenue
ADD CONSTRAINT positive_revenue CHECK (amount > 0);

