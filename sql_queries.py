# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
#try.cur_execute("DROP TABLE songplays")
#except psycopg2.Error as e: 
#    print("Error: Issue droping table songplays")
#    print (e)

user_table_drop  = "DROP TABLE IF EXISTS users"
#try.cur_execute("DROP TABLE users")
#except psycopg2.Error as e: 
#    print("Error: Issue droping table users")
#    print (e)
song_table_drop  = "DROP TABLE IF EXISTS songs"
#try.cur_execute("DROP TABLE songs")
#except psycopg2.Error as e: 
#    print("Error: Issue droping table songs")
#    print (e)
artist_table_drop= "DROP TABLE IF EXISTS artists"
#try.cur_execute("DROP TABLE artists")
#except psycopg2.Error as e: 
#    print("Error: Issue droping table artists")
#    print (e)
time_table_drop  = "DROP TABLE IF EXISTS time"
#try: cur.execute("DROP TABLE time")
#except psycopg2.Error as e: 
#    print("Error: Issue droping time")
#    print (e)

# CREATE TABLES

songplay_table_create = "create table if not exists songplays (songplay_id serial not null primary key, start_time bigint, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id int, location text, user_agent text)"
#try: cur.execute("CREATE TABLE IF NOT EXISTS songplays (songplay_id int, start_time bigint, user_id int, level int, song_id int, artist_id int, session_id int, location text, user_agent text);")

#except psycopg2.Error as e: 
#   print("Error: Issue creating table songplays")
#  print (e)
    
user_table_create = "create table if not exists users(user_id varchar not null primary key, first_name text, last_name text, gender text, level varchar)"

#try: cur.execute("CREATE TABLE IF NOT EXISTS users (user_id int, #first_name text, last_name text, gender text, level int);")

#except psycopg2.Error as e: 
#    print("Error: Issue creating table users")
#    print (e)

song_table_create = "create table if not exists songs (song_id varchar not null primary key, title text, artist_id varchar, year int, duration numeric)"

#try: cur.execute("CREATE TABLE IF NOT EXISTS songs (song_id int, #title text, artist_id int, year date, duration numeric);")

#except psycopg2.Error as e: 
#    print("Error: Issue creating table songs")
#    print (e)
artist_table_create = "create table if not exists artists(artist_id varchar not null primary key, name text, location text, latitude numeric, longitude numeric)"
#try: cur.execute("CREATE TABLE IF NOT EXISTS songs (song_id int, #title text, artist_id int, year date, duration numeric);")

#except psycopg2.Error as e: 
#    print("Error: Issue creating table songs")
#    print (e)

time_table_create = "create table if not exists time(start_time timestamp not null primary key, hour numeric, day numeric, week numeric, month numeric, year int, weekday numeric)"
#try: cur.execute("CREATE TABLE IF NOT EXISTS time (start_time #numeric, hour numeric, day numeric, week numeric, month numeric, #year numeric, weekday numeric);")
#except psycopg2.Error as e: 
#    print("Error: Issue creating table time")
#    print (e)

# INSERT RECORDS

songplay_table_insert =("""insert into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values (%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (songplay_id) DO NOTHING;""")

user_table_insert = ("""insert into users(user_id, first_name, last_name, gender, level) \
values (%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO NOTHING;""")

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

#song_select = ("""select a.song_id,a.title, c.artist_id, c.name, d.user_id, #d.first_name,d.last_name, e.location, e.songplay_id from  songs a, artists c, #users d,songplays e
#""")

song_select = ("""select a.song_id, b.artist_id 
from  songs a, artists b where a.artist_id = b.artist_id
and a.title = %s AND b.name = %s and  a.duration = %s
;""")
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]