#sql_queries.py consists of 5 "DROP TABLE ..." statements as well 
#as 5 "CREATE TABLE ..." with their columns #and correct datypes, 
#constraints and other conditions.

# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop  = "DROP TABLE IF EXISTS users"
song_table_drop  = "DROP TABLE IF EXISTS songs"
artist_table_drop= "DROP TABLE IF EXISTS artists"
time_table_drop  = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = "create table if not exists songplays (songplay_id serial not null primary key, start_time bigint not null, user_id integer not null, level varchar, song_id varchar, artist_id varchar, session_id int,location text, user_agent text)"
    
user_table_create = "create table if not exists users(user_id integer not null primary key, first_name text, last_name text, gender text, level varchar)"

song_table_create = "create table if not exists songs(song_id varchar not null primary key, title text not null, artist_id varchar, year int, duration numeric not null)"

artist_table_create = "create table if not exists artists(artist_id varchar not null primary key, name text not null, location text, latitude double precision, longitude double precision)"

time_table_create = "create table if not exists time(start_time timestamp not null primary key, hour numeric, day numeric, week numeric, month numeric, year int, weekday numeric)"

# INSERT RECORDS
songplay_table_insert =("""insert into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values (%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (songplay_id) DO NOTHING;""")

user_table_insert = ("""insert into users(user_id, first_name, last_name, gender, level) \
values (%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;""")

song_table_insert = ("""insert into songs (song_id, title, artist_id, year, duration)
values (%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;""")

artist_table_insert = ("""insert into artists (artist_id, name, location, latitude, longitude)
values (%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING;""")

time_table_insert = ("""insert into time (start_time, hour, day, week, month, year, weekday)
values (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING;""")

# FIND SONGS
song_select = ("""select a.song_id, b.artist_id 
from  songs a, artists b where a.artist_id = b.artist_id
and a.title = %s AND b.name = %s and  a.duration = %s
;""")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
