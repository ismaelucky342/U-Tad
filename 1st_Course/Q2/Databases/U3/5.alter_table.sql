ALTER TABLE Students
    ADD COLUMN address VARCHAR(255),
    ADD COLUMN registration_date DATETIME DEFAULT CURRENT_TIMESTAMP;

CREATE INDEX idx_last_name ON Students(last_name);
