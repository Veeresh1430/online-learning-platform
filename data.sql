CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  password VARCHAR(100),  -- Hash this in practice
  role VARCHAR(50) -- 'student' or 'instructor'
);

CREATE TABLE courses (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100),
  description TEXT,
  instructor_id INTEGER REFERENCES users(id),
  video_url TEXT
);

CREATE TABLE enrollments (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  course_id INTEGER REFERENCES courses(id),
  progress FLOAT DEFAULT 0
);
