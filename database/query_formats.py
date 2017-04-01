id_exist_check_format = "SELECT id FROM account WHERE id='%s'"

signup_primary_data_insert_format = "INSERT INTO account(id, password, registration_key, name, age, type, gender) VALUES('%s', '%s', '%s', '%s', %d, %d, '%s')"
disabled_person_signup_format = "UPDATE account SET disability_rating=%d, disability_type='%s' WHERE id='%s'"
ordinary_person_signup_format = "UPDATE account SET affiliation='%s' WHERE id='%s'"
