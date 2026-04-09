--
-- PostgreSQL database cluster dump
--

\restrict jLp8x8nbUpQnZOeEnc3q9Xx55QkzJQERhfAYKsqtgh5Fpz023R2VCbQsJAPBVZp

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS;
CREATE ROLE specialuser;
ALTER ROLE specialuser WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:9Ki3NcSyYQY9oOi3xW2KQg==$KfRcB/94XIPzyyXwrNdRKX5MOcnb2bubKYv6h7qKuo0=:7GhJPl5Wm+HBq54Jtu5cYfnPBb3z3zDwdZn8WVMEcKc=';

--
-- User Configurations
--

--
-- User Config "specialuser"
--

ALTER ROLE specialuser SET client_encoding TO 'utf8';
ALTER ROLE specialuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE specialuser SET "TimeZone" TO 'UTC';








\unrestrict jLp8x8nbUpQnZOeEnc3q9Xx55QkzJQERhfAYKsqtgh5Fpz023R2VCbQsJAPBVZp

--
-- PostgreSQL database cluster dump complete
--

