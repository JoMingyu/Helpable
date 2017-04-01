# id 존재 여부 체크
id_exist_check_format = "SELECT id FROM account WHERE id='%s'"

# 유저 기본 정보 초기화
signup_primary_data_insert_format = "INSERT INTO account(id, password, registration_key, name, age, type, gender, phone_number, password_question, password_answer) VALUES('%s', '%s', '%s', '%s', %d, %d, '%s', '%s', '%s', '%s')"
person_contribution_initialize_format = "INSERT INTO user_contribution(id, give, take) VALUES('%s', 0, 0)"

# 유저 종류에 따른 데이터 삽입 포맷
disabled_person_signup_format = "UPDATE account SET disability_rating=%d, disability_type='%s' WHERE id='%s'"
ordinary_person_signup_format = "UPDATE account SET affiliation='%s' WHERE id='%s'"

# 비밀번호 변경 포맷
password_change_format = "UPDATE account SET password='%s' WHERE id='%s'"

# 푸쉬알림용 registration id get 포맷
get_registration_id_format = "SELECT registration_key from account"

# 사용자 정보 get 포맷
get_user_info_format = "SELECT * FROM account WHERE id='%s'"
get_user_contribution_format = "SELECT * FROM user_contribution WHERE id='%s'"

# 도움 요청 데이터 삽입 포맷
request_help_format = "INSERT INTO help_list(requester_id, date, longitude, latitude, content) VALUES('%s', CURDATE(), %f, %f, '%s')"

# 도움 요청 목록 로드 포맷
get_help_list_format = "SELECT * FROM help_list"

# idx에 대한 도움 요청 로드 포맷
get_help_format = "SELECT requester_id FROM help_list WHERE idx=%d"

# 도움 요청 삭제 포맷
delete_help_format = "DELETE FROM help_list WHERE idx=%d"
