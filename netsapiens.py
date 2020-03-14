import os
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

from dotenv import load_dotenv
load_dotenv()


TOKEN_URL = os.getenv('TOKEN_URL')
BASE_URL = os.getenv('BASE_URL')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

class Netsapiens(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.nsclient = OAuth2Session(client=LegacyApplicationClient(client_id=CLIENT_ID))

    def fetch_token(self):
        try:
            self.nsclient.fetch_token(token_url=TOKEN_URL, username=self.username, password=self.password, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
            return self.nsclient.token
        except:
            print('Error fetching new token! Check username or password!')

    def api_call(self, object_, action, params=None, format__='json'):
        self.fetch_token()
        resource_url = BASE_URL + f'?object={object_}&action={action}&format={format_}'
        return self.nsclient.get(resource_url, params=params)


    def domain_read(self, domain=None, format__='json'):
        params = None
        if(domain is not None): params = {'domain': domain}
        return self.api_call('domain', 'read', params, format__)


    def reseller_create(self, territory, description):
        pass
    def reseller_count(self, territory):
        pass
    def reseller_read(self, territory, start, limit, sort):
        pass
    def reseller_update(self, territory, description):
        pass
    def reseller_delete(self, territory):
        pass
    def domain_create(self, domain, territory, description, call_limit, call_limit_ext, max_user, max_call_queue, max_aa, max_conference, max_department, max_site, max_device):
        pass
    def domain_count(self, domain, territory):
        pass
    def domain_read(self, domain):
        pass
    def domain_update(self, domain, territory, moh, mor, mot, rmoh, rating, resi, sub_limit, dial_plan, dial_policy, email_sender, smtp_host, smtp_port, smtp_uid, smtp_pwd, from_user, description, call_limit, call_limit_ext, max_user, max_call_queue, max_aa, max_conference, max_department, max_device, max_site, policies):
        pass
    def domain_delete(self, domain):
        pass
    def domain_readbilling(self, domain):
        pass
    def subscriber_create(self, uid, user, domain, subscriber_login, first_name, last_name, passwordLength, pwd_hash, subscriber_pin, dir_anc, dir_list, message, pwd, group, dir, email, vmail_provisioned, vmail_frd_to, vmail_enabled, vmail_greeting, vmail_notify, vmail_annc_time, vmail_annc_cid, vmail_sort_lifo, vmail_transcribe, data_limit, call_limit, dial_plan, dial_policy, area_code, callid_name, callid_nmbr, callid_emgr, no_answer_timeout, time_zone, scope, rej_anony, screen, srv_code, ntfy_missed_call, ntfy_data_limit, language):
        pass
    def subscriber_count(self, domain, territory):
        pass
    def subscriber_read(self, uid, user, domain, login, limit, first_name, last_name, group, fields, srv_code, email, dir, filter_users, directory_match, owner, scope, start, sort):
        pass
    def subscriber_update(self, uid, user, domain, first_name, last_name, dir_anc, dir_list, message, subscriber_login, pwd, current_password, pwd_hash, group, dir, email, vmail_provisioned, vmail_frd_to, vmail_enabled, vmail_greeting, vmail_notify, vmail_annc_time, vmail_annc_cid, vmail_sort_lifo, vmail_transcribe, data_limit, call_limit, dial_plan, dial_policy, area_code, callid_name, callid_nmbr, callid_emgr, no_answer_timeout, time_zone, scope, rej_anony, screen, srv_code, ntfy_missed_call, ntfy_data_limit, language):
        pass
    def subscriber_delete(self, uid, domain, user, termination_match, device):
        pass
    def subscriber_list(self, domain, fields):
        pass
    def device_create(self, domain, device, user, mac, model):
        pass
    def device_count(self, domain, territory, user, aor, device, limit, start, sort):
        pass
    def device_read(self, domain, device, user, owner, start, mode, limit, sort, list, fields, filters, noNDP):
        pass
    def device_update(self, device, domain, check_sync, evtCheckSync, mac, transport, model, mode, user_agent, accept_agent, received_from, registration_time, subscriber_name, subscriber_domain, authentication_key, call_processing_rule, registration_expires_time, sub_fullname, sub_scope, sub_login, ndperror):
        pass
    def device_delete(self, device, termination_match):
        pass
    def connection_create(self, aor, domain, termination_match, to_host_trans, address, req_host_trans, route):
        pass
    def connection_count(self, aor, termination_match, domain, territory, role):
        pass
    def connection_read(self, aor, termination_match, domain, territory, routechain, role):
        pass
    def connection_update(self, aor, termination_match, route, domain, role, req_user_trans, req_host_trans, to_user_trans, to_host_trans, from_user_trans, from_host_trans, address, origination_allowed, termination_allowed, nat_wan, authenticate_invite, authentication_alg, auth_user, authentication_realm, authentication_key, registration_required, registration_time, registration_expires, rate, rate_account, rate_max, rate_ratio, rate_margin, max_orig, max_term, max_total, min_orig_prd, min_term_prd, min_dura, nameout_dial_translation, out_dial_delay, out_dial_mode, dial_plan, dial_policy, gmt_offset, time_zone, call_processing_rule, description, count_in, count_out, total_orig, total_term, period_orig, period_term, ts, mac):
        pass
    def connection_delete(self, aor, termination_match, isRoute):
        pass
    def message_create(self, domain, user, type, from_num, destination, message):
        pass
    def message_read(self, domain, user, session_id, start, limit, sort):
        pass
    def message_notifyunreadmessages(self, subject):
        pass
    def message_readprocessemail(self, domain, user, session_id, template, subject, cclist):
        pass
    def agent_create(self, domain, queue, device):
        pass
    def agent_count(self, domain, queue, device):
        pass
    def agent_read(self, domain, queue_name, queue_list, device, period, stats, start_date, end_date, range_interval):
        pass
    def agent_update(self, domain, queue, device, huntgroup_name, huntgroup_domain, entry_option, wrap_up_sec, auto_ans, entry_order, entry_priority, call_limit, confirm_required, entry_device, entry_status, owner_user, owner_domain, session_count, error_info, last_update, stat, sub_firstname, sub_lastname, sub_login, sub_fullname):
        pass
    def agent_delete(self, domain, queue, device):
        pass
    def agent_updatestatus(self, domain, queue, device, entry_action, entry_option):
        pass
    def agent_log_create(self, agent, user, domain, mode, loggedin_sec, available_sec, unavailable_sec, break_sec, lunch_sec, meeting_sec, other_sec, acw_sec, web_sec, timestamp):
        pass
    def agent_log_read(self, domain, find, select, queue_list, queue_name, start_date, end_date, range_interval, agent, user, start, limit, period, department, format_):
        pass
    def answer_rule_create(self, time_frame, uid, user, domain):
        pass
    def answer_rule_count(self, uid, domain, user, time_frame):
        pass
    def answer_rule_read(self, uid, user, domain, limit, time_frame, caller_match, for_numbers, fna_numbers):
        pass
    def answer_rule_update(self, time_frame, uid, user, domain, rej_parameters, rej_control, acp_parameters, acp_control, deletesok, enable, order, first_name, last_name, subscriber_login, pwd, pwd_hash, group, dir, email, presence, message, vmail_provisioned, vmail_enabled, vmail_greeting, vmail_notify, vmail_annc_time, vmail_annc_cid, vmail_sort_lifo, vmail_transcribe, data_limit, call_limit, dial_plan, dial_policy, area_code, callid_name, callid_nmbr, callid_emgr, no_answer_timeout, time_zone, dir_anc, dir_list, date_created, scope, rej_anony, directory_order, screen, srv_code, ntfy_missed_call, ntfy_data_limit, language, gauSession, last_update):
        pass
    def answer_rule_delete(self, time_frame, uid, user, domain):
        pass
    def answer_rule_reorder(self, uid, user, domain, priority):
        pass
    def audio_count(self, domain, user, type, index):
        pass
    def audio_read(self, domain, user, index, type, directurl, fax):
        pass
    def audio_update(self, owner_domain, index, owner, type, script, forward):
        pass
    def audio_delete(self, owner_domain, index, owner, type):
        pass
    def audio_play(self, domain, user, type, file, index, time, auth):
        pass
    def audio_upload(self, owner_domain, owner, type, script, file, index, time, convert, FromName, NmsAni, NmsRecDuration, RecordTime):
        pass
    def cdr2_update(self, cdr_id, domain_name, uid, notes, disposition, reason, pac, time_disp):
        pass
    def cdr2_readbydomain(self, cdr_id, start_date, end_date, domain, limit):
        pass
    def cdr2_readbygroup(self, domain, group, start_date, end_date, limit, orig_from_uri, orig_to_user):
        pass
    def cdr2_readbyid(self, start_date, end_date, id, hostname, limit, orig_callid, term_callid, time_release):
        pass
    def cdr2_readbyterritory(self, cdr_id, start_date, end_date, territory, limit):
        pass
    def cdr2_readbyuser(self, start_date, end_date, limit, uid, type, showhidden):
        pass
    def cdr2_reportbydomain(self, start_date, end_date, domain, report_by):
        pass
    def cdr2_reportbygrouptype(self, start_date, end_date, group_type, grp, report_by):
        pass
    def cdr2_reportbygroup(self, start_date, end_date, group_by, report_by):
        pass
    def cdr2_reportbyhostname(self, start_date, end_date, hostname, report_by):
        pass
    def cdr2_reportbyreseller(self, start_date, end_date, reseller, report_by):
        pass
    def cdr2_countbydomain(self, cdr_id, start_date, end_date, domain, limit):
        pass
    def cdr2_countbygroup(self, start_date, end_date, limit, orig_from_uri, orig_to_user, group):
        pass
    def cdr2_countbyterritory(self, start_date, end_date, territory, cdr_id, limit):
        pass
    def cdr2_countbyuser(self, start_date, end_date, limit, uid, name, number):
        pass
    def cdr_export_create(self, schedule_name, domain, reseller, user, cdr_format, last_run_time, next_run_time, cdr_count, server, period):
        pass
    def cdr_export_read(self, domain, reseller, schedule_name):
        pass
    def cdr_export_update(self, schedule_name, domain, reseller, user, cdr_format, last_run_time, next_run_time, cdr_count, server):
        pass
    def cdr_export_delete(self, schedule_name, domain, reseller, user, cdr_format, last_run_time, next_run_time, cdr_count):
        pass
    def cdr_export_download(self, schedule_name, domain, reseller, user, cdr_format, last_run_time, next_run_time, cdr_count):
        pass
    def cdr_schedule_create(self, schedule_name, reseller, domain, user, period, cdrschedule_preset, time_start_preset, time_zone, cdr_format, include_header, inbound, outbound, offnet, script_enable, script_path, export_method, email, hostname, remote_path, last_sequence_number, next_run_time, send_email, report_cycle, error_backoff, status):
        pass
    def cdr_schedule_count(self, schedule_name, user, reseller, domain):
        pass
    def cdr_schedule_read(self, schedule_name, domain, reseller, sort, limit):
        pass
    def cdr_schedule_update(self, schedule_name, reseller, domain, user, period, cdr_format, include_header, inbound, outbound, offnet, script_enable, script_path, export_method, email, hostname, remote_path, last_run_time, next_run_time, send_email, report_cycle, status, server, start_time, kill_time, previous_export_date):
        pass
    def cdr_schedule_delete(self, schedule_name, domain):
        pass
    def call_count(self, domain, groupby, territory):
        pass
    def call_read(self, domain, start, limit, sort):
        pass
    def call_report(self, start_date, end_date, group_by, domain, hostname, reseller, cluster, site, group, connection, report_by, type):
        pass
    def call_answer(self, callid, uid, destination):
        pass
    def call_disconnect(self, callid, uid):
        pass
    def call_park(self, callid, uid, prefix):
        pass
    def call_make(self, callid, uid, destination, origination, application, auto, cbani, ani):
        pass
    def call_holdterm(self, callid, uid):
        pass
    def call_holdorig(self, callid, uid):
        pass
    def call_playback(self, callid, uid, destination, type, index, auto, ani, script, description):
        pass
    def call_calltorecord(self, callid, uid, destination, type, index, auto, ani, script, description):
        pass
    def call_recordstart(self, callid, uid, aor):
        pass
    def call_reject(self, callid, uid, aor):
        pass
    def call_recordstop(self, callid, uid):
        pass
    def call_transfer(self, callid, uid, destination, hostname, dest_sessionId):
        pass
    def call_unhold(self, callid, uid):
        pass
    def call_center_stats_readagentlog(self, domain, type, start_date, end_date, group, fields):
        pass
    def call_center_stats_readdnisstats(self, domain, type, start_date, end_date, fields, queue, remove_zeros):
        pass
    def call_center_stats_readqueuestats(self, domain, type, start_date, end_date, queue, queue_list, fields, remove_zeros):
        pass
    def call_center_stats_readuserstats(self, domain, type, start_date, end_date, fields, group, queue, remove_zeros):
        pass
    def call_center_stats_readprocessemail(self, domain, user, start_date, end_date, range_interval, report, template, subject, cclist, queue_fields, agent_fields, dnis_fields, include_csv, queue_list):
        pass
    def call_queue_create(self, domain, queue, description, max_time, wait_limit, length_limit, agent_required, run_stats, auto_logout, callback_max_hours, options, queue_audio, huntgroup_option):
        pass
    def call_queue_read(self, domain, queue_name, type, sort, start, limit, list, fields, queue_list, agent, run_stats, stats, start_date, end_date, range_interval):
        pass
    def call_queue_report(self, domain, period, type, logic, sla, op_term_sub, queue, queue_list, range_interval, value_offset, start_date, end_date, read, stat, logic2, format_):
        pass
    def call_queue_update(self, domain, queue, queue_option, huntgroup_option):
        pass
    def call_queue_delete(self, domain, queue):
        pass
    def call_queue_stats_read(self, domain, queue, format_):
        pass
    def call_request_create(self, uid, timeToCall, dDay, dHour, dMin, dSec, requestFrom):
        pass
    def call_request_read(self, request_id, orig_address, user, domain):
        pass
    def call_request_delete(self, uid, requestId):
        pass
    def caller_id_emergency_read(self, domain):
        pass
    def callqueueemailreport_create(self, uid, domain, type, frequency, range_interval, dom, dow, tod):
        pass
    def callqueueemailreport_read(self, uid, domain, type):
        pass
    def callqueueemailreport_update(self, uid, domain, type, frequency, range_interval, dom, dow, tod):
        pass
    def callqueueemailreport_delete(self, uid, domain, type, frequency):
        pass
    def chart_create(self, domain, name, dashboard_id, type, description, properties, data_sources, status):
        pass
    def chart_count(self, domain, dashboard_id, type, format_):
        pass
    def chart_read(self, dashboard_id, domain, id, name, format_):
        pass
    def chart_update(self, id, domain, dashboard_id, name, description, properties, data_sources, status):
        pass
    def chart_delete(self, id, domain):
        pass
    def chart_list(self, domain, dashboard_id, format_):
        pass
    def conference_create(self, aor, owner_uid, domain, owner, extension, SipSipAuthUser, SipSipAuthKey, RegRequired, save_participants, request_name, annc_part, leader_req, termination_match, call_processing_rule):
        pass
    def conference_count(self, aor, owner_domain, owner_uid):
        pass
    def conference_read(self, aor, domain, limit, fields, user, start, filter_bridges):
        pass
    def conference_update(self, aor, owner_uid, owner, owner_domain, save_participants, request_name, annc_part, leader_req):
        pass
    def conference_delete(self, aor, type):
        pass
    def conference_participant_create(self, conference_match, participant):
        pass
    def conference_participant_read(self, conference_match):
        pass
    def conference_record_cdr(self, aor, domain, conference, include_particapants, from_, to, conf_id):
        pass
    def contact_create(self, domain, user, first_name, last_name, home_phone, cell_phone, work_phone, email, fax):
        pass
    def contact_count(self, domain, user, first_name, last_name, contact_id):
        pass
    def contact_read(self, domain, user, first_name, last_name, tags, includeDomain, limit, department, order, contact_id):
        pass
    def contact_update(self, domain, user, first_name, last_name, company, work_phone, cell_phone, fax, email, home_phone, time_answer, tags, ts, contact_id):
        pass
    def contact_delete(self, domain, user, first_name, last_name, contact_id):
        pass
    def dashboard_create(self, name, domain, description, properties, layouts, owner_type, owner_id, status, share_type, share_details, public_id):
        pass
    def dashboard_count(self, domain, owner_id, format_):
        pass
    def dashboard_read(self, domain, id, name, owner_id, format_):
        pass
    def dashboard_update(self, id, domain, name, description, properties, layouts, owner_type, owner_id, status, share_type, share_details, public_id):
        pass
    def dashboard_delete(self, id):
        pass
    def dashboard_list(self, domain, owner_id, format_):
        pass
    def dashboard_hide(self, dashboard_id, domain):
        pass
    def dashboard_favorite(self, dashboard_id, domain):
        pass
    def default_read(self, domain, table_name):
        pass
    def department_create(self, user, domain, directory_match, first_name, last_name, dir_list, dir_anc, srv_code, passwordLength, pwd_hash, subscriber_pin):
        pass
    def department_list(self, domain):
        pass
    def device_model_read(self, brand, model, portal_view, include_ndp_defs, ndp_syntax):
        pass
    def device_profile_create(self, territory, description):
        pass
    def device_profile_count(self, territory):
        pass
    def device_profile_read(self, territory, device_type, brand, model):
        pass
    def device_profile_delete(self, domain, queue, device):
        pass
    def device_profile_readimage(self, filename, server, domain, territory):
        pass
    def dial_plan_create(self, domain, dialplan, plan_description):
        pass
    def dial_plan_read(self, dialplan, domain):
        pass
    def dial_plan_delete(self, domain, dialplan):
        pass
    def dial_policy_read(self, domain):
        pass
    def dial_rule_create(self, domain, dialplan, matchrule, to_user):
        pass
    def dial_rule_count(self, domain, dialplan):
        pass
    def dial_rule_read(self, domain, dialplan):
        pass
    def dial_rule_update(self, domain, dialplan, matchrule, dow, tod_from, tod_to, responder, parameter, to_scheme, to_user, to_host, from_name, from_scheme, from_user, from_host, plan_description):
        pass
    def dial_rule_delete(self, domain, dialplan, matchrule):
        pass
    def image_read(self, filename, server, domain, territory):
        pass
    def mac_create(self, mac, domain, model, transport, server, last_pull, date_created, device1, device2, device3, device4, device5, device6, device7, device8, territory, notes, line1_ext, line2_ext, redundancy, line1_enable, line2_enable, line3_enable, line4_enable, line5_enable, line6_enable, line7_enable, line8_enable, line1_share, line2_share, line3_share, line4_share, line5_share, line6_share, line7_share, line8_share, overrides, dir_inc, presence):
        pass
    def mac_count(self, domain, territory, mac, mac_LIKE, model, notes):
        pass
    def mac_read(self, mac, extension, checkExistance):
        pass
    def mac_update(self, mac, model, line, device, transport, server, last_pull, date_created, device1, device2, device3, device4, device5, device6, device7, device8, territory, notes, line1_ext, line2_ext, redundancy, line1_enable, line2_enable, line3_enable, line4_enable, line5_enable, line6_enable, line7_enable, line8_enable, line1_share, line2_share, line3_share, line4_share, line5_share, line6_share, line7_share, line8_share, overrides, dir_inc, presence):
        pass
    def mac_delete(self, mac, domain):
        pass
    def message_session_read(self, domain, user, session_id, term_queue, start, limit, sort):
        pass
    def message_session_update(self, domain, user, session_id, rx_hostname, muted):
        pass
    def message_session_update(self, domain, user, session_id):
        pass
    def message_session_delete(self, domain, user, session_id):
        pass
    def message_session_accept(self, domain, user, session_id, term_queue, rx_hostname, muted):
        pass
    def ndp_server_list(self, server):
        pass
    def ndp_server_read(self, server):
        pass
    def permission_create(self, domain, dialpolicy, dial_match, mode, reason):
        pass
    def permission_read(self, domain, dialpolicy, dial_match):
        pass
    def permission_update(self, domain, dialpolicy, dial_match, mode, reason):
        pass
    def permission_delete(self, domain, dialpolicy, dial_match):
        pass
    def phone_configuration_create(self, domain, description):
        pass
    def phone_configuration_count(self, territory):
        pass
    def phone_configuration_read(self, territory):
        pass
    def phone_configuration_read(self, territory, domain, mac, templatesOnly):
        pass
    def phone_configuration_delete(self, domain, queue, device):
        pass
    def phone_number_create(self, dest_domain, dialplan, matchrule, responder, to_user, to_host, enable):
        pass
    def phone_number_count(self, dialplan, dest_domain, matchrule):
        pass
    def phone_number_read(self, dialplan, dest_domain, matchrule, matchrule_LIKE):
        pass
    def phone_number_update(self, dest_domain, dialplan, matchrule, enable, dow, tod_from, tod_to, responder, parameter, to_scheme, to_user, to_host, from_name, from_scheme, from_user, from_host, plan_description):
        pass
    def phone_number_delete(self, domain, dialplan, matchrule):
        pass
    def presence_list(self, domain, last_update, limit, department, order, format_):
        pass
    def queued_read(self, domain, queue):
        pass
    def quota_create(self, domain, countLimit, sizeLimit, timeLimit, ageLimit):
        pass
    def quota_count(self, territory, domain):
        pass
    def quota_read(self, territory, domain):
        pass
    def quota_update(self, domain, countLimit, sizeLimit, timeLimit, ageLimit):
        pass
    def quota_delete(self, domain):
        pass
    def quota_readusages(self, territory, domain, date):
        pass
    def recording_create(self, aor):
        pass
    def recording_read(self, orig_callid, term_callid, callid):
        pass
    def recording_update(self, aor, status, call_id, time_open, time_close, duration, size, geo_id, url):
        pass
    def recording_delete(self, aor):
        pass
    def sms_number_create(self, domain, number, application, dest):
        pass
    def sms_number_count(self, domain, dest, number):
        pass
    def sms_number_read(self, domain, dest, number):
        pass
    def sms_number_update(self, domain, number, application, dest):
        pass
    def server_info_read(self, hostname, element_id, fields):
        pass
    def sfu_create(self, uid, room_id):
        pass
    def site_list(self, domain):
        pass
    def subscription_create(self, model, post_url, expires, domain):
        pass
    def subscription_read(self, subscription_id, domain):
        pass
    def subscription_delete(self, subscription_id, domain):
        pass
    def time_frame_create(self, domain, uid, user, owner, owner_domain, enable, order, selection_order):
        pass
    def time_frame_read(self, domain, start, limit):
        pass
    def time_frame_update(self, domain, uid, user, owner, owner_domain, enable, order, selection_order):
        pass
    def time_range_create(self, date_from, date_to, tod_from, tod_to, uid, owner_domain, owner, time_frame, days, invert, order):
        pass
    def time_range_update(self, date_from, date_to, tod_from, tod_to, uid, owner_domain, owner, time_frame, days, invert, order):
        pass
    def turn_read(self, domain, user):
        pass
    def uc_inbox_read(self, domain, user):
        pass
    def ui_config_create(self, domain, config_name, user, role, login_type, config_value, description):
        pass
    def ui_config_count(self, config_name, domain, user, role, login_type):
        pass
    def ui_config_read(self, domain, config_name, user, role, login_type):
        pass
    def ui_config_update(self, domain, config_name, user, role, login_type, config_value, description):
        pass
    def ui_config_delete(self, domain, config_name, user, role, login_type):
        pass

