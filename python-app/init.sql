-- Create quotes table
CREATE TABLE IF NOT EXISTS quotes (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO quotes (text) VALUES ('S - Single Responsibility Principle') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('O - Open/Closed Principle') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('L - Liskov Substitution Principle') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('I - Interface Segregation Principle') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('D - Dependency Inversion Principle') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('Actions speak louder than words.') ON CONFLICT DO NOTHING;