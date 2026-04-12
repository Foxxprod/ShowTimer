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

INSERT OR IGNORE INTO config (parameter, value) VALUES
    ('prompter_text_size',       '69'),
    ('prompter_text_color',      '#ff5500'),
    ('next_cue_text_size',       '50'),
    ('next_cue_text_color',      '#ffffff'),
    ('next_cue_outline_width',   '2'),
    ('second_cue_text_size',     '28'),
    ('second_cue_text_color',    '#aaaaaa'),
    ('second_cue_outline_width', '2'),
    ('clock_text_size',          '28'),
    ('clock_text_color',         '#ffffff'),
    ('clock_outline_width',      '2'),
    ('blink_first_time',         '25000'),
    ('blink_first_color',        '#00cc00'),
    ('blink_second_time',        '10000'),
    ('blink_second_color',       '#ff8800'),
    ('blink_third_time',         '5000'),
    ('blink_third_color',        '#ff0000'),
    ('osc_ip',                   '127.0.0.1'),
    ('osc_port',                 '9000'),
    ('osc_active',               'True'),
    ('active_show',              '5');

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