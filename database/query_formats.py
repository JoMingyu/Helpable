id_exist_check_format = "SELECT id FROM account WHERE id='%s'"

signup_primary_data_insert_format = "INSERT INTO account(id, password, registration_key, name, age, type, gender) VALUES('%s', '%s', '%s', '%s', %d, %d, '%s')"
person_activity_initialize_format = "INSERT INTO person_activity(id, give, take) VALUES('%s', 0, 0)"
disabled_person_signup_format = "UPDATE account SET disability_rating=%d, disability_type='%s' WHERE id='%s'"
ordinary_person_signup_format = "UPDATE account SET affiliation='%s' WHERE id='%s'"
get_registration_id_format = "SELECT registration_key from account"

get_person_data_format = "SELECT * FROM account WHERE id='%s'"
get_person_activity_format = "SELECT * FROM person_activity WHERE id='%s'"
