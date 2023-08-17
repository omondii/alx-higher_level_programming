-- Creates table id_not_null, default id to 1 and not null constraint
CREATE TABLE IF NOT EXISTS id_not_null(
       id INT DEFAULT 1 NOT NULL,
       name VARCHAR(256)
);
