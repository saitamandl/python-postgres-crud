--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: safeguard
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO safeguard;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: e_crud; Type: TABLE; Schema: public; Owner: safeguard
--

CREATE TABLE public.e_crud (
    e_id integer NOT NULL,
    e_name character varying(50),
    e_username character varying(50) NOT NULL,
    e_created_on timestamp with time zone NOT NULL,
    e_updated_on timestamp with time zone
);


ALTER TABLE public.e_crud OWNER TO safeguard;

--
-- Name: e_crud_e_id_seq; Type: SEQUENCE; Schema: public; Owner: safeguard
--

CREATE SEQUENCE public.e_crud_e_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.e_crud_e_id_seq OWNER TO safeguard;

--
-- Name: e_crud_e_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: safeguard
--

ALTER SEQUENCE public.e_crud_e_id_seq OWNED BY public.e_crud.e_id;


--
-- Name: e_crud e_id; Type: DEFAULT; Schema: public; Owner: safeguard
--

ALTER TABLE ONLY public.e_crud ALTER COLUMN e_id SET DEFAULT nextval('public.e_crud_e_id_seq'::regclass);


--
-- Data for Name: e_crud; Type: TABLE DATA; Schema: public; Owner: safeguard
--

COPY public.e_crud (e_id, e_name, e_username, e_created_on, e_updated_on) FROM stdin;
\.


--
-- Name: e_crud_e_id_seq; Type: SEQUENCE SET; Schema: public; Owner: safeguard
--

SELECT pg_catalog.setval('public.e_crud_e_id_seq', 1, false);


--
-- Name: e_crud e_crud_e_username_key; Type: CONSTRAINT; Schema: public; Owner: safeguard
--

ALTER TABLE ONLY public.e_crud
    ADD CONSTRAINT e_crud_e_username_key UNIQUE (e_username);


--
-- Name: e_crud e_crud_pkey; Type: CONSTRAINT; Schema: public; Owner: safeguard
--

ALTER TABLE ONLY public.e_crud
    ADD CONSTRAINT e_crud_pkey PRIMARY KEY (e_id);


--
-- PostgreSQL database dump complete
--

