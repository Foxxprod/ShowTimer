CREATE TABLE IF NOT EXISTS shows (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nom         TEXT    NOT NULL,
    description TEXT,
    duree       INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS config (
    parameter   TEXT    PRIMARY KEY,
    value       TEXT
);

CREATE TABLE IF NOT EXISTS cues (
    cue_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    show_id     INTEGER NOT NULL,
    nom         TEXT    NOT NULL,
    description TEXT,
    temps       INTEGER NOT NULL,
    color      TEXT,
    osc_url TEXT,
    osc_args INTEGER,

    FOREIGN KEY (show_id) REFERENCES shows(id)
);