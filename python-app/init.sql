-- Create quotes table
CREATE TABLE IF NOT EXISTS quotes (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO quotes (text) VALUES ('Hello') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('The quick brown fox jumps over the lazy dog.') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('To be or not to be, that is the question.') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('All that glitters is not gold.') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('Practice makes perfect.') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('Knowledge is power.') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('Time flies when you''re having fun.') ON CONFLICT DO NOTHING;
INSERT INTO quotes (text) VALUES ('Actions speak louder than words.') ON CONFLICT DO NOTHING;