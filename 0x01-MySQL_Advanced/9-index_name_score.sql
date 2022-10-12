-- this is task 9
-- creates index idx_name_first on table names and first letter of name and score

CREATE INDEX idx_name_first_score ON names(name(1), score);
