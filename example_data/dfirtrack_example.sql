--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.16
-- Dumped by pg_dump version 9.5.16

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO dfirtrack;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO dfirtrack;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO dfirtrack;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO dfirtrack;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO dfirtrack;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO dfirtrack;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO dfirtrack;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO dfirtrack;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO dfirtrack;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO dfirtrack;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO dfirtrack;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO dfirtrack;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: dfirtrack_main_analysisstatus; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_analysisstatus (
    analysisstatus_id integer NOT NULL,
    analysisstatus_name character varying(30) NOT NULL,
    analysisstatus_note text
);


ALTER TABLE public.dfirtrack_main_analysisstatus OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_analysisstatus_analysisstatus_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_analysisstatus_analysisstatus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_analysisstatus_analysisstatus_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_analysisstatus_analysisstatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_analysisstatus_analysisstatus_id_seq OWNED BY public.dfirtrack_main_analysisstatus.analysisstatus_id;


--
-- Name: dfirtrack_main_analystmemo; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_analystmemo (
    analystmemo_id integer NOT NULL,
    analystmemo_note text NOT NULL,
    analystmemo_create_time timestamp with time zone NOT NULL,
    analystmemo_modify_time timestamp with time zone NOT NULL,
    analystmemo_created_by_user_id_id integer NOT NULL,
    analystmemo_modified_by_user_id_id integer NOT NULL,
    system_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_analystmemo OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_analystmemo_analystmemo_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_analystmemo_analystmemo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_analystmemo_analystmemo_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_analystmemo_analystmemo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_analystmemo_analystmemo_id_seq OWNED BY public.dfirtrack_main_analystmemo.analystmemo_id;


--
-- Name: dfirtrack_main_case; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_case (
    case_id integer NOT NULL,
    case_name character varying(50) NOT NULL,
    case_is_incident boolean NOT NULL,
    case_create_time timestamp with time zone NOT NULL,
    case_created_by_user_id_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_case OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_case_case_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_case_case_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_case_case_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_case_case_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_case_case_id_seq OWNED BY public.dfirtrack_main_case.case_id;


--
-- Name: dfirtrack_main_company; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_company (
    company_id integer NOT NULL,
    company_name character varying(50) NOT NULL,
    company_note text,
    division_id integer
);


ALTER TABLE public.dfirtrack_main_company OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_company_company_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_company_company_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_company_company_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_company_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_company_company_id_seq OWNED BY public.dfirtrack_main_company.company_id;


--
-- Name: dfirtrack_main_contact; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_contact (
    contact_id integer NOT NULL,
    contact_name character varying(100) NOT NULL,
    contact_phone character varying(50),
    contact_email character varying(100) NOT NULL,
    contact_note text
);


ALTER TABLE public.dfirtrack_main_contact OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_contact_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_contact_contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_contact_contact_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_contact_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_contact_contact_id_seq OWNED BY public.dfirtrack_main_contact.contact_id;


--
-- Name: dfirtrack_main_division; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_division (
    division_id integer NOT NULL,
    division_name character varying(50) NOT NULL,
    division_note text
);


ALTER TABLE public.dfirtrack_main_division OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_division_division_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_division_division_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_division_division_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_division_division_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_division_division_id_seq OWNED BY public.dfirtrack_main_division.division_id;


--
-- Name: dfirtrack_main_domain; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_domain (
    domain_id integer NOT NULL,
    domain_name character varying(100) NOT NULL,
    domain_note text
);


ALTER TABLE public.dfirtrack_main_domain OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_domain_domain_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_domain_domain_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_domain_domain_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_domain_domain_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_domain_domain_id_seq OWNED BY public.dfirtrack_main_domain.domain_id;


--
-- Name: dfirtrack_main_entry; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_entry (
    entry_id integer NOT NULL,
    entry_time timestamp with time zone NOT NULL,
    entry_sha1 character varying(40),
    entry_date character varying(10),
    entry_utc character varying(8),
    entry_system character varying(30),
    entry_type character varying(30),
    entry_content text,
    entry_note text,
    entry_create_time timestamp with time zone NOT NULL,
    entry_modify_time timestamp with time zone NOT NULL,
    entry_api_time timestamp with time zone,
    case_id integer,
    entry_created_by_user_id_id integer NOT NULL,
    entry_modified_by_user_id_id integer NOT NULL,
    system_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_entry OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_entry_entry_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_entry_entry_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_entry_entry_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_entry_entry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_entry_entry_id_seq OWNED BY public.dfirtrack_main_entry.entry_id;


--
-- Name: dfirtrack_main_headline; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_headline (
    headline_id integer NOT NULL,
    headline_name character varying(100) NOT NULL
);


ALTER TABLE public.dfirtrack_main_headline OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_headline_headline_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_headline_headline_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_headline_headline_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_headline_headline_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_headline_headline_id_seq OWNED BY public.dfirtrack_main_headline.headline_id;


--
-- Name: dfirtrack_main_ip; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_ip (
    ip_id integer NOT NULL,
    ip_ip inet NOT NULL
);


ALTER TABLE public.dfirtrack_main_ip OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_ip_ip_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_ip_ip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_ip_ip_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_ip_ip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_ip_ip_id_seq OWNED BY public.dfirtrack_main_ip.ip_id;


--
-- Name: dfirtrack_main_location; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_location (
    location_id integer NOT NULL,
    location_name character varying(50) NOT NULL,
    location_note text
);


ALTER TABLE public.dfirtrack_main_location OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_location_location_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_location_location_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_location_location_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_location_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_location_location_id_seq OWNED BY public.dfirtrack_main_location.location_id;


--
-- Name: dfirtrack_main_os; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_os (
    os_id integer NOT NULL,
    os_name character varying(30) NOT NULL
);


ALTER TABLE public.dfirtrack_main_os OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_os_os_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_os_os_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_os_os_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_os_os_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_os_os_id_seq OWNED BY public.dfirtrack_main_os.os_id;


--
-- Name: dfirtrack_main_osarch; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_osarch (
    osarch_id integer NOT NULL,
    osarch_name character varying(10) NOT NULL
);


ALTER TABLE public.dfirtrack_main_osarch OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_osarch_osarch_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_osarch_osarch_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_osarch_osarch_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_osarch_osarch_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_osarch_osarch_id_seq OWNED BY public.dfirtrack_main_osarch.osarch_id;


--
-- Name: dfirtrack_main_osimportname; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_osimportname (
    osimportname_id integer NOT NULL,
    osimportname_name character varying(30) NOT NULL,
    osimportname_importer character varying(30) NOT NULL,
    os_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_osimportname OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_osimportname_osimportname_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_osimportname_osimportname_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_osimportname_osimportname_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_osimportname_osimportname_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_osimportname_osimportname_id_seq OWNED BY public.dfirtrack_main_osimportname.osimportname_id;


--
-- Name: dfirtrack_main_reason; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_reason (
    reason_id integer NOT NULL,
    reason_name character varying(30) NOT NULL,
    reason_note text
);


ALTER TABLE public.dfirtrack_main_reason OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_reason_reason_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_reason_reason_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_reason_reason_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_reason_reason_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_reason_reason_id_seq OWNED BY public.dfirtrack_main_reason.reason_id;


--
-- Name: dfirtrack_main_recommendation; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_recommendation (
    recommendation_id integer NOT NULL,
    recommendation_name character varying(30) NOT NULL,
    recommendation_note text
);


ALTER TABLE public.dfirtrack_main_recommendation OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_recommendation_recommendation_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_recommendation_recommendation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_recommendation_recommendation_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_recommendation_recommendation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_recommendation_recommendation_id_seq OWNED BY public.dfirtrack_main_recommendation.recommendation_id;


--
-- Name: dfirtrack_main_reportitem; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_reportitem (
    reportitem_id integer NOT NULL,
    reportitem_subheadline character varying(100),
    reportitem_note text NOT NULL,
    reportitem_create_time timestamp with time zone NOT NULL,
    reportitem_modify_time timestamp with time zone NOT NULL,
    headline_id integer NOT NULL,
    reportitem_created_by_user_id_id integer NOT NULL,
    reportitem_modified_by_user_id_id integer NOT NULL,
    system_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_reportitem OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_reportitem_reportitem_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_reportitem_reportitem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_reportitem_reportitem_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_reportitem_reportitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_reportitem_reportitem_id_seq OWNED BY public.dfirtrack_main_reportitem.reportitem_id;


--
-- Name: dfirtrack_main_serviceprovider; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_serviceprovider (
    serviceprovider_id integer NOT NULL,
    serviceprovider_name character varying(50) NOT NULL,
    serviceprovider_note text
);


ALTER TABLE public.dfirtrack_main_serviceprovider OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_serviceprovider_serviceprovider_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_serviceprovider_serviceprovider_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_serviceprovider_serviceprovider_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_serviceprovider_serviceprovider_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_serviceprovider_serviceprovider_id_seq OWNED BY public.dfirtrack_main_serviceprovider.serviceprovider_id;


--
-- Name: dfirtrack_main_system; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_system (
    system_id integer NOT NULL,
    system_uuid uuid,
    system_name character varying(50) NOT NULL,
    system_dnssuffix character varying(50),
    system_install_time timestamp with time zone,
    system_lastbooted_time timestamp with time zone,
    system_deprecated_time timestamp with time zone,
    system_is_vm boolean,
    system_create_time timestamp with time zone NOT NULL,
    system_modify_time timestamp with time zone NOT NULL,
    system_api_time timestamp with time zone,
    analysisstatus_id integer,
    contact_id integer,
    domain_id integer,
    host_system_id integer,
    location_id integer,
    os_id integer,
    osarch_id integer,
    reason_id integer,
    recommendation_id integer,
    serviceprovider_id integer,
    system_created_by_user_id_id integer NOT NULL,
    system_modified_by_user_id_id integer NOT NULL,
    systemstatus_id integer NOT NULL,
    systemtype_id integer
);


ALTER TABLE public.dfirtrack_main_system OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_case; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_system_case (
    id integer NOT NULL,
    system_id integer NOT NULL,
    case_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_system_case OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_case_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_system_case_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_system_case_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_case_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_system_case_id_seq OWNED BY public.dfirtrack_main_system_case.id;


--
-- Name: dfirtrack_main_system_company; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_system_company (
    id integer NOT NULL,
    system_id integer NOT NULL,
    company_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_system_company OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_company_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_system_company_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_system_company_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_system_company_id_seq OWNED BY public.dfirtrack_main_system_company.id;


--
-- Name: dfirtrack_main_system_ip; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_system_ip (
    id integer NOT NULL,
    system_id integer NOT NULL,
    ip_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_system_ip OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_ip_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_system_ip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_system_ip_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_ip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_system_ip_id_seq OWNED BY public.dfirtrack_main_system_ip.id;


--
-- Name: dfirtrack_main_system_system_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_system_system_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_system_system_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_system_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_system_system_id_seq OWNED BY public.dfirtrack_main_system.system_id;


--
-- Name: dfirtrack_main_system_tag; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_system_tag (
    id integer NOT NULL,
    system_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_system_tag OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_system_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_system_tag_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_system_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_system_tag_id_seq OWNED BY public.dfirtrack_main_system_tag.id;


--
-- Name: dfirtrack_main_systemstatus; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_systemstatus (
    systemstatus_id integer NOT NULL,
    systemstatus_name character varying(30) NOT NULL,
    systemstatus_note text
);


ALTER TABLE public.dfirtrack_main_systemstatus OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_systemstatus_systemstatus_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_systemstatus_systemstatus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_systemstatus_systemstatus_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_systemstatus_systemstatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_systemstatus_systemstatus_id_seq OWNED BY public.dfirtrack_main_systemstatus.systemstatus_id;


--
-- Name: dfirtrack_main_systemtype; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_systemtype (
    systemtype_id integer NOT NULL,
    systemtype_name character varying(50) NOT NULL
);


ALTER TABLE public.dfirtrack_main_systemtype OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_systemtype_systemtype_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_systemtype_systemtype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_systemtype_systemtype_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_systemtype_systemtype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_systemtype_systemtype_id_seq OWNED BY public.dfirtrack_main_systemtype.systemtype_id;


--
-- Name: dfirtrack_main_systemuser; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_systemuser (
    systemuser_id integer NOT NULL,
    systemuser_name character varying(50) NOT NULL,
    systemuser_lastlogon_time timestamp with time zone,
    system_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_systemuser OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_systemuser_systemuser_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_systemuser_systemuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_systemuser_systemuser_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_systemuser_systemuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_systemuser_systemuser_id_seq OWNED BY public.dfirtrack_main_systemuser.systemuser_id;


--
-- Name: dfirtrack_main_tag; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_tag (
    tag_id integer NOT NULL,
    tag_name character varying(50) NOT NULL,
    tagcolor_id integer NOT NULL,
    tag_modified_by_user_id_id integer,
    tag_note text
);


ALTER TABLE public.dfirtrack_main_tag OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_tag_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_tag_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_tag_tag_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_tag_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_tag_tag_id_seq OWNED BY public.dfirtrack_main_tag.tag_id;


--
-- Name: dfirtrack_main_tagcolor; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_tagcolor (
    tagcolor_id integer NOT NULL,
    tagcolor_name character varying(20) NOT NULL
);


ALTER TABLE public.dfirtrack_main_tagcolor OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_tagcolor_tagcolor_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_tagcolor_tagcolor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_tagcolor_tagcolor_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_tagcolor_tagcolor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_tagcolor_tagcolor_id_seq OWNED BY public.dfirtrack_main_tagcolor.tagcolor_id;


--
-- Name: dfirtrack_main_task; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_task (
    task_id integer NOT NULL,
    task_note text,
    task_scheduled_time timestamp with time zone,
    task_started_time timestamp with time zone,
    task_finished_time timestamp with time zone,
    task_due_time timestamp with time zone,
    task_create_time timestamp with time zone NOT NULL,
    task_modify_time timestamp with time zone NOT NULL,
    parent_task_id integer,
    system_id integer,
    task_assigned_to_user_id_id integer,
    task_created_by_user_id_id integer NOT NULL,
    task_modified_by_user_id_id integer NOT NULL,
    taskname_id integer NOT NULL,
    taskpriority_id integer NOT NULL,
    taskstatus_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_task OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_task_tag; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_task_tag (
    id integer NOT NULL,
    task_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.dfirtrack_main_task_tag OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_task_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_task_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_task_tag_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_task_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_task_tag_id_seq OWNED BY public.dfirtrack_main_task_tag.id;


--
-- Name: dfirtrack_main_task_task_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_task_task_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_task_task_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_task_task_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_task_task_id_seq OWNED BY public.dfirtrack_main_task.task_id;


--
-- Name: dfirtrack_main_taskname; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_taskname (
    taskname_id integer NOT NULL,
    taskname_name character varying(50) NOT NULL
);


ALTER TABLE public.dfirtrack_main_taskname OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_taskname_taskname_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_taskname_taskname_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_taskname_taskname_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_taskname_taskname_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_taskname_taskname_id_seq OWNED BY public.dfirtrack_main_taskname.taskname_id;


--
-- Name: dfirtrack_main_taskpriority; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_taskpriority (
    taskpriority_id integer NOT NULL,
    taskpriority_name character varying(6) NOT NULL
);


ALTER TABLE public.dfirtrack_main_taskpriority OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_taskpriority_taskpriority_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_taskpriority_taskpriority_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_taskpriority_taskpriority_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_taskpriority_taskpriority_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_taskpriority_taskpriority_id_seq OWNED BY public.dfirtrack_main_taskpriority.taskpriority_id;


--
-- Name: dfirtrack_main_taskstatus; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.dfirtrack_main_taskstatus (
    taskstatus_id integer NOT NULL,
    taskstatus_name character varying(50) NOT NULL
);


ALTER TABLE public.dfirtrack_main_taskstatus OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_taskstatus_taskstatus_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.dfirtrack_main_taskstatus_taskstatus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dfirtrack_main_taskstatus_taskstatus_id_seq OWNER TO dfirtrack;

--
-- Name: dfirtrack_main_taskstatus_taskstatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.dfirtrack_main_taskstatus_taskstatus_id_seq OWNED BY public.dfirtrack_main_taskstatus.taskstatus_id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO dfirtrack;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO dfirtrack;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO dfirtrack;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO dfirtrack;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO dfirtrack;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO dfirtrack;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_q_ormq; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.django_q_ormq (
    id integer NOT NULL,
    key character varying(100) NOT NULL,
    payload text NOT NULL,
    lock timestamp with time zone
);


ALTER TABLE public.django_q_ormq OWNER TO dfirtrack;

--
-- Name: django_q_ormq_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.django_q_ormq_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_q_ormq_id_seq OWNER TO dfirtrack;

--
-- Name: django_q_ormq_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.django_q_ormq_id_seq OWNED BY public.django_q_ormq.id;


--
-- Name: django_q_schedule; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.django_q_schedule (
    id integer NOT NULL,
    func character varying(256) NOT NULL,
    hook character varying(256),
    args text,
    kwargs text,
    schedule_type character varying(1) NOT NULL,
    repeats integer NOT NULL,
    next_run timestamp with time zone,
    task character varying(100),
    name character varying(100),
    minutes smallint,
    CONSTRAINT django_q_schedule_minutes_check CHECK ((minutes >= 0))
);


ALTER TABLE public.django_q_schedule OWNER TO dfirtrack;

--
-- Name: django_q_schedule_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.django_q_schedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_q_schedule_id_seq OWNER TO dfirtrack;

--
-- Name: django_q_schedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.django_q_schedule_id_seq OWNED BY public.django_q_schedule.id;


--
-- Name: django_q_task; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.django_q_task (
    id character varying(32) NOT NULL,
    name character varying(100) NOT NULL,
    func character varying(256) NOT NULL,
    hook character varying(256),
    args text,
    kwargs text,
    result text,
    started timestamp with time zone NOT NULL,
    stopped timestamp with time zone NOT NULL,
    success boolean NOT NULL,
    "group" character varying(100)
);


ALTER TABLE public.django_q_task OWNER TO dfirtrack;

--
-- Name: django_q_task_id_seq; Type: SEQUENCE; Schema: public; Owner: dfirtrack
--

CREATE SEQUENCE public.django_q_task_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_q_task_id_seq OWNER TO dfirtrack;

--
-- Name: django_q_task_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dfirtrack
--

ALTER SEQUENCE public.django_q_task_id_seq OWNED BY public.django_q_task.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: dfirtrack
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO dfirtrack;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: analysisstatus_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_analysisstatus ALTER COLUMN analysisstatus_id SET DEFAULT nextval('public.dfirtrack_main_analysisstatus_analysisstatus_id_seq'::regclass);


--
-- Name: analystmemo_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_analystmemo ALTER COLUMN analystmemo_id SET DEFAULT nextval('public.dfirtrack_main_analystmemo_analystmemo_id_seq'::regclass);


--
-- Name: case_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_case ALTER COLUMN case_id SET DEFAULT nextval('public.dfirtrack_main_case_case_id_seq'::regclass);


--
-- Name: company_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_company ALTER COLUMN company_id SET DEFAULT nextval('public.dfirtrack_main_company_company_id_seq'::regclass);


--
-- Name: contact_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_contact ALTER COLUMN contact_id SET DEFAULT nextval('public.dfirtrack_main_contact_contact_id_seq'::regclass);


--
-- Name: division_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_division ALTER COLUMN division_id SET DEFAULT nextval('public.dfirtrack_main_division_division_id_seq'::regclass);


--
-- Name: domain_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_domain ALTER COLUMN domain_id SET DEFAULT nextval('public.dfirtrack_main_domain_domain_id_seq'::regclass);


--
-- Name: entry_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_entry ALTER COLUMN entry_id SET DEFAULT nextval('public.dfirtrack_main_entry_entry_id_seq'::regclass);


--
-- Name: headline_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_headline ALTER COLUMN headline_id SET DEFAULT nextval('public.dfirtrack_main_headline_headline_id_seq'::regclass);


--
-- Name: ip_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_ip ALTER COLUMN ip_id SET DEFAULT nextval('public.dfirtrack_main_ip_ip_id_seq'::regclass);


--
-- Name: location_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_location ALTER COLUMN location_id SET DEFAULT nextval('public.dfirtrack_main_location_location_id_seq'::regclass);


--
-- Name: os_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_os ALTER COLUMN os_id SET DEFAULT nextval('public.dfirtrack_main_os_os_id_seq'::regclass);


--
-- Name: osarch_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_osarch ALTER COLUMN osarch_id SET DEFAULT nextval('public.dfirtrack_main_osarch_osarch_id_seq'::regclass);


--
-- Name: osimportname_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_osimportname ALTER COLUMN osimportname_id SET DEFAULT nextval('public.dfirtrack_main_osimportname_osimportname_id_seq'::regclass);


--
-- Name: reason_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reason ALTER COLUMN reason_id SET DEFAULT nextval('public.dfirtrack_main_reason_reason_id_seq'::regclass);


--
-- Name: recommendation_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_recommendation ALTER COLUMN recommendation_id SET DEFAULT nextval('public.dfirtrack_main_recommendation_recommendation_id_seq'::regclass);


--
-- Name: reportitem_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reportitem ALTER COLUMN reportitem_id SET DEFAULT nextval('public.dfirtrack_main_reportitem_reportitem_id_seq'::regclass);


--
-- Name: serviceprovider_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_serviceprovider ALTER COLUMN serviceprovider_id SET DEFAULT nextval('public.dfirtrack_main_serviceprovider_serviceprovider_id_seq'::regclass);


--
-- Name: system_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system ALTER COLUMN system_id SET DEFAULT nextval('public.dfirtrack_main_system_system_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_case ALTER COLUMN id SET DEFAULT nextval('public.dfirtrack_main_system_case_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_company ALTER COLUMN id SET DEFAULT nextval('public.dfirtrack_main_system_company_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_ip ALTER COLUMN id SET DEFAULT nextval('public.dfirtrack_main_system_ip_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_tag ALTER COLUMN id SET DEFAULT nextval('public.dfirtrack_main_system_tag_id_seq'::regclass);


--
-- Name: systemstatus_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemstatus ALTER COLUMN systemstatus_id SET DEFAULT nextval('public.dfirtrack_main_systemstatus_systemstatus_id_seq'::regclass);


--
-- Name: systemtype_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemtype ALTER COLUMN systemtype_id SET DEFAULT nextval('public.dfirtrack_main_systemtype_systemtype_id_seq'::regclass);


--
-- Name: systemuser_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemuser ALTER COLUMN systemuser_id SET DEFAULT nextval('public.dfirtrack_main_systemuser_systemuser_id_seq'::regclass);


--
-- Name: tag_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_tag ALTER COLUMN tag_id SET DEFAULT nextval('public.dfirtrack_main_tag_tag_id_seq'::regclass);


--
-- Name: tagcolor_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_tagcolor ALTER COLUMN tagcolor_id SET DEFAULT nextval('public.dfirtrack_main_tagcolor_tagcolor_id_seq'::regclass);


--
-- Name: task_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task ALTER COLUMN task_id SET DEFAULT nextval('public.dfirtrack_main_task_task_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task_tag ALTER COLUMN id SET DEFAULT nextval('public.dfirtrack_main_task_tag_id_seq'::regclass);


--
-- Name: taskname_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskname ALTER COLUMN taskname_id SET DEFAULT nextval('public.dfirtrack_main_taskname_taskname_id_seq'::regclass);


--
-- Name: taskpriority_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskpriority ALTER COLUMN taskpriority_id SET DEFAULT nextval('public.dfirtrack_main_taskpriority_taskpriority_id_seq'::regclass);


--
-- Name: taskstatus_id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskstatus ALTER COLUMN taskstatus_id SET DEFAULT nextval('public.dfirtrack_main_taskstatus_taskstatus_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_q_ormq ALTER COLUMN id SET DEFAULT nextval('public.django_q_ormq_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_q_schedule ALTER COLUMN id SET DEFAULT nextval('public.django_q_schedule_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_q_task ALTER COLUMN id SET DEFAULT nextval('public.django_q_task_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add tagcolor	1	add_tagcolor
2	Can change tagcolor	1	change_tagcolor
3	Can delete tagcolor	1	delete_tagcolor
4	Can add task	2	add_task
5	Can change task	2	change_task
6	Can delete task	2	delete_task
7	Can add serviceprovider	3	add_serviceprovider
8	Can change serviceprovider	3	change_serviceprovider
9	Can delete serviceprovider	3	delete_serviceprovider
10	Can add entry	4	add_entry
11	Can change entry	4	change_entry
12	Can delete entry	4	delete_entry
13	Can add headline	5	add_headline
14	Can change headline	5	change_headline
15	Can delete headline	5	delete_headline
16	Can add analystmemo	6	add_analystmemo
17	Can change analystmemo	6	change_analystmemo
18	Can delete analystmemo	6	delete_analystmemo
19	Can add domain	7	add_domain
20	Can change domain	7	change_domain
21	Can delete domain	7	delete_domain
22	Can add systemtype	8	add_systemtype
23	Can change systemtype	8	change_systemtype
24	Can delete systemtype	8	delete_systemtype
25	Can add contact	9	add_contact
26	Can change contact	9	change_contact
27	Can delete contact	9	delete_contact
28	Can add taskstatus	10	add_taskstatus
29	Can change taskstatus	10	change_taskstatus
30	Can delete taskstatus	10	delete_taskstatus
31	Can add system	11	add_system
32	Can change system	11	change_system
33	Can delete system	11	delete_system
34	Can add systemuser	12	add_systemuser
35	Can change systemuser	12	change_systemuser
36	Can delete systemuser	12	delete_systemuser
37	Can add os	13	add_os
38	Can change os	13	change_os
39	Can delete os	13	delete_os
40	Can add osimportname	14	add_osimportname
41	Can change osimportname	14	change_osimportname
42	Can delete osimportname	14	delete_osimportname
43	Can add reason	15	add_reason
44	Can change reason	15	change_reason
45	Can delete reason	15	delete_reason
46	Can add taskpriority	16	add_taskpriority
47	Can change taskpriority	16	change_taskpriority
48	Can delete taskpriority	16	delete_taskpriority
49	Can add ip	17	add_ip
50	Can change ip	17	change_ip
51	Can delete ip	17	delete_ip
52	Can add osarch	18	add_osarch
53	Can change osarch	18	change_osarch
54	Can delete osarch	18	delete_osarch
55	Can add tag	19	add_tag
56	Can change tag	19	change_tag
57	Can delete tag	19	delete_tag
58	Can add recommendation	20	add_recommendation
59	Can change recommendation	20	change_recommendation
60	Can delete recommendation	20	delete_recommendation
61	Can add case	21	add_case
62	Can change case	21	change_case
63	Can delete case	21	delete_case
64	Can add company	22	add_company
65	Can change company	22	change_company
66	Can delete company	22	delete_company
67	Can add location	23	add_location
68	Can change location	23	change_location
69	Can delete location	23	delete_location
70	Can add taskname	24	add_taskname
71	Can change taskname	24	change_taskname
72	Can delete taskname	24	delete_taskname
73	Can add reportitem	25	add_reportitem
74	Can change reportitem	25	change_reportitem
75	Can delete reportitem	25	delete_reportitem
76	Can add division	26	add_division
77	Can change division	26	change_division
78	Can delete division	26	delete_division
79	Can add systemstatus	27	add_systemstatus
80	Can change systemstatus	27	change_systemstatus
81	Can delete systemstatus	27	delete_systemstatus
82	Can add analysisstatus	28	add_analysisstatus
83	Can change analysisstatus	28	change_analysisstatus
84	Can delete analysisstatus	28	delete_analysisstatus
85	Can add Scheduled task	29	add_schedule
86	Can change Scheduled task	29	change_schedule
87	Can delete Scheduled task	29	delete_schedule
88	Can add Queued task	30	add_ormq
89	Can change Queued task	30	change_ormq
90	Can delete Queued task	30	delete_ormq
91	Can add task	31	add_task
92	Can change task	31	change_task
93	Can delete task	31	delete_task
94	Can add Successful task	31	add_success
95	Can change Successful task	31	change_success
96	Can delete Successful task	31	delete_success
97	Can add Failed task	31	add_failure
98	Can change Failed task	31	change_failure
99	Can delete Failed task	31	delete_failure
100	Can add log entry	34	add_logentry
101	Can change log entry	34	change_logentry
102	Can delete log entry	34	delete_logentry
103	Can add group	35	add_group
104	Can change group	35	change_group
105	Can delete group	35	delete_group
106	Can add permission	36	add_permission
107	Can change permission	36	change_permission
108	Can delete permission	36	delete_permission
109	Can add user	37	add_user
110	Can change user	37	change_user
111	Can delete user	37	delete_user
112	Can add content type	38	add_contenttype
113	Can change content type	38	change_contenttype
114	Can delete content type	38	delete_contenttype
115	Can add session	39	add_session
116	Can change session	39	change_session
117	Can delete session	39	delete_session
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 117, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$100000$Nh1b9EW8P4Ik$cELsXr1r5ZlFLu2pIS9XA9gBnMWqCe1SPcVoFlGf8/M=	2019-04-25 18:05:31.259104+02	t	forensics				t	t	2019-04-25 18:05:12.927531+02
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: dfirtrack_main_analysisstatus; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_analysisstatus (analysisstatus_id, analysisstatus_name, analysisstatus_note) FROM stdin;
1	Needs analysis	\N
2	Ready for analysis	\N
3	Ongoing analysis	\N
4	Nothing to do	\N
5	Main analysis finished	\N
\.


--
-- Name: dfirtrack_main_analysisstatus_analysisstatus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_analysisstatus_analysisstatus_id_seq', 5, true);


--
-- Data for Name: dfirtrack_main_analystmemo; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_analystmemo (analystmemo_id, analystmemo_note, analystmemo_create_time, analystmemo_modify_time, analystmemo_created_by_user_id_id, analystmemo_modified_by_user_id_id, system_id) FROM stdin;
\.


--
-- Name: dfirtrack_main_analystmemo_analystmemo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_analystmemo_analystmemo_id_seq', 1, false);


--
-- Data for Name: dfirtrack_main_case; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_case (case_id, case_name, case_is_incident, case_create_time, case_created_by_user_id_id) FROM stdin;
1	Serious APT	t	2019-04-25 18:21:58.079054+02	1
2	Crimeware stuff	f	2019-04-25 18:22:24.728911+02	1
\.


--
-- Name: dfirtrack_main_case_case_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_case_case_id_seq', 2, true);


--
-- Data for Name: dfirtrack_main_company; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_company (company_id, company_name, company_note, division_id) FROM stdin;
2	Foobar s. r. o.	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.	1
1	Foobar GmbH	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.	2
3	Foobar Ltd.	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.	1
\.


--
-- Name: dfirtrack_main_company_company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_company_company_id_seq', 3, true);


--
-- Data for Name: dfirtrack_main_contact; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_contact (contact_id, contact_name, contact_phone, contact_email, contact_note) FROM stdin;
1	John Doe	0123456789	john.doe@foobar.com	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
2	Jane Doe	1234567890	jane.doe@foobar.com	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
3	Max Mustermann	0815	max.mustermann@foobar.de	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
\.


--
-- Name: dfirtrack_main_contact_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_contact_contact_id_seq', 3, true);


--
-- Data for Name: dfirtrack_main_division; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_division (division_id, division_name, division_note) FROM stdin;
1	Foobar SE	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
2	Foobar AG	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
\.


--
-- Name: dfirtrack_main_division_division_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_division_division_id_seq', 2, true);


--
-- Data for Name: dfirtrack_main_domain; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_domain (domain_id, domain_name, domain_note) FROM stdin;
2	FOOBAR-DE	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
1	FOOBAR-COM	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
\.


--
-- Name: dfirtrack_main_domain_domain_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_domain_domain_id_seq', 2, true);


--
-- Data for Name: dfirtrack_main_entry; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_entry (entry_id, entry_time, entry_sha1, entry_date, entry_utc, entry_system, entry_type, entry_content, entry_note, entry_create_time, entry_modify_time, entry_api_time, case_id, entry_created_by_user_id_id, entry_modified_by_user_id_id, system_id) FROM stdin;
\.


--
-- Name: dfirtrack_main_entry_entry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_entry_entry_id_seq', 1, false);


--
-- Data for Name: dfirtrack_main_headline; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_headline (headline_id, headline_name) FROM stdin;
1	Summary
\.


--
-- Name: dfirtrack_main_headline_headline_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_headline_headline_id_seq', 1, true);


--
-- Data for Name: dfirtrack_main_ip; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_ip (ip_id, ip_ip) FROM stdin;
\.


--
-- Name: dfirtrack_main_ip_ip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_ip_ip_id_seq', 1, false);


--
-- Data for Name: dfirtrack_main_location; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_location (location_id, location_name, location_note) FROM stdin;
1	Berlin	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
2	Frankfurt M.	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
3	New York	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
4	Shanghai	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
\.


--
-- Name: dfirtrack_main_location_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_location_location_id_seq', 4, true);


--
-- Data for Name: dfirtrack_main_os; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_os (os_id, os_name) FROM stdin;
1	Windows Server 2003
2	Windows Server 2003 R2
3	Windows Server 2008
4	Windows Server 2008 R2
5	Windows Server 2012
6	Windows Server 2012 R2
7	Windows Server 2016
8	Windows XP
9	Windows Vista
10	Windows 7
11	Windows 8
12	Windows 8.1
13	Windows 10
14	tbd
\.


--
-- Name: dfirtrack_main_os_os_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_os_os_id_seq', 14, true);


--
-- Data for Name: dfirtrack_main_osarch; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_osarch (osarch_id, osarch_name) FROM stdin;
1	32-Bit
2	64-Bit
\.


--
-- Name: dfirtrack_main_osarch_osarch_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_osarch_osarch_id_seq', 2, true);


--
-- Data for Name: dfirtrack_main_osimportname; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_osimportname (osimportname_id, osimportname_name, osimportname_importer, os_id) FROM stdin;
\.


--
-- Name: dfirtrack_main_osimportname_osimportname_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_osimportname_osimportname_id_seq', 1, false);


--
-- Data for Name: dfirtrack_main_reason; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_reason (reason_id, reason_name, reason_note) FROM stdin;
1	Host scan	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
2	Network scan	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
3	Antivirus alert	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
4	Vulnerability scan	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
\.


--
-- Name: dfirtrack_main_reason_reason_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_reason_reason_id_seq', 4, true);


--
-- Data for Name: dfirtrack_main_recommendation; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_recommendation (recommendation_id, recommendation_name, recommendation_note) FROM stdin;
1	No action required	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
2	Replace or reinstall	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
3	Make honeypot	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
4	Manual cleaning	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
\.


--
-- Name: dfirtrack_main_recommendation_recommendation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_recommendation_recommendation_id_seq', 4, true);


--
-- Data for Name: dfirtrack_main_reportitem; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_reportitem (reportitem_id, reportitem_subheadline, reportitem_note, reportitem_create_time, reportitem_modify_time, headline_id, reportitem_created_by_user_id_id, reportitem_modified_by_user_id_id, system_id) FROM stdin;
\.


--
-- Name: dfirtrack_main_reportitem_reportitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_reportitem_reportitem_id_seq', 1, false);


--
-- Data for Name: dfirtrack_main_serviceprovider; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_serviceprovider (serviceprovider_id, serviceprovider_name, serviceprovider_note) FROM stdin;
1	Foobar Service GmbH	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
2	Foobar Service Ltd.	Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
\.


--
-- Name: dfirtrack_main_serviceprovider_serviceprovider_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_serviceprovider_serviceprovider_id_seq', 2, true);


--
-- Data for Name: dfirtrack_main_system; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_system (system_id, system_uuid, system_name, system_dnssuffix, system_install_time, system_lastbooted_time, system_deprecated_time, system_is_vm, system_create_time, system_modify_time, system_api_time, analysisstatus_id, contact_id, domain_id, host_system_id, location_id, os_id, osarch_id, reason_id, recommendation_id, serviceprovider_id, system_created_by_user_id_id, system_modified_by_user_id_id, systemstatus_id, systemtype_id) FROM stdin;
26	\N	system_023	\N	\N	\N	\N	\N	2019-04-25 18:29:24.337334+02	2019-04-25 18:29:24.337052+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
27	\N	system_024	\N	\N	\N	\N	\N	2019-04-25 18:29:24.375644+02	2019-04-25 18:29:24.375339+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
28	\N	system_025	\N	\N	\N	\N	\N	2019-04-25 18:29:24.41456+02	2019-04-25 18:29:24.414275+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
29	\N	system_026	\N	\N	\N	\N	\N	2019-04-25 18:29:24.457236+02	2019-04-25 18:29:24.456878+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
30	\N	system_027	\N	\N	\N	\N	\N	2019-04-25 18:29:24.49162+02	2019-04-25 18:29:24.491332+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
31	\N	system_028	\N	\N	\N	\N	\N	2019-04-25 18:29:24.523283+02	2019-04-25 18:29:24.523006+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
32	\N	system_029	\N	\N	\N	\N	\N	2019-04-25 18:29:24.551762+02	2019-04-25 18:29:24.551486+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
33	\N	system_030	\N	\N	\N	\N	\N	2019-04-25 18:29:24.581097+02	2019-04-25 18:29:24.580858+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
34	\N	system_031	\N	\N	\N	\N	\N	2019-04-25 18:29:24.610604+02	2019-04-25 18:29:24.610349+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
35	\N	system_032	\N	\N	\N	\N	\N	2019-04-25 18:29:24.643298+02	2019-04-25 18:29:24.643027+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
36	\N	system_033	\N	\N	\N	\N	\N	2019-04-25 18:29:24.670208+02	2019-04-25 18:29:24.669963+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
37	\N	system_034	\N	\N	\N	\N	\N	2019-04-25 18:29:24.697821+02	2019-04-25 18:29:24.69757+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
38	\N	system_035	\N	\N	\N	\N	\N	2019-04-25 18:29:24.725449+02	2019-04-25 18:29:24.725201+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
39	\N	system_036	\N	\N	\N	\N	\N	2019-04-25 18:29:24.75295+02	2019-04-25 18:29:24.752689+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
40	\N	system_037	\N	\N	\N	\N	\N	2019-04-25 18:29:24.781484+02	2019-04-25 18:29:24.781214+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
41	\N	system_038	\N	\N	\N	\N	\N	2019-04-25 18:29:24.811367+02	2019-04-25 18:29:24.811028+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
42	\N	system_039	\N	\N	\N	\N	\N	2019-04-25 18:29:24.847705+02	2019-04-25 18:29:24.847422+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
43	\N	system_040	\N	\N	\N	\N	\N	2019-04-25 18:29:24.875304+02	2019-04-25 18:29:24.875049+02	\N	1	3	2	\N	1	4	\N	3	\N	1	1	1	2	\N
24	\N	system_021	\N	\N	\N	\N	\N	2019-04-25 18:29:24.254175+02	2019-04-25 18:31:25.903912+02	\N	4	3	2	\N	1	4	\N	3	1	1	1	1	1	\N
25	\N	system_022	\N	\N	\N	\N	\N	2019-04-25 18:29:24.298739+02	2019-04-25 18:32:17.835091+02	\N	5	3	2	\N	1	4	\N	3	2	1	1	1	4	\N
21	\N	dc_001	\N	\N	\N	\N	\N	2019-04-25 18:27:57.074772+02	2019-04-25 18:32:29.662544+02	\N	5	3	2	\N	1	4	2	1	2	\N	1	1	4	1
22	\N	dc_002	\N	\N	\N	\N	\N	2019-04-25 18:27:57.13085+02	2019-04-25 18:32:38.505085+02	\N	5	3	2	\N	1	4	2	1	2	\N	1	1	4	1
23	\N	dc_003	\N	\N	\N	\N	\N	2019-04-25 18:27:57.191567+02	2019-04-25 18:32:47.307554+02	\N	5	3	2	\N	1	4	2	1	2	\N	1	1	4	1
1	\N	system_001	\N	\N	\N	\N	\N	2019-04-25 18:26:08.035121+02	2019-04-25 18:32:58.80958+02	\N	5	3	2	\N	1	6	2	1	3	\N	1	1	4	6
2	\N	system_002	\N	\N	\N	\N	\N	2019-04-25 18:26:08.081481+02	2019-04-25 18:33:07.209811+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
3	\N	system_003	\N	\N	\N	\N	\N	2019-04-25 18:26:08.119666+02	2019-04-25 18:33:16.363256+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
4	\N	system_004	\N	\N	\N	\N	\N	2019-04-25 18:26:08.154896+02	2019-04-25 18:33:27.185414+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
5	\N	system_005	\N	\N	\N	\N	\N	2019-04-25 18:26:08.187493+02	2019-04-25 18:33:49.608084+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
6	\N	system_006	\N	\N	\N	\N	\N	2019-04-25 18:26:08.225046+02	2019-04-25 18:33:58.200209+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
7	\N	system_007	\N	\N	\N	\N	\N	2019-04-25 18:26:08.260471+02	2019-04-25 18:34:06.337661+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
8	\N	system_008	\N	\N	\N	\N	\N	2019-04-25 18:26:08.294953+02	2019-04-25 18:34:16.858275+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
9	\N	system_009	\N	\N	\N	\N	\N	2019-04-25 18:26:08.330805+02	2019-04-25 18:34:25.689089+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
10	\N	system_010	\N	\N	\N	\N	\N	2019-04-25 18:26:08.374762+02	2019-04-25 18:34:53.120792+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
11	\N	system_011	\N	\N	\N	\N	\N	2019-04-25 18:26:08.405592+02	2019-04-25 18:35:01.039409+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
12	\N	system_012	\N	\N	\N	\N	\N	2019-04-25 18:26:08.441884+02	2019-04-25 18:35:09.387807+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
13	\N	system_013	\N	\N	\N	\N	\N	2019-04-25 18:26:08.485831+02	2019-04-25 18:35:39.80106+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
14	\N	system_014	\N	\N	\N	\N	\N	2019-04-25 18:26:08.518532+02	2019-04-25 18:35:49.069312+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
15	\N	system_015	\N	\N	\N	\N	\N	2019-04-25 18:26:08.550026+02	2019-04-25 18:35:59.870229+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
16	\N	system_016	\N	\N	\N	\N	\N	2019-04-25 18:26:08.59518+02	2019-04-25 18:36:11.157427+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
17	\N	system_017	\N	\N	\N	\N	\N	2019-04-25 18:26:08.626785+02	2019-04-25 18:36:21.534113+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
18	\N	system_018	\N	\N	\N	\N	\N	2019-04-25 18:26:08.662466+02	2019-04-25 18:36:30.143104+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
19	\N	system_019	\N	\N	\N	\N	\N	2019-04-25 18:26:08.70692+02	2019-04-25 18:36:40.01088+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
20	\N	system_020	\N	\N	\N	\N	\N	2019-04-25 18:26:08.76541+02	2019-04-25 18:36:49.149353+02	\N	5	3	2	\N	1	6	2	1	2	\N	1	1	4	6
48	\N	asys_5	\N	\N	\N	\N	\N	2019-04-25 18:38:31.414529+02	2019-04-25 18:38:31.41405+02	\N	1	1	1	\N	3	7	\N	2	\N	2	1	1	2	\N
44	\N	asys_1	\N	\N	\N	\N	\N	2019-04-25 18:38:31.277118+02	2019-04-25 18:39:39.019196+02	\N	4	1	1	\N	3	7	\N	2	1	2	1	1	1	\N
45	\N	asys_2	\N	\N	\N	\N	\N	2019-04-25 18:38:31.312743+02	2019-04-25 18:40:09.290012+02	\N	5	1	1	\N	3	7	\N	2	2	2	1	1	4	\N
46	\N	asys_3	\N	\N	\N	\N	\N	2019-04-25 18:38:31.343861+02	2019-04-25 18:40:36.598502+02	\N	3	1	1	\N	3	7	\N	2	\N	2	1	1	3	\N
47	\N	asys_4	\N	\N	\N	\N	\N	2019-04-25 18:38:31.374735+02	2019-04-25 18:41:02.505401+02	\N	3	1	1	\N	3	7	\N	2	\N	2	1	1	3	\N
49	\N	zsys_1	\N	\N	\N	\N	\N	2019-04-25 18:42:50.434858+02	2019-04-25 18:42:50.434474+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
50	\N	zsys_2	\N	\N	\N	\N	\N	2019-04-25 18:42:50.471806+02	2019-04-25 18:42:50.471525+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
51	\N	zsys_3	\N	\N	\N	\N	\N	2019-04-25 18:42:50.503362+02	2019-04-25 18:42:50.503074+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
52	\N	zsys_4	\N	\N	\N	\N	\N	2019-04-25 18:42:50.549556+02	2019-04-25 18:42:50.549244+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
53	\N	zsys_5	\N	\N	\N	\N	\N	2019-04-25 18:42:50.584078+02	2019-04-25 18:42:50.583705+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
54	\N	zsys_6	\N	\N	\N	\N	\N	2019-04-25 18:42:50.638952+02	2019-04-25 18:42:50.638264+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
55	\N	zsys_7	\N	\N	\N	\N	\N	2019-04-25 18:42:50.688539+02	2019-04-25 18:42:50.687978+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
56	\N	zsys_8	\N	\N	\N	\N	\N	2019-04-25 18:42:50.733959+02	2019-04-25 18:42:50.733675+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
57	\N	zsys_9	\N	\N	\N	\N	\N	2019-04-25 18:42:50.77799+02	2019-04-25 18:42:50.777652+02	\N	1	2	1	\N	4	4	\N	1	\N	2	1	1	2	\N
\.


--
-- Data for Name: dfirtrack_main_system_case; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_system_case (id, system_id, case_id) FROM stdin;
1	1	1
2	2	1
3	3	1
4	4	1
5	5	1
6	6	1
7	7	1
8	8	1
9	9	1
10	10	1
11	11	1
12	12	1
13	13	1
14	14	1
15	15	1
16	16	1
17	17	1
18	18	1
19	19	1
20	20	1
21	21	1
22	22	1
23	23	1
\.


--
-- Name: dfirtrack_main_system_case_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_system_case_id_seq', 23, true);


--
-- Data for Name: dfirtrack_main_system_company; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_system_company (id, system_id, company_id) FROM stdin;
1	1	1
2	2	1
3	3	1
4	4	1
5	5	1
6	6	1
7	7	1
8	8	1
9	9	1
10	10	1
11	11	1
12	12	1
13	13	1
14	14	1
15	15	1
16	16	1
17	17	1
18	18	1
19	19	1
20	20	1
21	21	1
22	22	1
23	23	1
24	24	1
25	25	1
26	26	1
27	27	1
28	28	1
29	29	1
30	30	1
31	31	1
32	32	1
33	33	1
34	34	1
35	35	1
36	36	1
37	37	1
38	38	1
39	39	1
40	40	1
41	41	1
42	42	1
43	43	1
44	44	3
45	45	3
46	46	3
47	47	3
48	48	3
49	49	2
50	49	3
51	50	2
52	50	3
53	51	2
54	51	3
55	52	2
56	52	3
57	53	2
58	53	3
59	54	2
60	54	3
61	55	2
62	55	3
63	56	2
64	56	3
65	57	2
66	57	3
\.


--
-- Name: dfirtrack_main_system_company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_system_company_id_seq', 66, true);


--
-- Data for Name: dfirtrack_main_system_ip; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_system_ip (id, system_id, ip_id) FROM stdin;
\.


--
-- Name: dfirtrack_main_system_ip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_system_ip_id_seq', 1, false);


--
-- Name: dfirtrack_main_system_system_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_system_system_id_seq', 57, true);


--
-- Data for Name: dfirtrack_main_system_tag; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_system_tag (id, system_id, tag_id) FROM stdin;
1	1	2
2	2	2
3	3	2
4	4	2
5	5	2
6	6	2
7	7	2
8	8	2
9	9	2
10	10	2
11	11	2
12	12	2
13	13	2
14	14	2
15	15	2
16	16	2
17	17	2
18	18	2
19	19	2
20	20	2
21	21	2
22	21	3
23	22	2
24	22	3
25	23	2
26	23	3
\.


--
-- Name: dfirtrack_main_system_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_system_tag_id_seq', 26, true);


--
-- Data for Name: dfirtrack_main_systemstatus; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_systemstatus (systemstatus_id, systemstatus_name, systemstatus_note) FROM stdin;
1	Clean	\N
2	Unknown	\N
3	Analysis ongoing	\N
4	Compromised	\N
5	Remediation done	\N
6	Reinstalled	\N
7	Removed	\N
8	Not analyzed	\N
\.


--
-- Name: dfirtrack_main_systemstatus_systemstatus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_systemstatus_systemstatus_id_seq', 8, true);


--
-- Data for Name: dfirtrack_main_systemtype; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_systemtype (systemtype_id, systemtype_name) FROM stdin;
1	Domaincontroller
2	Mailserver
3	Fileserver
4	USB-Drive
5	Client
6	Memberserver
7	Exchange
8	Sharepoint
\.


--
-- Name: dfirtrack_main_systemtype_systemtype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_systemtype_systemtype_id_seq', 8, true);


--
-- Data for Name: dfirtrack_main_systemuser; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_systemuser (systemuser_id, systemuser_name, systemuser_lastlogon_time, system_id) FROM stdin;
\.


--
-- Name: dfirtrack_main_systemuser_systemuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_systemuser_systemuser_id_seq', 1, false);


--
-- Data for Name: dfirtrack_main_tag; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_tag (tag_id, tag_name, tagcolor_id, tag_modified_by_user_id_id, tag_note) FROM stdin;
1	Suspicious	3	\N	\N
2	Backdoor installed	4	\N	\N
3	Credential harvesting	4	\N	\N
4	Data theft	4	\N	\N
5	Important	4	\N	\N
\.


--
-- Name: dfirtrack_main_tag_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_tag_tag_id_seq', 5, true);


--
-- Data for Name: dfirtrack_main_tagcolor; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_tagcolor (tagcolor_id, tagcolor_name) FROM stdin;
1	primary
2	green
3	orange
4	red
5	black
6	white
\.


--
-- Name: dfirtrack_main_tagcolor_tagcolor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_tagcolor_tagcolor_id_seq', 6, true);


--
-- Data for Name: dfirtrack_main_task; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_task (task_id, task_note, task_scheduled_time, task_started_time, task_finished_time, task_due_time, task_create_time, task_modify_time, parent_task_id, system_id, task_assigned_to_user_id_id, task_created_by_user_id_id, task_modified_by_user_id_id, taskname_id, taskpriority_id, taskstatus_id) FROM stdin;
3	\N	\N	\N	\N	\N	2019-04-25 18:30:23.423698+02	2019-04-25 18:30:23.423718+02	\N	26	\N	1	1	1	2	1
4	\N	\N	\N	\N	\N	2019-04-25 18:30:23.444241+02	2019-04-25 18:30:23.44431+02	\N	27	\N	1	1	1	2	1
5	\N	\N	\N	\N	\N	2019-04-25 18:30:23.464059+02	2019-04-25 18:30:23.464078+02	\N	28	\N	1	1	1	2	1
6	\N	\N	\N	\N	\N	2019-04-25 18:30:23.484399+02	2019-04-25 18:30:23.484425+02	\N	29	\N	1	1	1	2	1
7	\N	\N	\N	\N	\N	2019-04-25 18:30:23.502439+02	2019-04-25 18:30:23.502462+02	\N	30	\N	1	1	1	2	1
8	\N	\N	\N	\N	\N	2019-04-25 18:30:23.522576+02	2019-04-25 18:30:23.522595+02	\N	31	\N	1	1	1	2	1
9	\N	\N	\N	\N	\N	2019-04-25 18:30:23.540505+02	2019-04-25 18:30:23.540524+02	\N	32	\N	1	1	1	2	1
10	\N	\N	\N	\N	\N	2019-04-25 18:30:23.559244+02	2019-04-25 18:30:23.559263+02	\N	33	\N	1	1	1	2	1
11	\N	\N	\N	\N	\N	2019-04-25 18:30:23.580551+02	2019-04-25 18:30:23.580569+02	\N	34	\N	1	1	1	2	1
12	\N	\N	\N	\N	\N	2019-04-25 18:30:23.598584+02	2019-04-25 18:30:23.598603+02	\N	35	\N	1	1	1	2	1
13	\N	\N	\N	\N	\N	2019-04-25 18:30:23.616531+02	2019-04-25 18:30:23.616549+02	\N	36	\N	1	1	1	2	1
14	\N	\N	\N	\N	\N	2019-04-25 18:30:23.633834+02	2019-04-25 18:30:23.63385+02	\N	37	\N	1	1	1	2	1
15	\N	\N	\N	\N	\N	2019-04-25 18:30:23.655539+02	2019-04-25 18:30:23.655557+02	\N	38	\N	1	1	1	2	1
16	\N	\N	\N	\N	\N	2019-04-25 18:30:23.676278+02	2019-04-25 18:30:23.676297+02	\N	39	\N	1	1	1	2	1
17	\N	\N	\N	\N	\N	2019-04-25 18:30:23.697361+02	2019-04-25 18:30:23.697379+02	\N	40	\N	1	1	1	2	1
18	\N	\N	\N	\N	\N	2019-04-25 18:30:23.717764+02	2019-04-25 18:30:23.717782+02	\N	41	\N	1	1	1	2	1
19	\N	\N	\N	\N	\N	2019-04-25 18:30:23.73767+02	2019-04-25 18:30:23.737688+02	\N	42	\N	1	1	1	2	1
20	\N	\N	\N	\N	\N	2019-04-25 18:30:23.754858+02	2019-04-25 18:30:23.754876+02	\N	43	\N	1	1	1	2	1
23	\N	\N	\N	\N	\N	2019-04-25 18:30:23.808613+02	2019-04-25 18:30:23.808631+02	\N	26	\N	1	1	2	2	1
24	\N	\N	\N	\N	\N	2019-04-25 18:30:23.824157+02	2019-04-25 18:30:23.824174+02	\N	27	\N	1	1	2	2	1
25	\N	\N	\N	\N	\N	2019-04-25 18:30:23.840633+02	2019-04-25 18:30:23.840652+02	\N	28	\N	1	1	2	2	1
26	\N	\N	\N	\N	\N	2019-04-25 18:30:23.856168+02	2019-04-25 18:30:23.856185+02	\N	29	\N	1	1	2	2	1
27	\N	\N	\N	\N	\N	2019-04-25 18:30:23.872589+02	2019-04-25 18:30:23.872606+02	\N	30	\N	1	1	2	2	1
28	\N	\N	\N	\N	\N	2019-04-25 18:30:23.887915+02	2019-04-25 18:30:23.887933+02	\N	31	\N	1	1	2	2	1
29	\N	\N	\N	\N	\N	2019-04-25 18:30:23.902461+02	2019-04-25 18:30:23.90248+02	\N	32	\N	1	1	2	2	1
30	\N	\N	\N	\N	\N	2019-04-25 18:30:23.916651+02	2019-04-25 18:30:23.916666+02	\N	33	\N	1	1	2	2	1
31	\N	\N	\N	\N	\N	2019-04-25 18:30:23.929528+02	2019-04-25 18:30:23.929542+02	\N	34	\N	1	1	2	2	1
32	\N	\N	\N	\N	\N	2019-04-25 18:30:23.942493+02	2019-04-25 18:30:23.942507+02	\N	35	\N	1	1	2	2	1
33	\N	\N	\N	\N	\N	2019-04-25 18:30:23.967678+02	2019-04-25 18:30:23.967697+02	\N	36	\N	1	1	2	2	1
34	\N	\N	\N	\N	\N	2019-04-25 18:30:23.985039+02	2019-04-25 18:30:23.985055+02	\N	37	\N	1	1	2	2	1
35	\N	\N	\N	\N	\N	2019-04-25 18:30:24.000108+02	2019-04-25 18:30:24.000124+02	\N	38	\N	1	1	2	2	1
36	\N	\N	\N	\N	\N	2019-04-25 18:30:24.014058+02	2019-04-25 18:30:24.014072+02	\N	39	\N	1	1	2	2	1
37	\N	\N	\N	\N	\N	2019-04-25 18:30:24.030199+02	2019-04-25 18:30:24.030216+02	\N	40	\N	1	1	2	2	1
38	\N	\N	\N	\N	\N	2019-04-25 18:30:24.046701+02	2019-04-25 18:30:24.046719+02	\N	41	\N	1	1	2	2	1
39	\N	\N	\N	\N	\N	2019-04-25 18:30:24.063184+02	2019-04-25 18:30:24.063204+02	\N	42	\N	1	1	2	2	1
40	\N	\N	\N	\N	\N	2019-04-25 18:30:24.07961+02	2019-04-25 18:30:24.079647+02	\N	43	\N	1	1	2	2	1
43	\N	\N	\N	\N	\N	2019-04-25 18:30:24.127502+02	2019-04-25 18:30:24.127527+02	\N	26	\N	1	1	3	2	1
44	\N	\N	\N	\N	\N	2019-04-25 18:30:24.143627+02	2019-04-25 18:30:24.143646+02	\N	27	\N	1	1	3	2	1
45	\N	\N	\N	\N	\N	2019-04-25 18:30:24.159211+02	2019-04-25 18:30:24.159228+02	\N	28	\N	1	1	3	2	1
46	\N	\N	\N	\N	\N	2019-04-25 18:30:24.175358+02	2019-04-25 18:30:24.175376+02	\N	29	\N	1	1	3	2	1
47	\N	\N	\N	\N	\N	2019-04-25 18:30:24.193842+02	2019-04-25 18:30:24.193861+02	\N	30	\N	1	1	3	2	1
48	\N	\N	\N	\N	\N	2019-04-25 18:30:24.211239+02	2019-04-25 18:30:24.211257+02	\N	31	\N	1	1	3	2	1
49	\N	\N	\N	\N	\N	2019-04-25 18:30:24.227774+02	2019-04-25 18:30:24.227793+02	\N	32	\N	1	1	3	2	1
50	\N	\N	\N	\N	\N	2019-04-25 18:30:24.243721+02	2019-04-25 18:30:24.243738+02	\N	33	\N	1	1	3	2	1
51	\N	\N	\N	\N	\N	2019-04-25 18:30:24.258203+02	2019-04-25 18:30:24.25822+02	\N	34	\N	1	1	3	2	1
52	\N	\N	\N	\N	\N	2019-04-25 18:30:24.272417+02	2019-04-25 18:30:24.272433+02	\N	35	\N	1	1	3	2	1
53	\N	\N	\N	\N	\N	2019-04-25 18:30:24.286107+02	2019-04-25 18:30:24.286123+02	\N	36	\N	1	1	3	2	1
54	\N	\N	\N	\N	\N	2019-04-25 18:30:24.29955+02	2019-04-25 18:30:24.299565+02	\N	37	\N	1	1	3	2	1
55	\N	\N	\N	\N	\N	2019-04-25 18:30:24.312659+02	2019-04-25 18:30:24.312674+02	\N	38	\N	1	1	3	2	1
56	\N	\N	\N	\N	\N	2019-04-25 18:30:24.325615+02	2019-04-25 18:30:24.325629+02	\N	39	\N	1	1	3	2	1
57	\N	\N	\N	\N	\N	2019-04-25 18:30:24.338137+02	2019-04-25 18:30:24.338151+02	\N	40	\N	1	1	3	2	1
58	\N	\N	\N	\N	\N	2019-04-25 18:30:24.350575+02	2019-04-25 18:30:24.350588+02	\N	41	\N	1	1	3	2	1
59	\N	\N	\N	\N	\N	2019-04-25 18:30:24.362859+02	2019-04-25 18:30:24.362873+02	\N	42	\N	1	1	3	2	1
60	\N	\N	\N	\N	\N	2019-04-25 18:30:24.375326+02	2019-04-25 18:30:24.37534+02	\N	43	\N	1	1	3	2	1
63	\N	\N	\N	\N	\N	2019-04-25 18:30:24.432917+02	2019-04-25 18:30:24.432936+02	\N	26	\N	1	1	4	2	1
64	\N	\N	\N	\N	\N	2019-04-25 18:30:24.44739+02	2019-04-25 18:30:24.447405+02	\N	27	\N	1	1	4	2	1
65	\N	\N	\N	\N	\N	2019-04-25 18:30:24.473224+02	2019-04-25 18:30:24.473245+02	\N	28	\N	1	1	4	2	1
66	\N	\N	\N	\N	\N	2019-04-25 18:30:24.489217+02	2019-04-25 18:30:24.489235+02	\N	29	\N	1	1	4	2	1
67	\N	\N	\N	\N	\N	2019-04-25 18:30:24.503595+02	2019-04-25 18:30:24.50361+02	\N	30	\N	1	1	4	2	1
68	\N	\N	\N	\N	\N	2019-04-25 18:30:24.517212+02	2019-04-25 18:30:24.517226+02	\N	31	\N	1	1	4	2	1
69	\N	\N	\N	\N	\N	2019-04-25 18:30:24.542657+02	2019-04-25 18:30:24.542689+02	\N	32	\N	1	1	4	2	1
70	\N	\N	\N	\N	\N	2019-04-25 18:30:24.556749+02	2019-04-25 18:30:24.556762+02	\N	33	\N	1	1	4	2	1
71	\N	\N	\N	\N	\N	2019-04-25 18:30:24.569732+02	2019-04-25 18:30:24.569745+02	\N	34	\N	1	1	4	2	1
72	\N	\N	\N	\N	\N	2019-04-25 18:30:24.583158+02	2019-04-25 18:30:24.583172+02	\N	35	\N	1	1	4	2	1
73	\N	\N	\N	\N	\N	2019-04-25 18:30:24.596207+02	2019-04-25 18:30:24.596222+02	\N	36	\N	1	1	4	2	1
74	\N	\N	\N	\N	\N	2019-04-25 18:30:24.612327+02	2019-04-25 18:30:24.612345+02	\N	37	\N	1	1	4	2	1
75	\N	\N	\N	\N	\N	2019-04-25 18:30:24.626827+02	2019-04-25 18:30:24.626844+02	\N	38	\N	1	1	4	2	1
76	\N	\N	\N	\N	\N	2019-04-25 18:30:24.64069+02	2019-04-25 18:30:24.640705+02	\N	39	\N	1	1	4	2	1
77	\N	\N	\N	\N	\N	2019-04-25 18:30:24.654031+02	2019-04-25 18:30:24.654046+02	\N	40	\N	1	1	4	2	1
78	\N	\N	\N	\N	\N	2019-04-25 18:30:24.667356+02	2019-04-25 18:30:24.667372+02	\N	41	\N	1	1	4	2	1
79	\N	\N	\N	\N	\N	2019-04-25 18:30:24.683126+02	2019-04-25 18:30:24.683144+02	\N	42	\N	1	1	4	2	1
80	\N	\N	\N	\N	\N	2019-04-25 18:30:24.697777+02	2019-04-25 18:30:24.697792+02	\N	43	\N	1	1	4	2	1
83	\N	\N	\N	\N	\N	2019-04-25 18:30:24.742393+02	2019-04-25 18:30:24.74241+02	\N	26	\N	1	1	5	2	1
84	\N	\N	\N	\N	\N	2019-04-25 18:30:24.757086+02	2019-04-25 18:30:24.757101+02	\N	27	\N	1	1	5	2	1
85	\N	\N	\N	\N	\N	2019-04-25 18:30:24.78316+02	2019-04-25 18:30:24.783181+02	\N	28	\N	1	1	5	2	1
86	\N	\N	\N	\N	\N	2019-04-25 18:30:24.798896+02	2019-04-25 18:30:24.798911+02	\N	29	\N	1	1	5	2	1
87	\N	\N	\N	\N	\N	2019-04-25 18:30:24.813389+02	2019-04-25 18:30:24.813404+02	\N	30	\N	1	1	5	2	1
88	\N	\N	\N	\N	\N	2019-04-25 18:30:24.829571+02	2019-04-25 18:30:24.829586+02	\N	31	\N	1	1	5	2	1
89	\N	\N	\N	\N	\N	2019-04-25 18:30:24.843294+02	2019-04-25 18:30:24.84331+02	\N	32	\N	1	1	5	2	1
90	\N	\N	\N	\N	\N	2019-04-25 18:30:24.856604+02	2019-04-25 18:30:24.85662+02	\N	33	\N	1	1	5	2	1
91	\N	\N	\N	\N	\N	2019-04-25 18:30:24.86939+02	2019-04-25 18:30:24.869404+02	\N	34	\N	1	1	5	2	1
92	\N	\N	\N	\N	\N	2019-04-25 18:30:24.88196+02	2019-04-25 18:30:24.881975+02	\N	35	\N	1	1	5	2	1
93	\N	\N	\N	\N	\N	2019-04-25 18:30:24.913645+02	2019-04-25 18:30:24.913674+02	\N	36	\N	1	1	5	2	1
94	\N	\N	\N	\N	\N	2019-04-25 18:30:24.940802+02	2019-04-25 18:30:24.940822+02	\N	37	\N	1	1	5	2	1
95	\N	\N	\N	\N	\N	2019-04-25 18:30:24.958177+02	2019-04-25 18:30:24.958191+02	\N	38	\N	1	1	5	2	1
96	\N	\N	\N	\N	\N	2019-04-25 18:30:24.972135+02	2019-04-25 18:30:24.972148+02	\N	39	\N	1	1	5	2	1
97	\N	\N	\N	\N	\N	2019-04-25 18:30:24.999112+02	2019-04-25 18:30:24.999129+02	\N	40	\N	1	1	5	2	1
41	\N	\N	2019-04-25 18:30:51.753729+02	2019-04-25 18:30:52.782707+02	\N	2019-04-25 18:30:24.095529+02	2019-04-25 18:30:52.783684+02	\N	24	1	1	1	3	2	3
61	\N	\N	2019-04-25 18:30:55.921498+02	2019-04-25 18:30:57.141807+02	\N	2019-04-25 18:30:24.389164+02	2019-04-25 18:30:57.142859+02	\N	24	1	1	1	4	2	3
2	\N	\N	2019-04-25 18:31:42.513914+02	2019-04-25 18:31:44.273368+02	\N	2019-04-25 18:30:23.402844+02	2019-04-25 18:31:44.274364+02	\N	25	1	1	1	1	2	3
22	\N	\N	2019-04-25 18:31:46.56327+02	2019-04-25 18:31:53.491198+02	\N	2019-04-25 18:30:23.792599+02	2019-04-25 18:31:53.492147+02	\N	25	1	1	1	2	2	3
62	\N	\N	2019-04-25 18:31:59.078027+02	2019-04-25 18:32:00.115952+02	\N	2019-04-25 18:30:24.407179+02	2019-04-25 18:32:00.116945+02	\N	25	1	1	1	4	2	3
82	\N	\N	2019-04-25 18:32:02.64838+02	2019-04-25 18:32:03.582643+02	\N	2019-04-25 18:30:24.727662+02	2019-04-25 18:32:03.583641+02	\N	25	1	1	1	5	2	3
98	\N	\N	\N	\N	\N	2019-04-25 18:30:25.014893+02	2019-04-25 18:30:25.014908+02	\N	41	\N	1	1	5	2	1
99	\N	\N	\N	\N	\N	2019-04-25 18:30:25.031871+02	2019-04-25 18:30:25.031889+02	\N	42	\N	1	1	5	2	1
100	\N	\N	\N	\N	\N	2019-04-25 18:30:25.096434+02	2019-04-25 18:30:25.096454+02	\N	43	\N	1	1	5	2	1
1	\N	\N	2019-04-25 18:30:44.523916+02	2019-04-25 18:30:45.663308+02	\N	2019-04-25 18:30:23.374361+02	2019-04-25 18:30:45.664395+02	\N	24	1	1	1	1	2	3
21	\N	\N	2019-04-25 18:30:48.009144+02	2019-04-25 18:30:49.095527+02	\N	2019-04-25 18:30:23.775013+02	2019-04-25 18:30:49.096756+02	\N	24	1	1	1	2	2	3
81	\N	\N	2019-04-25 18:30:59.783382+02	2019-04-25 18:31:00.66816+02	\N	2019-04-25 18:30:24.712742+02	2019-04-25 18:31:00.669315+02	\N	24	1	1	1	5	2	3
42	\N	\N	2019-04-25 18:31:55.64075+02	2019-04-25 18:31:56.681917+02	\N	2019-04-25 18:30:24.111797+02	2019-04-25 18:31:56.68297+02	\N	25	1	1	1	3	2	3
105	\N	\N	\N	\N	\N	2019-04-25 18:39:02.921158+02	2019-04-25 18:39:02.921176+02	\N	48	1	1	1	1	3	1
110	\N	\N	\N	\N	\N	2019-04-25 18:39:03.02493+02	2019-04-25 18:39:03.024949+02	\N	48	1	1	1	2	3	1
114	\N	\N	\N	\N	\N	2019-04-25 18:39:03.097528+02	2019-04-25 18:39:03.097547+02	\N	47	1	1	1	3	3	1
115	\N	\N	\N	\N	\N	2019-04-25 18:39:03.114634+02	2019-04-25 18:39:03.114653+02	\N	48	1	1	1	3	3	1
118	\N	\N	\N	\N	\N	2019-04-25 18:39:03.165861+02	2019-04-25 18:39:03.165879+02	\N	46	1	1	1	4	3	1
119	\N	\N	\N	\N	\N	2019-04-25 18:39:03.182133+02	2019-04-25 18:39:03.182151+02	\N	47	1	1	1	4	3	1
120	\N	\N	\N	\N	\N	2019-04-25 18:39:03.198297+02	2019-04-25 18:39:03.198317+02	\N	48	1	1	1	4	3	1
123	\N	\N	\N	\N	\N	2019-04-25 18:39:03.254828+02	2019-04-25 18:39:03.254846+02	\N	46	1	1	1	5	3	1
124	\N	\N	\N	\N	\N	2019-04-25 18:39:03.271565+02	2019-04-25 18:39:03.271584+02	\N	47	1	1	1	5	3	1
125	\N	\N	\N	\N	\N	2019-04-25 18:39:03.290787+02	2019-04-25 18:39:03.290806+02	\N	48	1	1	1	5	3	1
101	\N	\N	2019-04-25 18:39:16.199343+02	2019-04-25 18:39:17.450818+02	\N	2019-04-25 18:39:02.851398+02	2019-04-25 18:39:17.451797+02	\N	44	1	1	1	1	3	3
106	\N	\N	2019-04-25 18:39:18.498235+02	2019-04-25 18:39:19.502755+02	\N	2019-04-25 18:39:02.942307+02	2019-04-25 18:39:19.503796+02	\N	44	1	1	1	2	3	3
111	\N	\N	2019-04-25 18:39:20.540307+02	2019-04-25 18:39:22.096194+02	\N	2019-04-25 18:39:03.047571+02	2019-04-25 18:39:22.097411+02	\N	44	1	1	1	3	3	3
116	\N	\N	2019-04-25 18:39:23.18589+02	2019-04-25 18:39:24.21602+02	\N	2019-04-25 18:39:03.131674+02	2019-04-25 18:39:24.217388+02	\N	44	1	1	1	4	3	3
121	\N	\N	2019-04-25 18:39:25.29165+02	2019-04-25 18:39:26.386572+02	\N	2019-04-25 18:39:03.214728+02	2019-04-25 18:39:26.388431+02	\N	44	1	1	1	5	3	3
102	\N	\N	2019-04-25 18:39:45.167311+02	2019-04-25 18:39:46.855448+02	\N	2019-04-25 18:39:02.870229+02	2019-04-25 18:39:46.856703+02	\N	45	1	1	1	1	3	3
107	\N	\N	2019-04-25 18:39:48.430381+02	2019-04-25 18:39:50.811184+02	\N	2019-04-25 18:39:02.966294+02	2019-04-25 18:39:50.812185+02	\N	45	1	1	1	2	3	3
112	\N	\N	2019-04-25 18:39:52.106126+02	2019-04-25 18:39:54.006249+02	\N	2019-04-25 18:39:03.064643+02	2019-04-25 18:39:54.007499+02	\N	45	1	1	1	3	3	3
117	\N	\N	2019-04-25 18:39:56.084768+02	2019-04-25 18:39:57.06448+02	\N	2019-04-25 18:39:03.149302+02	2019-04-25 18:39:57.065861+02	\N	45	1	1	1	4	3	3
122	\N	\N	2019-04-25 18:39:58.029144+02	2019-04-25 18:39:59.72793+02	\N	2019-04-25 18:39:03.231233+02	2019-04-25 18:39:59.728988+02	\N	45	1	1	1	5	3	3
103	\N	\N	2019-04-25 18:40:21.212194+02	2019-04-25 18:40:22.43625+02	\N	2019-04-25 18:39:02.887623+02	2019-04-25 18:40:22.437285+02	\N	46	1	1	1	1	3	3
108	\N	\N	2019-04-25 18:40:23.515552+02	2019-04-25 18:40:24.540897+02	\N	2019-04-25 18:39:02.99094+02	2019-04-25 18:40:24.542239+02	\N	46	1	1	1	2	3	3
113	\N	\N	2019-04-25 18:40:28.08704+02	\N	\N	2019-04-25 18:39:03.081003+02	2019-04-25 18:40:28.088396+02	\N	46	1	1	1	3	3	2
104	\N	\N	2019-04-25 18:40:51.147103+02	2019-04-25 18:40:52.598143+02	\N	2019-04-25 18:39:02.905134+02	2019-04-25 18:40:52.599398+02	\N	47	1	1	1	1	3	3
109	\N	\N	2019-04-25 18:40:53.72766+02	\N	\N	2019-04-25 18:39:03.007607+02	2019-04-25 18:40:53.728949+02	\N	47	1	1	1	2	3	2
126	\N	\N	\N	\N	\N	2019-04-25 18:43:23.428941+02	2019-04-25 18:43:23.429013+02	\N	49	\N	1	1	1	1	1
127	\N	\N	\N	\N	\N	2019-04-25 18:43:23.448807+02	2019-04-25 18:43:23.448825+02	\N	50	\N	1	1	1	1	1
128	\N	\N	\N	\N	\N	2019-04-25 18:43:23.466387+02	2019-04-25 18:43:23.466406+02	\N	51	\N	1	1	1	1	1
129	\N	\N	\N	\N	\N	2019-04-25 18:43:23.48359+02	2019-04-25 18:43:23.48364+02	\N	52	\N	1	1	1	1	1
130	\N	\N	\N	\N	\N	2019-04-25 18:43:23.499475+02	2019-04-25 18:43:23.499494+02	\N	53	\N	1	1	1	1	1
131	\N	\N	\N	\N	\N	2019-04-25 18:43:23.515044+02	2019-04-25 18:43:23.515064+02	\N	54	\N	1	1	1	1	1
132	\N	\N	\N	\N	\N	2019-04-25 18:43:23.530297+02	2019-04-25 18:43:23.530315+02	\N	55	\N	1	1	1	1	1
133	\N	\N	\N	\N	\N	2019-04-25 18:43:23.545153+02	2019-04-25 18:43:23.545172+02	\N	56	\N	1	1	1	1	1
134	\N	\N	\N	\N	\N	2019-04-25 18:43:23.560404+02	2019-04-25 18:43:23.560423+02	\N	57	\N	1	1	1	1	1
135	\N	\N	\N	\N	\N	2019-04-25 18:43:23.575525+02	2019-04-25 18:43:23.575545+02	\N	49	\N	1	1	2	1	1
136	\N	\N	\N	\N	\N	2019-04-25 18:43:23.590894+02	2019-04-25 18:43:23.590914+02	\N	50	\N	1	1	2	1	1
137	\N	\N	\N	\N	\N	2019-04-25 18:43:23.605828+02	2019-04-25 18:43:23.605862+02	\N	51	\N	1	1	2	1	1
138	\N	\N	\N	\N	\N	2019-04-25 18:43:23.627508+02	2019-04-25 18:43:23.627526+02	\N	52	\N	1	1	2	1	1
139	\N	\N	\N	\N	\N	2019-04-25 18:43:23.642143+02	2019-04-25 18:43:23.642162+02	\N	53	\N	1	1	2	1	1
140	\N	\N	\N	\N	\N	2019-04-25 18:43:23.657412+02	2019-04-25 18:43:23.657431+02	\N	54	\N	1	1	2	1	1
141	\N	\N	\N	\N	\N	2019-04-25 18:43:23.67201+02	2019-04-25 18:43:23.672028+02	\N	55	\N	1	1	2	1	1
142	\N	\N	\N	\N	\N	2019-04-25 18:43:23.686478+02	2019-04-25 18:43:23.686496+02	\N	56	\N	1	1	2	1	1
143	\N	\N	\N	\N	\N	2019-04-25 18:43:23.701172+02	2019-04-25 18:43:23.701189+02	\N	57	\N	1	1	2	1	1
144	\N	\N	\N	\N	\N	2019-04-25 18:43:23.718475+02	2019-04-25 18:43:23.718493+02	\N	49	\N	1	1	3	1	1
145	\N	\N	\N	\N	\N	2019-04-25 18:43:23.735841+02	2019-04-25 18:43:23.735859+02	\N	50	\N	1	1	3	1	1
146	\N	\N	\N	\N	\N	2019-04-25 18:43:23.753033+02	2019-04-25 18:43:23.753051+02	\N	51	\N	1	1	3	1	1
147	\N	\N	\N	\N	\N	2019-04-25 18:43:23.770539+02	2019-04-25 18:43:23.770557+02	\N	52	\N	1	1	3	1	1
148	\N	\N	\N	\N	\N	2019-04-25 18:43:23.787305+02	2019-04-25 18:43:23.787325+02	\N	53	\N	1	1	3	1	1
149	\N	\N	\N	\N	\N	2019-04-25 18:43:23.809493+02	2019-04-25 18:43:23.809523+02	\N	54	\N	1	1	3	1	1
150	\N	\N	\N	\N	\N	2019-04-25 18:43:23.838052+02	2019-04-25 18:43:23.838079+02	\N	55	\N	1	1	3	1	1
151	\N	\N	\N	\N	\N	2019-04-25 18:43:23.866611+02	2019-04-25 18:43:23.866645+02	\N	56	\N	1	1	3	1	1
152	\N	\N	\N	\N	\N	2019-04-25 18:43:23.892538+02	2019-04-25 18:43:23.892568+02	\N	57	\N	1	1	3	1	1
\.


--
-- Data for Name: dfirtrack_main_task_tag; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_task_tag (id, task_id, tag_id) FROM stdin;
\.


--
-- Name: dfirtrack_main_task_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_task_tag_id_seq', 1, false);


--
-- Name: dfirtrack_main_task_task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_task_task_id_seq', 152, true);


--
-- Data for Name: dfirtrack_main_taskname; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_taskname (taskname_id, taskname_name) FROM stdin;
1	task_1
2	task_2
3	task_3
4	task_4
5	task_5
\.


--
-- Name: dfirtrack_main_taskname_taskname_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_taskname_taskname_id_seq', 5, true);


--
-- Data for Name: dfirtrack_main_taskpriority; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_taskpriority (taskpriority_id, taskpriority_name) FROM stdin;
1	Low
2	Medium
3	High
\.


--
-- Name: dfirtrack_main_taskpriority_taskpriority_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_taskpriority_taskpriority_id_seq', 3, true);


--
-- Data for Name: dfirtrack_main_taskstatus; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.dfirtrack_main_taskstatus (taskstatus_id, taskstatus_name) FROM stdin;
1	Pending
2	Working
3	Done
\.


--
-- Name: dfirtrack_main_taskstatus_taskstatus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.dfirtrack_main_taskstatus_taskstatus_id_seq', 3, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	dfirtrack_main	tagcolor
2	dfirtrack_main	task
3	dfirtrack_main	serviceprovider
4	dfirtrack_main	entry
5	dfirtrack_main	headline
6	dfirtrack_main	analystmemo
7	dfirtrack_main	domain
8	dfirtrack_main	systemtype
9	dfirtrack_main	contact
10	dfirtrack_main	taskstatus
11	dfirtrack_main	system
12	dfirtrack_main	systemuser
13	dfirtrack_main	os
14	dfirtrack_main	osimportname
15	dfirtrack_main	reason
16	dfirtrack_main	taskpriority
17	dfirtrack_main	ip
18	dfirtrack_main	osarch
19	dfirtrack_main	tag
20	dfirtrack_main	recommendation
21	dfirtrack_main	case
22	dfirtrack_main	company
23	dfirtrack_main	location
24	dfirtrack_main	taskname
25	dfirtrack_main	reportitem
26	dfirtrack_main	division
27	dfirtrack_main	systemstatus
28	dfirtrack_main	analysisstatus
29	django_q	schedule
30	django_q	ormq
31	django_q	task
32	django_q	failure
33	django_q	success
34	admin	logentry
35	auth	group
36	auth	permission
37	auth	user
38	contenttypes	contenttype
39	sessions	session
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 39, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-04-25 18:03:41.619446+02
2	auth	0001_initial	2019-04-25 18:03:41.908101+02
3	admin	0001_initial	2019-04-25 18:03:41.970893+02
4	admin	0002_logentry_remove_auto_add	2019-04-25 18:03:41.994486+02
5	contenttypes	0002_remove_content_type_name	2019-04-25 18:03:42.018975+02
6	auth	0002_alter_permission_name_max_length	2019-04-25 18:03:42.037729+02
7	auth	0003_alter_user_email_max_length	2019-04-25 18:03:42.05158+02
8	auth	0004_alter_user_username_opts	2019-04-25 18:03:42.061549+02
9	auth	0005_alter_user_last_login_null	2019-04-25 18:03:42.074433+02
10	auth	0006_require_contenttypes_0002	2019-04-25 18:03:42.078108+02
11	auth	0007_alter_validators_add_error_messages	2019-04-25 18:03:42.106301+02
12	auth	0008_alter_user_username_max_length	2019-04-25 18:03:42.149384+02
13	auth	0009_alter_user_last_name_max_length	2019-04-25 18:03:42.180005+02
14	dfirtrack_main	0001_initial	2019-04-25 18:03:44.218891+02
15	dfirtrack_main	0002_default_values	2019-04-25 18:03:44.349545+02
16	dfirtrack_main	0003_default_tags	2019-04-25 18:03:44.364757+02
17	dfirtrack_main	0004_changed_fqdn_to_dnssuffix	2019-04-25 18:03:44.397371+02
18	dfirtrack_main	0005_added_tag_note_and_user	2019-04-25 18:03:44.471746+02
19	dfirtrack_main	0006_tagcolors	2019-04-25 18:03:44.479774+02
20	dfirtrack_main	0007_systemstatus	2019-04-25 18:03:44.48728+02
21	django_q	0001_initial	2019-04-25 18:03:44.544053+02
22	django_q	0002_auto_20150630_1624	2019-04-25 18:03:44.559363+02
23	django_q	0003_auto_20150708_1326	2019-04-25 18:03:44.614719+02
24	django_q	0004_auto_20150710_1043	2019-04-25 18:03:44.643466+02
25	django_q	0005_auto_20150718_1506	2019-04-25 18:03:44.659953+02
26	django_q	0006_auto_20150805_1817	2019-04-25 18:03:44.67326+02
27	django_q	0007_ormq	2019-04-25 18:03:44.690231+02
28	django_q	0008_auto_20160224_1026	2019-04-25 18:03:44.696585+02
29	django_q	0009_auto_20171009_0915	2019-04-25 18:03:44.744494+02
30	sessions	0001_initial	2019-04-25 18:03:44.787102+02
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 30, true);


--
-- Data for Name: django_q_ormq; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.django_q_ormq (id, key, payload, lock) FROM stdin;
\.


--
-- Name: django_q_ormq_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.django_q_ormq_id_seq', 8, true);


--
-- Data for Name: django_q_schedule; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.django_q_schedule (id, func, hook, args, kwargs, schedule_type, repeats, next_run, task, name, minutes) FROM stdin;
\.


--
-- Name: django_q_schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.django_q_schedule_id_seq', 1, false);


--
-- Data for Name: django_q_task; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.django_q_task (id, name, func, hook, args, kwargs, result, started, stopped, success, "group") FROM stdin;
afe1a34ad4c847dba4ce05c5d4f9a4a3	oregon-magnesium-oxygen-colorado	dfirtrack_main.creator.systems_creator.systems_creator_async	\N	gASVnAQAAAAAAACME2RqYW5nby5odHRwLnJlcXVlc3SUjAlRdWVyeURpY3SUk5QpgZQojA5hbmFseXNpc3N0YXR1c5SMATWUjAJvc5SMATaUjARjYXNllIwBMZSMD3NlcnZpY2Vwcm92aWRlcpSMAJSMCGxvY2F0aW9ulGgJjAdjb250YWN0lIwBM5SMDHN5c3RlbXN0YXR1c5SMATSUjBNjc3JmbWlkZGxld2FyZXRva2VulIxAWVNiWHVZS2l5NEVGNEQ3eXNicmN6WlpiVUlZMlBJM0x4dXhBWXdpUVlKdURnSDNjdVR2RXR0cWFKVkxnVnlkeZSMBmRvbWFpbpSMATKUjApzeXN0ZW1saXN0lIzuc3lzdGVtXzAwMQ0Kc3lzdGVtXzAwMg0Kc3lzdGVtXzAwMw0Kc3lzdGVtXzAwNA0Kc3lzdGVtXzAwNQ0Kc3lzdGVtXzAwNg0Kc3lzdGVtXzAwNw0Kc3lzdGVtXzAwOA0Kc3lzdGVtXzAwOQ0Kc3lzdGVtXzAxMA0Kc3lzdGVtXzAxMQ0Kc3lzdGVtXzAxMg0Kc3lzdGVtXzAxMw0Kc3lzdGVtXzAxNA0Kc3lzdGVtXzAxNQ0Kc3lzdGVtXzAxNg0Kc3lzdGVtXzAxNw0Kc3lzdGVtXzAxOA0Kc3lzdGVtXzAxOQ0Kc3lzdGVtXzAyMJSMA3RhZ5RoFIwGb3NhcmNolGgUjApzeXN0ZW10eXBllGgHjAZyZWFzb26UaAmMB2NvbXBhbnmUaAl1fZQojAlfZW5jb2RpbmeUjAV1dGYtOJSMBV9kYXRhlH2UKGgEXZRoBWFoBl2UaAdhaAhdlGgJYWgKXZRoC2FoDF2UaAlhaA1dlGgOYWgPXZRoEGFoEV2UaBJhaBNdlGgUYWgVXZRoFmFoF12UaBRhaBtdlGgJYWgYXZRoFGFoGV2UaAdhaBpdlGgJYXWMCF9tdXRhYmxllIh1YowVZGphbmdvLmRiLm1vZGVscy5iYXNllIwObW9kZWxfdW5waWNrbGWUk5SMBGF1dGiUjARVc2VylIaUhZRSlH2UKIwFZW1haWyUaAuMCWxhc3RfbmFtZZRoC4wKZmlyc3RfbmFtZZRoC4wMaXNfc3VwZXJ1c2VylIiMCHBhc3N3b3JklIxOcGJrZGYyX3NoYTI1NiQxMDAwMDAkTmgxYjlFVzhQNElrJGNFTHNYcjFyNVpsRkx1MnBJUzlYQTlnQm5NV3FDZTFTUGNWb0ZsR2Y4L009lIwKbGFzdF9sb2dpbpSMCGRhdGV0aW1llIwIZGF0ZXRpbWWUk5RDCgfjBBkQBR8D9CCUjARweXR6lIwEX1VUQ5STlClSlIaUUpSMCHVzZXJuYW1llIwJZm9yZW5zaWNzlIwLZGF0ZV9qb2luZWSUaENDCgfjBBkQBQwOJyuUaEiGlFKUjAJpZJRLAYwIaXNfc3RhZmaUiIwPX2RqYW5nb192ZXJzaW9ulIwDMi4wlIwGX3N0YXRllGgxjApNb2RlbFN0YXRllJOUKYGUfZQojAZhZGRpbmeUiYwCZGKUjAdkZWZhdWx0lHVijAlpc19hY3RpdmWUiHVihpQu	gASVAwAAAAAAAAB9lC4=	\N	2019-04-25 18:25:57.231084+02	2019-04-25 18:26:08.807432+02	t	\N
de056f82b1b84db6b7f6694a8148cbd3	early-west-illinois-speaker	dfirtrack_main.creator.systems_creator.systems_creator_async	\N	gASVxQMAAAAAAACME2RqYW5nby5odHRwLnJlcXVlc3SUjAlRdWVyeURpY3SUk5QpgZQojA5hbmFseXNpc3N0YXR1c5SMATWUjAJvc5SMATSUjARjYXNllIwBMZSMD3NlcnZpY2Vwcm92aWRlcpSMAJSMCGxvY2F0aW9ulGgJjAdjb250YWN0lIwBM5SMDHN5c3RlbXN0YXR1c5RoB4wTY3NyZm1pZGRsZXdhcmV0b2tlbpSMQEloTG55MjRMQlVHWm9nY2hZejdpOVh2eUZVaE9UUjI5aFQ3MDJBQ2oxendYQWs4VjBoYkszcld4dTc0MlpIY1eUjAZkb21haW6UjAEylIwKc3lzdGVtbGlzdJSMFmRjXzAwMQ0KZGNfMDAyDQpkY18wMDOUjAN0YWeUaA6MBm9zYXJjaJRoE4wKc3lzdGVtdHlwZZRoCYwGcmVhc29ulGgJjAdjb21wYW55lGgJdX2UKIwJX2VuY29kaW5nlIwFdXRmLTiUjAVfZGF0YZR9lChoBF2UaAVhaAZdlGgHYWgIXZRoCWFoCl2UaAthaAxdlGgJYWgNXZRoDmFoD12UaAdhaBBdlGgRYWgSXZRoE2FoFF2UaBVhaBZdlChoE2gOZWgaXZRoCWFoF12UaBNhaBhdlGgJYWgZXZRoCWF1jAhfbXV0YWJsZZSIdWKMFWRqYW5nby5kYi5tb2RlbHMuYmFzZZSMDm1vZGVsX3VucGlja2xllJOUjARhdXRolIwEVXNlcpSGlIWUUpR9lCiMBWVtYWlslGgLjAlsYXN0X25hbWWUaAuMCmZpcnN0X25hbWWUaAuMDGlzX3N1cGVydXNlcpSIjAh1c2VybmFtZZSMCWZvcmVuc2ljc5SMCmxhc3RfbG9naW6UjAhkYXRldGltZZSMCGRhdGV0aW1llJOUQwoH4wQZEAUfA/QglIwEcHl0epSMBF9VVEOUk5QpUpSGlFKUjAhwYXNzd29yZJSMTnBia2RmMl9zaGEyNTYkMTAwMDAwJE5oMWI5RVc4UDRJayRjRUxzWHIxcjVabEZMdTJwSVM5WEE5Z0JuTVdxQ2UxU1BjVm9GbEdmOC9NPZSMC2RhdGVfam9pbmVklGhCQwoH4wQZEAUMDicrlGhHhpRSlIwCaWSUSwGMCGlzX3N0YWZmlIiMD19kamFuZ29fdmVyc2lvbpSMAzIuMJSMBl9zdGF0ZZRoMIwKTW9kZWxTdGF0ZZSTlCmBlH2UKIwGYWRkaW5nlImMAmRilIwHZGVmYXVsdJR1YowJaXNfYWN0aXZllIh1YoaULg==	gASVAwAAAAAAAAB9lC4=	\N	2019-04-25 18:27:56.962981+02	2019-04-25 18:27:57.217805+02	t	\N
d65e0f8edd3b4cbca0c4a76c93a5cd4d	arkansas-black-pip-queen	dfirtrack_main.creator.systems_creator.systems_creator_async	\N	gASVeQQAAAAAAACME2RqYW5nby5odHRwLnJlcXVlc3SUjAlRdWVyeURpY3SUk5QpgZQojA5hbmFseXNpc3N0YXR1c5SMATGUjAJvc5SMATSUjA9zZXJ2aWNlcHJvdmlkZXKUaAWMDHN5c3RlbXN0YXR1c5SMATKUjAdjb250YWN0lIwBM5SMCGxvY2F0aW9ulGgFjBNjc3JmbWlkZGxld2FyZXRva2VulIxAMlJJbDg1eGUyczdxYldpN2Y2OVhKT2U5NXlGUzZDaDRCdDRZQ0Q1TXM3WG9uMGVMaE9kcERpRjhVTHM2Y3NyUpSMBmRvbWFpbpRoCowKc3lzdGVtbGlzdJSM7nN5c3RlbV8wMjENCnN5c3RlbV8wMjINCnN5c3RlbV8wMjMNCnN5c3RlbV8wMjQNCnN5c3RlbV8wMjUNCnN5c3RlbV8wMjYNCnN5c3RlbV8wMjcNCnN5c3RlbV8wMjgNCnN5c3RlbV8wMjkNCnN5c3RlbV8wMzANCnN5c3RlbV8wMzENCnN5c3RlbV8wMzINCnN5c3RlbV8wMzMNCnN5c3RlbV8wMzQNCnN5c3RlbV8wMzUNCnN5c3RlbV8wMzYNCnN5c3RlbV8wMzcNCnN5c3RlbV8wMzgNCnN5c3RlbV8wMzkNCnN5c3RlbV8wNDCUjAdjb21wYW55lGgFjAZvc2FyY2iUjACUjApzeXN0ZW10eXBllGgVjAZyZWFzb26UaAx1fZQojAlfZW5jb2RpbmeUjAV1dGYtOJSMBV9kYXRhlH2UKGgEXZRoBWFoBl2UaAdhaAhdlGgFYWgJXZRoCmFoC12UaAxhaA1dlGgFYWgOXZRoD2FoEF2UaAphaBFdlGgSYWgTXZRoBWFoFF2UaBVhaBZdlGgVYWgXXZRoDGF1jAhfbXV0YWJsZZSIdWKMFWRqYW5nby5kYi5tb2RlbHMuYmFzZZSMDm1vZGVsX3VucGlja2xllJOUjARhdXRolIwEVXNlcpSGlIWUUpR9lCiMBWVtYWlslGgVjAlsYXN0X25hbWWUaBWMCmZpcnN0X25hbWWUaBWMDGlzX3N1cGVydXNlcpSIjAh1c2VybmFtZZSMCWZvcmVuc2ljc5SMCmxhc3RfbG9naW6UjAhkYXRldGltZZSMCGRhdGV0aW1llJOUQwoH4wQZEAUfA/QglIwEcHl0epSMBF9VVEOUk5QpUpSGlFKUjAhwYXNzd29yZJSMTnBia2RmMl9zaGEyNTYkMTAwMDAwJE5oMWI5RVc4UDRJayRjRUxzWHIxcjVabEZMdTJwSVM5WEE5Z0JuTVdxQ2UxU1BjVm9GbEdmOC9NPZSMC2RhdGVfam9pbmVklGg9QwoH4wQZEAUMDicrlGhChpRSlIwCaWSUSwGMCGlzX3N0YWZmlIiMD19kamFuZ29fdmVyc2lvbpSMAzIuMJSMBl9zdGF0ZZRoK4wKTW9kZWxTdGF0ZZSTlCmBlH2UKIwGYWRkaW5nlImMAmRilIwHZGVmYXVsdJR1YowJaXNfYWN0aXZllIh1YoaULg==	gASVAwAAAAAAAAB9lC4=	\N	2019-04-25 18:29:24.036779+02	2019-04-25 18:29:24.88904+02	t	\N
7912a5a2e9df48dca0bd8b629a5ae49d	juliet-ohio-white-river	dfirtrack_main.creator.tasks_creator.tasks_creator_async	\N	gASVeQMAAAAAAACME2RqYW5nby5odHRwLnJlcXVlc3SUjAlRdWVyeURpY3SUk5QpgZQojAx0YXNrcHJpb3JpdHmUjAEylIwTY3NyZm1pZGRsZXdhcmV0b2tlbpSMQDRHbklkM0t5Y1IwNzU5S2FVQ0hxbkpaSnR0U1cxV05rRGlKbEhCaTZDd1E1aGRHT1drTFNoZHFJaUdGYTdNWDeUjAh0YXNrbmFtZZSMATWUjBh0YXNrX2Fzc2lnbmVkX3RvX3VzZXJfaWSUjACUjAp0YXNrc3RhdHVzlIwBMZSMBnN5c3RlbZSMAjQzlHV9lCiMCV9lbmNvZGluZ5SMBXV0Zi04lIwFX2RhdGGUfZQoaARdlGgFYWgGXZRoB2FoCF2UKGgNaAWMATOUjAE0lGgJZWgKXZRoC2FoDF2UaA1haA5dlCiMAjI0lIwCMjWUjAIyNpSMAjI3lIwCMjiUjAIyOZSMAjMwlIwCMzGUjAIzMpSMAjMzlIwCMzSUjAIzNZSMAjM2lIwCMzeUjAIzOJSMAjM5lIwCNDCUjAI0MZSMAjQylGgPZXWMCF9tdXRhYmxllIh1YowVZGphbmdvLmRiLm1vZGVscy5iYXNllIwObW9kZWxfdW5waWNrbGWUk5SMBGF1dGiUjARVc2VylIaUhZRSlH2UKIwFZW1haWyUaAuMCWxhc3RfbmFtZZRoC4wKZmlyc3RfbmFtZZRoC4wMaXNfc3VwZXJ1c2VylIiMCHVzZXJuYW1llIwJZm9yZW5zaWNzlIwKbGFzdF9sb2dpbpSMCGRhdGV0aW1llIwIZGF0ZXRpbWWUk5RDCgfjBBkQBR8D9CCUjARweXR6lIwEX1VUQ5STlClSlIaUUpSMCHBhc3N3b3JklIxOcGJrZGYyX3NoYTI1NiQxMDAwMDAkTmgxYjlFVzhQNElrJGNFTHNYcjFyNVpsRkx1MnBJUzlYQTlnQm5NV3FDZTFTUGNWb0ZsR2Y4L009lIwLZGF0ZV9qb2luZWSUaENDCgfjBBkQBQwOJyuUaEiGlFKUjAJpZJRLAYwIaXNfc3RhZmaUiIwPX2RqYW5nb192ZXJzaW9ulIwDMi4wlIwGX3N0YXRllGgxjApNb2RlbFN0YXRllJOUKYGUfZQojAZhZGRpbmeUiYwCZGKUjAdkZWZhdWx0lHVijAlpc19hY3RpdmWUiHVihpQu	gASVAwAAAAAAAAB9lC4=	\N	2019-04-25 18:30:23.180212+02	2019-04-25 18:30:25.109957+02	t	\N
e60ce18d2099495490105e6b77093577	massachusetts-one-quebec-eighteen	dfirtrack_main.creator.systems_creator.systems_creator_async	\N	gASVsQMAAAAAAACME2RqYW5nby5odHRwLnJlcXVlc3SUjAlRdWVyeURpY3SUk5QpgZQojA5hbmFseXNpc3N0YXR1c5SMATGUjAJvc5SMATeUjA9zZXJ2aWNlcHJvdmlkZXKUjAEylIwMc3lzdGVtc3RhdHVzlGgJjAdjb250YWN0lGgFjAhsb2NhdGlvbpSMATOUjBNjc3JmbWlkZGxld2FyZXRva2VulIxAQ2hhek4yV0JRVlF2WnJGTVRlUHd4ZkRGMzZoZ0tTRlhiVHdjaEF1OWdBR3RidkJxVldUWXJKNEVTajR1UUlQS5SMBmRvbWFpbpRoBYwKc3lzdGVtbGlzdJSMJmFzeXNfMQ0KYXN5c18yDQphc3lzXzMNCmFzeXNfNA0KYXN5c181lIwHY29tcGFueZRoDYwGb3NhcmNolIwAlIwKc3lzdGVtdHlwZZRoFYwGcmVhc29ulGgJdX2UKIwJX2VuY29kaW5nlIwFdXRmLTiUjAVfZGF0YZR9lChoBF2UaAVhaAZdlGgHYWgIXZRoCWFoCl2UaAlhaAtdlGgFYWgMXZRoDWFoDl2UaA9haBBdlGgFYWgRXZRoEmFoE12UaA1haBRdlGgVYWgWXZRoFWFoF12UaAlhdYwIX211dGFibGWUiHVijBVkamFuZ28uZGIubW9kZWxzLmJhc2WUjA5tb2RlbF91bnBpY2tsZZSTlIwEYXV0aJSMBFVzZXKUhpSFlFKUfZQojAVlbWFpbJRoFYwJbGFzdF9uYW1llGgVjApmaXJzdF9uYW1llGgVjAxpc19zdXBlcnVzZXKUiIwIdXNlcm5hbWWUjAlmb3JlbnNpY3OUjApsYXN0X2xvZ2lulIwIZGF0ZXRpbWWUjAhkYXRldGltZZSTlEMKB+MEGRAFHwP0IJSMBHB5dHqUjARfVVRDlJOUKVKUhpRSlIwIcGFzc3dvcmSUjE5wYmtkZjJfc2hhMjU2JDEwMDAwMCROaDFiOUVXOFA0SWskY0VMc1hyMXI1WmxGTHUycElTOVhBOWdCbk1XcUNlMVNQY1ZvRmxHZjgvTT2UjAtkYXRlX2pvaW5lZJRoPUMKB+MEGRAFDA4nK5RoQoaUUpSMAmlklEsBjAhpc19zdGFmZpSIjA9fZGphbmdvX3ZlcnNpb26UjAMyLjCUjAZfc3RhdGWUaCuMCk1vZGVsU3RhdGWUk5QpgZR9lCiMBmFkZGluZ5SJjAJkYpSMB2RlZmF1bHSUdWKMCWlzX2FjdGl2ZZSIdWKGlC4=	gASVAwAAAAAAAAB9lC4=	\N	2019-04-25 18:38:31.210648+02	2019-04-25 18:38:31.435605+02	t	\N
e8ec8051cef545a1a54c5e3db5f3cc0b	stream-three-mike-maine	dfirtrack_main.creator.tasks_creator.tasks_creator_async	\N	gASVLgMAAAAAAACME2RqYW5nby5odHRwLnJlcXVlc3SUjAlRdWVyeURpY3SUk5QpgZQojAx0YXNrcHJpb3JpdHmUjAEzlIwTY3NyZm1pZGRsZXdhcmV0b2tlbpSMQGRGSndYQlRaWUs1M00yZmxzeHhsbVU0WVU4NjdVd2FUTWg1OXI5cnhvcFYxWTZiWnVmQk5nb3ZYSmxUbDBta0eUjAh0YXNrbmFtZZSMATWUjBh0YXNrX2Fzc2lnbmVkX3RvX3VzZXJfaWSUjAExlIwKdGFza3N0YXR1c5RoC4wGc3lzdGVtlIwCNDiUdX2UKIwJX2VuY29kaW5nlIwFdXRmLTiUjAVfZGF0YZR9lChoBF2UaAVhaAZdlGgHYWgIXZQoaAuMATKUaAWMATSUaAllaApdlGgLYWgMXZRoC2FoDV2UKIwCNDSUjAI0NZSMAjQ2lIwCNDeUaA5ldYwIX211dGFibGWUiHVijBVkamFuZ28uZGIubW9kZWxzLmJhc2WUjA5tb2RlbF91bnBpY2tsZZSTlIwEYXV0aJSMBFVzZXKUhpSFlFKUfZQojAVlbWFpbJSMAJSMCWxhc3RfbmFtZZRoK4wKZmlyc3RfbmFtZZRoK4wMaXNfc3VwZXJ1c2VylIiMCHVzZXJuYW1llIwJZm9yZW5zaWNzlIwKbGFzdF9sb2dpbpSMCGRhdGV0aW1llIwIZGF0ZXRpbWWUk5RDCgfjBBkQBR8D9CCUjARweXR6lIwEX1VUQ5STlClSlIaUUpSMCHBhc3N3b3JklIxOcGJrZGYyX3NoYTI1NiQxMDAwMDAkTmgxYjlFVzhQNElrJGNFTHNYcjFyNVpsRkx1MnBJUzlYQTlnQm5NV3FDZTFTUGNWb0ZsR2Y4L009lIwLZGF0ZV9qb2luZWSUaDRDCgfjBBkQBQwOJyuUaDmGlFKUjAJpZJRLAYwIaXNfc3RhZmaUiIwPX2RqYW5nb192ZXJzaW9ulIwDMi4wlIwGX3N0YXRllGghjApNb2RlbFN0YXRllJOUKYGUfZQojAZhZGRpbmeUiYwCZGKUjAdkZWZhdWx0lHVijAlpc19hY3RpdmWUiHVihpQu	gASVAwAAAAAAAAB9lC4=	\N	2019-04-25 18:39:02.735876+02	2019-04-25 18:39:03.298114+02	t	\N
a15de8b2999d48ca917431bd3387aea9	oranges-massachusetts-jersey-princess	dfirtrack_main.creator.systems_creator.systems_creator_async	\N	gASV1AMAAAAAAACME2RqYW5nby5odHRwLnJlcXVlc3SUjAlRdWVyeURpY3SUk5QpgZQojA5hbmFseXNpc3N0YXR1c5SMATGUjAJvc5SMATSUjA9zZXJ2aWNlcHJvdmlkZXKUjAEylIwMc3lzdGVtc3RhdHVzlGgJjAdjb250YWN0lGgJjAhsb2NhdGlvbpRoB4wTY3NyZm1pZGRsZXdhcmV0b2tlbpSMQEJFeUN0R1dhclZETER1MW5XS0xNS0VZYWdndTExUVVCYWdVZlhldUlSQXRKUHlYMVlzUGVFOHA5NXRoZjdHNG+UjAZkb21haW6UaAWMCnN5c3RlbWxpc3SUjEZ6c3lzXzENCnpzeXNfMg0KenN5c18zDQp6c3lzXzQNCnpzeXNfNQ0KenN5c182DQp6c3lzXzcNCnpzeXNfOA0KenN5c185lIwHY29tcGFueZSMATOUjAZvc2FyY2iUjACUjApzeXN0ZW10eXBllGgVjAZyZWFzb26UaAV1fZQojAlfZW5jb2RpbmeUjAV1dGYtOJSMBV9kYXRhlH2UKGgEXZRoBWFoBl2UaAdhaAhdlGgJYWgKXZRoCWFoC12UaAlhaAxdlGgHYWgNXZRoDmFoD12UaAVhaBBdlGgRYWgSXZQoaAloE2VoFF2UaBVhaBZdlGgVYWgXXZRoBWF1jAhfbXV0YWJsZZSIdWKMFWRqYW5nby5kYi5tb2RlbHMuYmFzZZSMDm1vZGVsX3VucGlja2xllJOUjARhdXRolIwEVXNlcpSGlIWUUpR9lCiMBWVtYWlslGgVjAlsYXN0X25hbWWUaBWMCmZpcnN0X25hbWWUaBWMDGlzX3N1cGVydXNlcpSIjAh1c2VybmFtZZSMCWZvcmVuc2ljc5SMCmxhc3RfbG9naW6UjAhkYXRldGltZZSMCGRhdGV0aW1llJOUQwoH4wQZEAUfA/QglIwEcHl0epSMBF9VVEOUk5QpUpSGlFKUjAhwYXNzd29yZJSMTnBia2RmMl9zaGEyNTYkMTAwMDAwJE5oMWI5RVc4UDRJayRjRUxzWHIxcjVabEZMdTJwSVM5WEE5Z0JuTVdxQ2UxU1BjVm9GbEdmOC9NPZSMC2RhdGVfam9pbmVklGg9QwoH4wQZEAUMDicrlGhChpRSlIwCaWSUSwGMCGlzX3N0YWZmlIiMD19kamFuZ29fdmVyc2lvbpSMAzIuMJSMBl9zdGF0ZZRoK4wKTW9kZWxTdGF0ZZSTlCmBlH2UKIwGYWRkaW5nlImMAmRilIwHZGVmYXVsdJR1YowJaXNfYWN0aXZllIh1YoaULg==	gASVAwAAAAAAAAB9lC4=	\N	2019-04-25 18:42:50.33062+02	2019-04-25 18:42:50.80151+02	t	\N
53e590fb38364f74bf1358dfe02725a8	texas-double-comet-florida	dfirtrack_main.creator.tasks_creator.tasks_creator_async	\N	gASVOgMAAAAAAACME2RqYW5nby5odHRwLnJlcXVlc3SUjAlRdWVyeURpY3SUk5QpgZQojAx0YXNrcHJpb3JpdHmUjAExlIwTY3NyZm1pZGRsZXdhcmV0b2tlbpSMQElGMjhGY1NwaFhNRGNhMmZScjhJMkw4MXdIR1I0YmxUaGhvTDlLcVhIQ0NCb2VZVFQ5Y2FXZnowbFV0NWExdkeUjAh0YXNrbmFtZZSMATOUjBh0YXNrX2Fzc2lnbmVkX3RvX3VzZXJfaWSUjACUjAp0YXNrc3RhdHVzlGgFjAZzeXN0ZW2UjAI1N5R1fZQojAlfZW5jb2RpbmeUjAV1dGYtOJSMBV9kYXRhlH2UKGgEXZRoBWFoBl2UaAdhaAhdlChoBYwBMpRoCWVoCl2UaAthaAxdlGgFYWgNXZQojAI0OZSMAjUwlIwCNTGUjAI1MpSMAjUzlIwCNTSUjAI1NZSMAjU2lGgOZXWMCF9tdXRhYmxllIh1YowVZGphbmdvLmRiLm1vZGVscy5iYXNllIwObW9kZWxfdW5waWNrbGWUk5SMBGF1dGiUjARVc2VylIaUhZRSlH2UKIwFZW1haWyUaAuMCWxhc3RfbmFtZZRoC4wKZmlyc3RfbmFtZZRoC4wMaXNfc3VwZXJ1c2VylIiMCHVzZXJuYW1llIwJZm9yZW5zaWNzlIwKbGFzdF9sb2dpbpSMCGRhdGV0aW1llIwIZGF0ZXRpbWWUk5RDCgfjBBkQBR8D9CCUjARweXR6lIwEX1VUQ5STlClSlIaUUpSMCHBhc3N3b3JklIxOcGJrZGYyX3NoYTI1NiQxMDAwMDAkTmgxYjlFVzhQNElrJGNFTHNYcjFyNVpsRkx1MnBJUzlYQTlnQm5NV3FDZTFTUGNWb0ZsR2Y4L009lIwLZGF0ZV9qb2luZWSUaDZDCgfjBBkQBQwOJyuUaDuGlFKUjAJpZJRLAYwIaXNfc3RhZmaUiIwPX2RqYW5nb192ZXJzaW9ulIwDMi4wlIwGX3N0YXRllGgkjApNb2RlbFN0YXRllJOUKYGUfZQojAZhZGRpbmeUiYwCZGKUjAdkZWZhdWx0lHVijAlpc19hY3RpdmWUiHVihpQu	gASVAwAAAAAAAAB9lC4=	\N	2019-04-25 18:43:23.188482+02	2019-04-25 18:43:23.900261+02	t	\N
\.


--
-- Name: django_q_task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dfirtrack
--

SELECT pg_catalog.setval('public.django_q_task_id_seq', 1, false);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: dfirtrack
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
dhbpab17368xqgy8i5emffmwidxund1q	NDE2MWM5ZDUyNmQyMjNhM2Q4MGM4NmZkNmEzOGI5ZGJkYjIyNzU4Mjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMzhjMWU1MTgwMDFjYWQxYjE2ODZlN2YzM2Y4ZTlhZGQ1ZDU5MWFmZSIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2019-05-09 18:05:31.262882+02
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: dfirtrack_main_analysisstatus_analysisstatus_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_analysisstatus
    ADD CONSTRAINT dfirtrack_main_analysisstatus_analysisstatus_name_key UNIQUE (analysisstatus_name);


--
-- Name: dfirtrack_main_analysisstatus_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_analysisstatus
    ADD CONSTRAINT dfirtrack_main_analysisstatus_pkey PRIMARY KEY (analysisstatus_id);


--
-- Name: dfirtrack_main_analystmemo_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_analystmemo
    ADD CONSTRAINT dfirtrack_main_analystmemo_pkey PRIMARY KEY (analystmemo_id);


--
-- Name: dfirtrack_main_case_case_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_case
    ADD CONSTRAINT dfirtrack_main_case_case_name_key UNIQUE (case_name);


--
-- Name: dfirtrack_main_case_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_case
    ADD CONSTRAINT dfirtrack_main_case_pkey PRIMARY KEY (case_id);


--
-- Name: dfirtrack_main_company_company_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_company
    ADD CONSTRAINT dfirtrack_main_company_company_name_key UNIQUE (company_name);


--
-- Name: dfirtrack_main_company_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_company
    ADD CONSTRAINT dfirtrack_main_company_pkey PRIMARY KEY (company_id);


--
-- Name: dfirtrack_main_contact_contact_email_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_contact
    ADD CONSTRAINT dfirtrack_main_contact_contact_email_key UNIQUE (contact_email);


--
-- Name: dfirtrack_main_contact_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_contact
    ADD CONSTRAINT dfirtrack_main_contact_pkey PRIMARY KEY (contact_id);


--
-- Name: dfirtrack_main_division_division_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_division
    ADD CONSTRAINT dfirtrack_main_division_division_name_key UNIQUE (division_name);


--
-- Name: dfirtrack_main_division_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_division
    ADD CONSTRAINT dfirtrack_main_division_pkey PRIMARY KEY (division_id);


--
-- Name: dfirtrack_main_domain_domain_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_domain
    ADD CONSTRAINT dfirtrack_main_domain_domain_name_key UNIQUE (domain_name);


--
-- Name: dfirtrack_main_domain_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_domain
    ADD CONSTRAINT dfirtrack_main_domain_pkey PRIMARY KEY (domain_id);


--
-- Name: dfirtrack_main_entry_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_entry
    ADD CONSTRAINT dfirtrack_main_entry_pkey PRIMARY KEY (entry_id);


--
-- Name: dfirtrack_main_entry_system_id_entry_sha1_d46e6424_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_entry
    ADD CONSTRAINT dfirtrack_main_entry_system_id_entry_sha1_d46e6424_uniq UNIQUE (system_id, entry_sha1);


--
-- Name: dfirtrack_main_headline_headline_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_headline
    ADD CONSTRAINT dfirtrack_main_headline_headline_name_key UNIQUE (headline_name);


--
-- Name: dfirtrack_main_headline_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_headline
    ADD CONSTRAINT dfirtrack_main_headline_pkey PRIMARY KEY (headline_id);


--
-- Name: dfirtrack_main_ip_ip_ip_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_ip
    ADD CONSTRAINT dfirtrack_main_ip_ip_ip_key UNIQUE (ip_ip);


--
-- Name: dfirtrack_main_ip_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_ip
    ADD CONSTRAINT dfirtrack_main_ip_pkey PRIMARY KEY (ip_id);


--
-- Name: dfirtrack_main_location_location_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_location
    ADD CONSTRAINT dfirtrack_main_location_location_name_key UNIQUE (location_name);


--
-- Name: dfirtrack_main_location_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_location
    ADD CONSTRAINT dfirtrack_main_location_pkey PRIMARY KEY (location_id);


--
-- Name: dfirtrack_main_os_os_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_os
    ADD CONSTRAINT dfirtrack_main_os_os_name_key UNIQUE (os_name);


--
-- Name: dfirtrack_main_os_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_os
    ADD CONSTRAINT dfirtrack_main_os_pkey PRIMARY KEY (os_id);


--
-- Name: dfirtrack_main_osarch_osarch_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_osarch
    ADD CONSTRAINT dfirtrack_main_osarch_osarch_name_key UNIQUE (osarch_name);


--
-- Name: dfirtrack_main_osarch_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_osarch
    ADD CONSTRAINT dfirtrack_main_osarch_pkey PRIMARY KEY (osarch_id);


--
-- Name: dfirtrack_main_osimportname_osimportname_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_osimportname
    ADD CONSTRAINT dfirtrack_main_osimportname_osimportname_name_key UNIQUE (osimportname_name);


--
-- Name: dfirtrack_main_osimportname_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_osimportname
    ADD CONSTRAINT dfirtrack_main_osimportname_pkey PRIMARY KEY (osimportname_id);


--
-- Name: dfirtrack_main_reason_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reason
    ADD CONSTRAINT dfirtrack_main_reason_pkey PRIMARY KEY (reason_id);


--
-- Name: dfirtrack_main_reason_reason_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reason
    ADD CONSTRAINT dfirtrack_main_reason_reason_name_key UNIQUE (reason_name);


--
-- Name: dfirtrack_main_recommendation_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_recommendation
    ADD CONSTRAINT dfirtrack_main_recommendation_pkey PRIMARY KEY (recommendation_id);


--
-- Name: dfirtrack_main_recommendation_recommendation_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_recommendation
    ADD CONSTRAINT dfirtrack_main_recommendation_recommendation_name_key UNIQUE (recommendation_name);


--
-- Name: dfirtrack_main_reportite_system_id_headline_id_re_5173a021_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reportitem
    ADD CONSTRAINT dfirtrack_main_reportite_system_id_headline_id_re_5173a021_uniq UNIQUE (system_id, headline_id, reportitem_subheadline);


--
-- Name: dfirtrack_main_reportitem_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reportitem
    ADD CONSTRAINT dfirtrack_main_reportitem_pkey PRIMARY KEY (reportitem_id);


--
-- Name: dfirtrack_main_serviceprovider_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_serviceprovider
    ADD CONSTRAINT dfirtrack_main_serviceprovider_pkey PRIMARY KEY (serviceprovider_id);


--
-- Name: dfirtrack_main_serviceprovider_serviceprovider_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_serviceprovider
    ADD CONSTRAINT dfirtrack_main_serviceprovider_serviceprovider_name_key UNIQUE (serviceprovider_name);


--
-- Name: dfirtrack_main_system_case_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_case
    ADD CONSTRAINT dfirtrack_main_system_case_pkey PRIMARY KEY (id);


--
-- Name: dfirtrack_main_system_case_system_id_case_id_db4864aa_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_case
    ADD CONSTRAINT dfirtrack_main_system_case_system_id_case_id_db4864aa_uniq UNIQUE (system_id, case_id);


--
-- Name: dfirtrack_main_system_co_system_id_company_id_74d4acdf_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_company
    ADD CONSTRAINT dfirtrack_main_system_co_system_id_company_id_74d4acdf_uniq UNIQUE (system_id, company_id);


--
-- Name: dfirtrack_main_system_company_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_company
    ADD CONSTRAINT dfirtrack_main_system_company_pkey PRIMARY KEY (id);


--
-- Name: dfirtrack_main_system_ip_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_ip
    ADD CONSTRAINT dfirtrack_main_system_ip_pkey PRIMARY KEY (id);


--
-- Name: dfirtrack_main_system_ip_system_id_ip_id_56cb1e5e_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_ip
    ADD CONSTRAINT dfirtrack_main_system_ip_system_id_ip_id_56cb1e5e_uniq UNIQUE (system_id, ip_id);


--
-- Name: dfirtrack_main_system_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_system_pkey PRIMARY KEY (system_id);


--
-- Name: dfirtrack_main_system_system_name_domain_id_sy_23c9c3ca_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_system_system_name_domain_id_sy_23c9c3ca_uniq UNIQUE (system_name, domain_id, system_install_time);


--
-- Name: dfirtrack_main_system_system_uuid_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_system_system_uuid_key UNIQUE (system_uuid);


--
-- Name: dfirtrack_main_system_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_tag
    ADD CONSTRAINT dfirtrack_main_system_tag_pkey PRIMARY KEY (id);


--
-- Name: dfirtrack_main_system_tag_system_id_tag_id_fbc1ca5e_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_tag
    ADD CONSTRAINT dfirtrack_main_system_tag_system_id_tag_id_fbc1ca5e_uniq UNIQUE (system_id, tag_id);


--
-- Name: dfirtrack_main_systemstatus_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemstatus
    ADD CONSTRAINT dfirtrack_main_systemstatus_pkey PRIMARY KEY (systemstatus_id);


--
-- Name: dfirtrack_main_systemstatus_systemstatus_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemstatus
    ADD CONSTRAINT dfirtrack_main_systemstatus_systemstatus_name_key UNIQUE (systemstatus_name);


--
-- Name: dfirtrack_main_systemtype_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemtype
    ADD CONSTRAINT dfirtrack_main_systemtype_pkey PRIMARY KEY (systemtype_id);


--
-- Name: dfirtrack_main_systemtype_systemtype_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemtype
    ADD CONSTRAINT dfirtrack_main_systemtype_systemtype_name_key UNIQUE (systemtype_name);


--
-- Name: dfirtrack_main_systemuse_system_id_systemuser_nam_2950d466_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemuser
    ADD CONSTRAINT dfirtrack_main_systemuse_system_id_systemuser_nam_2950d466_uniq UNIQUE (system_id, systemuser_name);


--
-- Name: dfirtrack_main_systemuser_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemuser
    ADD CONSTRAINT dfirtrack_main_systemuser_pkey PRIMARY KEY (systemuser_id);


--
-- Name: dfirtrack_main_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_tag
    ADD CONSTRAINT dfirtrack_main_tag_pkey PRIMARY KEY (tag_id);


--
-- Name: dfirtrack_main_tag_tag_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_tag
    ADD CONSTRAINT dfirtrack_main_tag_tag_name_key UNIQUE (tag_name);


--
-- Name: dfirtrack_main_tagcolor_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_tagcolor
    ADD CONSTRAINT dfirtrack_main_tagcolor_pkey PRIMARY KEY (tagcolor_id);


--
-- Name: dfirtrack_main_tagcolor_tagcolor_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_tagcolor
    ADD CONSTRAINT dfirtrack_main_tagcolor_tagcolor_name_key UNIQUE (tagcolor_name);


--
-- Name: dfirtrack_main_task_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_pkey PRIMARY KEY (task_id);


--
-- Name: dfirtrack_main_task_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task_tag
    ADD CONSTRAINT dfirtrack_main_task_tag_pkey PRIMARY KEY (id);


--
-- Name: dfirtrack_main_task_tag_task_id_tag_id_eacebfbc_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task_tag
    ADD CONSTRAINT dfirtrack_main_task_tag_task_id_tag_id_eacebfbc_uniq UNIQUE (task_id, tag_id);


--
-- Name: dfirtrack_main_taskname_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskname
    ADD CONSTRAINT dfirtrack_main_taskname_pkey PRIMARY KEY (taskname_id);


--
-- Name: dfirtrack_main_taskname_taskname_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskname
    ADD CONSTRAINT dfirtrack_main_taskname_taskname_name_key UNIQUE (taskname_name);


--
-- Name: dfirtrack_main_taskpriority_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskpriority
    ADD CONSTRAINT dfirtrack_main_taskpriority_pkey PRIMARY KEY (taskpriority_id);


--
-- Name: dfirtrack_main_taskpriority_taskpriority_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskpriority
    ADD CONSTRAINT dfirtrack_main_taskpriority_taskpriority_name_key UNIQUE (taskpriority_name);


--
-- Name: dfirtrack_main_taskstatus_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskstatus
    ADD CONSTRAINT dfirtrack_main_taskstatus_pkey PRIMARY KEY (taskstatus_id);


--
-- Name: dfirtrack_main_taskstatus_taskstatus_name_key; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_taskstatus
    ADD CONSTRAINT dfirtrack_main_taskstatus_taskstatus_name_key UNIQUE (taskstatus_name);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_q_ormq_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_q_ormq
    ADD CONSTRAINT django_q_ormq_pkey PRIMARY KEY (id);


--
-- Name: django_q_schedule_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_q_schedule
    ADD CONSTRAINT django_q_schedule_pkey PRIMARY KEY (id);


--
-- Name: django_q_task_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_q_task
    ADD CONSTRAINT django_q_task_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: dfirtrack_main_analysisstatus_analysisstatus_name_3ff26025_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_analysisstatus_analysisstatus_name_3ff26025_like ON public.dfirtrack_main_analysisstatus USING btree (analysisstatus_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_analystmemo_analystmemo_created_by_use_8b4e9f45; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_analystmemo_analystmemo_created_by_use_8b4e9f45 ON public.dfirtrack_main_analystmemo USING btree (analystmemo_created_by_user_id_id);


--
-- Name: dfirtrack_main_analystmemo_analystmemo_modified_by_us_1b030832; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_analystmemo_analystmemo_modified_by_us_1b030832 ON public.dfirtrack_main_analystmemo USING btree (analystmemo_modified_by_user_id_id);


--
-- Name: dfirtrack_main_analystmemo_system_id_a762c41a; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_analystmemo_system_id_a762c41a ON public.dfirtrack_main_analystmemo USING btree (system_id);


--
-- Name: dfirtrack_main_case_case_created_by_user_id_id_84b385b3; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_case_case_created_by_user_id_id_84b385b3 ON public.dfirtrack_main_case USING btree (case_created_by_user_id_id);


--
-- Name: dfirtrack_main_case_case_name_0d7232b4_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_case_case_name_0d7232b4_like ON public.dfirtrack_main_case USING btree (case_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_company_company_name_666c6af2_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_company_company_name_666c6af2_like ON public.dfirtrack_main_company USING btree (company_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_company_division_id_a92adb0f; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_company_division_id_a92adb0f ON public.dfirtrack_main_company USING btree (division_id);


--
-- Name: dfirtrack_main_contact_contact_email_0d335dc6_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_contact_contact_email_0d335dc6_like ON public.dfirtrack_main_contact USING btree (contact_email varchar_pattern_ops);


--
-- Name: dfirtrack_main_division_division_name_dfec548d_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_division_division_name_dfec548d_like ON public.dfirtrack_main_division USING btree (division_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_domain_domain_name_6aa46ad2_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_domain_domain_name_6aa46ad2_like ON public.dfirtrack_main_domain USING btree (domain_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_entry_case_id_b427e77a; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_entry_case_id_b427e77a ON public.dfirtrack_main_entry USING btree (case_id);


--
-- Name: dfirtrack_main_entry_entry_created_by_user_id_id_547943f7; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_entry_entry_created_by_user_id_id_547943f7 ON public.dfirtrack_main_entry USING btree (entry_created_by_user_id_id);


--
-- Name: dfirtrack_main_entry_entry_modified_by_user_id_id_3c22b68d; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_entry_entry_modified_by_user_id_id_3c22b68d ON public.dfirtrack_main_entry USING btree (entry_modified_by_user_id_id);


--
-- Name: dfirtrack_main_entry_system_id_86a519ec; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_entry_system_id_86a519ec ON public.dfirtrack_main_entry USING btree (system_id);


--
-- Name: dfirtrack_main_headline_headline_name_b01d616a_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_headline_headline_name_b01d616a_like ON public.dfirtrack_main_headline USING btree (headline_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_location_location_name_eaec8404_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_location_location_name_eaec8404_like ON public.dfirtrack_main_location USING btree (location_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_os_os_name_d6232c5d_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_os_os_name_d6232c5d_like ON public.dfirtrack_main_os USING btree (os_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_osarch_osarch_name_f84bee38_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_osarch_osarch_name_f84bee38_like ON public.dfirtrack_main_osarch USING btree (osarch_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_osimportname_os_id_76f6a41f; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_osimportname_os_id_76f6a41f ON public.dfirtrack_main_osimportname USING btree (os_id);


--
-- Name: dfirtrack_main_osimportname_osimportname_name_a8c6d014_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_osimportname_osimportname_name_a8c6d014_like ON public.dfirtrack_main_osimportname USING btree (osimportname_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_reason_reason_name_efc62890_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_reason_reason_name_efc62890_like ON public.dfirtrack_main_reason USING btree (reason_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_recommendation_recommendation_name_0538a32a_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_recommendation_recommendation_name_0538a32a_like ON public.dfirtrack_main_recommendation USING btree (recommendation_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_reportitem_headline_id_3e6e09a4; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_reportitem_headline_id_3e6e09a4 ON public.dfirtrack_main_reportitem USING btree (headline_id);


--
-- Name: dfirtrack_main_reportitem_reportitem_created_by_user_8b3902d1; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_reportitem_reportitem_created_by_user_8b3902d1 ON public.dfirtrack_main_reportitem USING btree (reportitem_created_by_user_id_id);


--
-- Name: dfirtrack_main_reportitem_reportitem_modified_by_use_d6bdbb25; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_reportitem_reportitem_modified_by_use_d6bdbb25 ON public.dfirtrack_main_reportitem USING btree (reportitem_modified_by_user_id_id);


--
-- Name: dfirtrack_main_reportitem_system_id_c5ff4bb8; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_reportitem_system_id_c5ff4bb8 ON public.dfirtrack_main_reportitem USING btree (system_id);


--
-- Name: dfirtrack_main_servicepr_serviceprovider_name_33f04731_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_servicepr_serviceprovider_name_33f04731_like ON public.dfirtrack_main_serviceprovider USING btree (serviceprovider_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_system_analysisstatus_id_a4ae4a04; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_analysisstatus_id_a4ae4a04 ON public.dfirtrack_main_system USING btree (analysisstatus_id);


--
-- Name: dfirtrack_main_system_case_case_id_1aab69f6; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_case_case_id_1aab69f6 ON public.dfirtrack_main_system_case USING btree (case_id);


--
-- Name: dfirtrack_main_system_case_system_id_d9464a33; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_case_system_id_d9464a33 ON public.dfirtrack_main_system_case USING btree (system_id);


--
-- Name: dfirtrack_main_system_company_company_id_a651b8d0; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_company_company_id_a651b8d0 ON public.dfirtrack_main_system_company USING btree (company_id);


--
-- Name: dfirtrack_main_system_company_system_id_46949304; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_company_system_id_46949304 ON public.dfirtrack_main_system_company USING btree (system_id);


--
-- Name: dfirtrack_main_system_contact_id_2ca7db77; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_contact_id_2ca7db77 ON public.dfirtrack_main_system USING btree (contact_id);


--
-- Name: dfirtrack_main_system_domain_id_e2653c87; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_domain_id_e2653c87 ON public.dfirtrack_main_system USING btree (domain_id);


--
-- Name: dfirtrack_main_system_host_system_id_b6d083d4; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_host_system_id_b6d083d4 ON public.dfirtrack_main_system USING btree (host_system_id);


--
-- Name: dfirtrack_main_system_ip_ip_id_36738a63; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_ip_ip_id_36738a63 ON public.dfirtrack_main_system_ip USING btree (ip_id);


--
-- Name: dfirtrack_main_system_ip_system_id_391bc2ce; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_ip_system_id_391bc2ce ON public.dfirtrack_main_system_ip USING btree (system_id);


--
-- Name: dfirtrack_main_system_location_id_9085a988; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_location_id_9085a988 ON public.dfirtrack_main_system USING btree (location_id);


--
-- Name: dfirtrack_main_system_os_id_278b71aa; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_os_id_278b71aa ON public.dfirtrack_main_system USING btree (os_id);


--
-- Name: dfirtrack_main_system_osarch_id_d411ce1c; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_osarch_id_d411ce1c ON public.dfirtrack_main_system USING btree (osarch_id);


--
-- Name: dfirtrack_main_system_reason_id_2c4b5ed9; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_reason_id_2c4b5ed9 ON public.dfirtrack_main_system USING btree (reason_id);


--
-- Name: dfirtrack_main_system_recommendation_id_2a276c05; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_recommendation_id_2a276c05 ON public.dfirtrack_main_system USING btree (recommendation_id);


--
-- Name: dfirtrack_main_system_serviceprovider_id_f8690585; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_serviceprovider_id_f8690585 ON public.dfirtrack_main_system USING btree (serviceprovider_id);


--
-- Name: dfirtrack_main_system_system_created_by_user_id_id_37ccfe2c; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_system_created_by_user_id_id_37ccfe2c ON public.dfirtrack_main_system USING btree (system_created_by_user_id_id);


--
-- Name: dfirtrack_main_system_system_modified_by_user_id_id_92a3bd0a; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_system_modified_by_user_id_id_92a3bd0a ON public.dfirtrack_main_system USING btree (system_modified_by_user_id_id);


--
-- Name: dfirtrack_main_system_systemstatus_id_625ea6ce; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_systemstatus_id_625ea6ce ON public.dfirtrack_main_system USING btree (systemstatus_id);


--
-- Name: dfirtrack_main_system_systemtype_id_29fe057c; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_systemtype_id_29fe057c ON public.dfirtrack_main_system USING btree (systemtype_id);


--
-- Name: dfirtrack_main_system_tag_system_id_8d343c41; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_tag_system_id_8d343c41 ON public.dfirtrack_main_system_tag USING btree (system_id);


--
-- Name: dfirtrack_main_system_tag_tag_id_c6424960; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_system_tag_tag_id_c6424960 ON public.dfirtrack_main_system_tag USING btree (tag_id);


--
-- Name: dfirtrack_main_systemstatus_systemstatus_name_c0b992d8_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_systemstatus_systemstatus_name_c0b992d8_like ON public.dfirtrack_main_systemstatus USING btree (systemstatus_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_systemtype_systemtype_name_575dffb5_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_systemtype_systemtype_name_575dffb5_like ON public.dfirtrack_main_systemtype USING btree (systemtype_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_systemuser_system_id_634d6fa5; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_systemuser_system_id_634d6fa5 ON public.dfirtrack_main_systemuser USING btree (system_id);


--
-- Name: dfirtrack_main_tag_tag_modified_by_user_id_id_349c36f4; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_tag_tag_modified_by_user_id_id_349c36f4 ON public.dfirtrack_main_tag USING btree (tag_modified_by_user_id_id);


--
-- Name: dfirtrack_main_tag_tag_name_f6a6484f_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_tag_tag_name_f6a6484f_like ON public.dfirtrack_main_tag USING btree (tag_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_tag_tagcolor_id_519f853f; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_tag_tagcolor_id_519f853f ON public.dfirtrack_main_tag USING btree (tagcolor_id);


--
-- Name: dfirtrack_main_tagcolor_tagcolor_name_fc427931_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_tagcolor_tagcolor_name_fc427931_like ON public.dfirtrack_main_tagcolor USING btree (tagcolor_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_task_parent_task_id_ba86b957; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_parent_task_id_ba86b957 ON public.dfirtrack_main_task USING btree (parent_task_id);


--
-- Name: dfirtrack_main_task_system_id_a0b590fd; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_system_id_a0b590fd ON public.dfirtrack_main_task USING btree (system_id);


--
-- Name: dfirtrack_main_task_tag_tag_id_5bf92469; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_tag_tag_id_5bf92469 ON public.dfirtrack_main_task_tag USING btree (tag_id);


--
-- Name: dfirtrack_main_task_tag_task_id_61ed5eab; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_tag_task_id_61ed5eab ON public.dfirtrack_main_task_tag USING btree (task_id);


--
-- Name: dfirtrack_main_task_task_assigned_to_user_id_id_2e1aee04; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_task_assigned_to_user_id_id_2e1aee04 ON public.dfirtrack_main_task USING btree (task_assigned_to_user_id_id);


--
-- Name: dfirtrack_main_task_task_created_by_user_id_id_827648d8; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_task_created_by_user_id_id_827648d8 ON public.dfirtrack_main_task USING btree (task_created_by_user_id_id);


--
-- Name: dfirtrack_main_task_task_modified_by_user_id_id_bc767997; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_task_modified_by_user_id_id_bc767997 ON public.dfirtrack_main_task USING btree (task_modified_by_user_id_id);


--
-- Name: dfirtrack_main_task_taskname_id_a816f22c; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_taskname_id_a816f22c ON public.dfirtrack_main_task USING btree (taskname_id);


--
-- Name: dfirtrack_main_task_taskpriority_id_b5eb9f27; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_taskpriority_id_b5eb9f27 ON public.dfirtrack_main_task USING btree (taskpriority_id);


--
-- Name: dfirtrack_main_task_taskstatus_id_b26f5c77; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_task_taskstatus_id_b26f5c77 ON public.dfirtrack_main_task USING btree (taskstatus_id);


--
-- Name: dfirtrack_main_taskname_taskname_name_9c8565d1_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_taskname_taskname_name_9c8565d1_like ON public.dfirtrack_main_taskname USING btree (taskname_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_taskpriority_taskpriority_name_58224b23_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_taskpriority_taskpriority_name_58224b23_like ON public.dfirtrack_main_taskpriority USING btree (taskpriority_name varchar_pattern_ops);


--
-- Name: dfirtrack_main_taskstatus_taskstatus_name_0b6d7d4c_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX dfirtrack_main_taskstatus_taskstatus_name_0b6d7d4c_like ON public.dfirtrack_main_taskstatus USING btree (taskstatus_name varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: dfirtrack
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_analy_analystmemo_created__8b4e9f45_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_analystmemo
    ADD CONSTRAINT dfirtrack_main_analy_analystmemo_created__8b4e9f45_fk_auth_user FOREIGN KEY (analystmemo_created_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_analy_analystmemo_modified_1b030832_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_analystmemo
    ADD CONSTRAINT dfirtrack_main_analy_analystmemo_modified_1b030832_fk_auth_user FOREIGN KEY (analystmemo_modified_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_analy_system_id_a762c41a_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_analystmemo
    ADD CONSTRAINT dfirtrack_main_analy_system_id_a762c41a_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_case_case_created_by_user_84b385b3_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_case
    ADD CONSTRAINT dfirtrack_main_case_case_created_by_user_84b385b3_fk_auth_user FOREIGN KEY (case_created_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_compa_division_id_a92adb0f_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_company
    ADD CONSTRAINT dfirtrack_main_compa_division_id_a92adb0f_fk_dfirtrack FOREIGN KEY (division_id) REFERENCES public.dfirtrack_main_division(division_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_entry_case_id_b427e77a_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_entry
    ADD CONSTRAINT dfirtrack_main_entry_case_id_b427e77a_fk_dfirtrack FOREIGN KEY (case_id) REFERENCES public.dfirtrack_main_case(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_entry_entry_created_by_use_547943f7_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_entry
    ADD CONSTRAINT dfirtrack_main_entry_entry_created_by_use_547943f7_fk_auth_user FOREIGN KEY (entry_created_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_entry_entry_modified_by_us_3c22b68d_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_entry
    ADD CONSTRAINT dfirtrack_main_entry_entry_modified_by_us_3c22b68d_fk_auth_user FOREIGN KEY (entry_modified_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_entry_system_id_86a519ec_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_entry
    ADD CONSTRAINT dfirtrack_main_entry_system_id_86a519ec_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_osimp_os_id_76f6a41f_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_osimportname
    ADD CONSTRAINT dfirtrack_main_osimp_os_id_76f6a41f_fk_dfirtrack FOREIGN KEY (os_id) REFERENCES public.dfirtrack_main_os(os_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_repor_headline_id_3e6e09a4_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reportitem
    ADD CONSTRAINT dfirtrack_main_repor_headline_id_3e6e09a4_fk_dfirtrack FOREIGN KEY (headline_id) REFERENCES public.dfirtrack_main_headline(headline_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_repor_reportitem_created_b_8b3902d1_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reportitem
    ADD CONSTRAINT dfirtrack_main_repor_reportitem_created_b_8b3902d1_fk_auth_user FOREIGN KEY (reportitem_created_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_repor_reportitem_modified__d6bdbb25_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reportitem
    ADD CONSTRAINT dfirtrack_main_repor_reportitem_modified__d6bdbb25_fk_auth_user FOREIGN KEY (reportitem_modified_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_repor_system_id_c5ff4bb8_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_reportitem
    ADD CONSTRAINT dfirtrack_main_repor_system_id_c5ff4bb8_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_analysisstatus_id_a4ae4a04_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_analysisstatus_id_a4ae4a04_fk_dfirtrack FOREIGN KEY (analysisstatus_id) REFERENCES public.dfirtrack_main_analysisstatus(analysisstatus_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_case_id_1aab69f6_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_case
    ADD CONSTRAINT dfirtrack_main_syste_case_id_1aab69f6_fk_dfirtrack FOREIGN KEY (case_id) REFERENCES public.dfirtrack_main_case(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_company_id_a651b8d0_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_company
    ADD CONSTRAINT dfirtrack_main_syste_company_id_a651b8d0_fk_dfirtrack FOREIGN KEY (company_id) REFERENCES public.dfirtrack_main_company(company_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_contact_id_2ca7db77_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_contact_id_2ca7db77_fk_dfirtrack FOREIGN KEY (contact_id) REFERENCES public.dfirtrack_main_contact(contact_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_domain_id_e2653c87_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_domain_id_e2653c87_fk_dfirtrack FOREIGN KEY (domain_id) REFERENCES public.dfirtrack_main_domain(domain_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_host_system_id_b6d083d4_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_host_system_id_b6d083d4_fk_dfirtrack FOREIGN KEY (host_system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_ip_id_36738a63_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_ip
    ADD CONSTRAINT dfirtrack_main_syste_ip_id_36738a63_fk_dfirtrack FOREIGN KEY (ip_id) REFERENCES public.dfirtrack_main_ip(ip_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_location_id_9085a988_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_location_id_9085a988_fk_dfirtrack FOREIGN KEY (location_id) REFERENCES public.dfirtrack_main_location(location_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_osarch_id_d411ce1c_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_osarch_id_d411ce1c_fk_dfirtrack FOREIGN KEY (osarch_id) REFERENCES public.dfirtrack_main_osarch(osarch_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_reason_id_2c4b5ed9_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_reason_id_2c4b5ed9_fk_dfirtrack FOREIGN KEY (reason_id) REFERENCES public.dfirtrack_main_reason(reason_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_recommendation_id_2a276c05_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_recommendation_id_2a276c05_fk_dfirtrack FOREIGN KEY (recommendation_id) REFERENCES public.dfirtrack_main_recommendation(recommendation_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_serviceprovider_id_f8690585_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_serviceprovider_id_f8690585_fk_dfirtrack FOREIGN KEY (serviceprovider_id) REFERENCES public.dfirtrack_main_serviceprovider(serviceprovider_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_system_created_by_us_37ccfe2c_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_system_created_by_us_37ccfe2c_fk_auth_user FOREIGN KEY (system_created_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_system_id_391bc2ce_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_ip
    ADD CONSTRAINT dfirtrack_main_syste_system_id_391bc2ce_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_system_id_46949304_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_company
    ADD CONSTRAINT dfirtrack_main_syste_system_id_46949304_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_system_id_634d6fa5_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_systemuser
    ADD CONSTRAINT dfirtrack_main_syste_system_id_634d6fa5_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_system_id_8d343c41_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_tag
    ADD CONSTRAINT dfirtrack_main_syste_system_id_8d343c41_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_system_id_d9464a33_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_case
    ADD CONSTRAINT dfirtrack_main_syste_system_id_d9464a33_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_system_modified_by_u_92a3bd0a_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_system_modified_by_u_92a3bd0a_fk_auth_user FOREIGN KEY (system_modified_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_systemstatus_id_625ea6ce_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_systemstatus_id_625ea6ce_fk_dfirtrack FOREIGN KEY (systemstatus_id) REFERENCES public.dfirtrack_main_systemstatus(systemstatus_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_systemtype_id_29fe057c_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_syste_systemtype_id_29fe057c_fk_dfirtrack FOREIGN KEY (systemtype_id) REFERENCES public.dfirtrack_main_systemtype(systemtype_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_syste_tag_id_c6424960_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system_tag
    ADD CONSTRAINT dfirtrack_main_syste_tag_id_c6424960_fk_dfirtrack FOREIGN KEY (tag_id) REFERENCES public.dfirtrack_main_tag(tag_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_system_os_id_278b71aa_fk_dfirtrack_main_os_os_id; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_system
    ADD CONSTRAINT dfirtrack_main_system_os_id_278b71aa_fk_dfirtrack_main_os_os_id FOREIGN KEY (os_id) REFERENCES public.dfirtrack_main_os(os_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_tag_tag_modified_by_user_349c36f4_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_tag
    ADD CONSTRAINT dfirtrack_main_tag_tag_modified_by_user_349c36f4_fk_auth_user FOREIGN KEY (tag_modified_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_tag_tagcolor_id_519f853f_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_tag
    ADD CONSTRAINT dfirtrack_main_tag_tagcolor_id_519f853f_fk_dfirtrack FOREIGN KEY (tagcolor_id) REFERENCES public.dfirtrack_main_tagcolor(tagcolor_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task__tag_id_5bf92469_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task_tag
    ADD CONSTRAINT dfirtrack_main_task__tag_id_5bf92469_fk_dfirtrack FOREIGN KEY (tag_id) REFERENCES public.dfirtrack_main_tag(tag_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task__task_id_61ed5eab_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task_tag
    ADD CONSTRAINT dfirtrack_main_task__task_id_61ed5eab_fk_dfirtrack FOREIGN KEY (task_id) REFERENCES public.dfirtrack_main_task(task_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task_parent_task_id_ba86b957_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_parent_task_id_ba86b957_fk_dfirtrack FOREIGN KEY (parent_task_id) REFERENCES public.dfirtrack_main_task(task_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task_system_id_a0b590fd_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_system_id_a0b590fd_fk_dfirtrack FOREIGN KEY (system_id) REFERENCES public.dfirtrack_main_system(system_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task_task_assigned_to_use_2e1aee04_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_task_assigned_to_use_2e1aee04_fk_auth_user FOREIGN KEY (task_assigned_to_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task_task_created_by_user_827648d8_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_task_created_by_user_827648d8_fk_auth_user FOREIGN KEY (task_created_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task_task_modified_by_use_bc767997_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_task_modified_by_use_bc767997_fk_auth_user FOREIGN KEY (task_modified_by_user_id_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task_taskname_id_a816f22c_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_taskname_id_a816f22c_fk_dfirtrack FOREIGN KEY (taskname_id) REFERENCES public.dfirtrack_main_taskname(taskname_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task_taskpriority_id_b5eb9f27_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_taskpriority_id_b5eb9f27_fk_dfirtrack FOREIGN KEY (taskpriority_id) REFERENCES public.dfirtrack_main_taskpriority(taskpriority_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dfirtrack_main_task_taskstatus_id_b26f5c77_fk_dfirtrack; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.dfirtrack_main_task
    ADD CONSTRAINT dfirtrack_main_task_taskstatus_id_b26f5c77_fk_dfirtrack FOREIGN KEY (taskstatus_id) REFERENCES public.dfirtrack_main_taskstatus(taskstatus_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk; Type: FK CONSTRAINT; Schema: public; Owner: dfirtrack
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

