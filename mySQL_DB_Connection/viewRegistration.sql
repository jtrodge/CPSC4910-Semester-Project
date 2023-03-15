SELECT `auth_group`.`id`,
    `auth_group`.`name`
FROM `REGISTRATION`.`auth_group`;

SELECT `auth_group_permissions`.`id`,
    `auth_group_permissions`.`group_id`,
    `auth_group_permissions`.`permission_id`
FROM `REGISTRATION`.`auth_group_permissions`;

SELECT `auth_permission`.`id`,
    `auth_permission`.`name`,
    `auth_permission`.`content_type_id`,
    `auth_permission`.`codename`
FROM `REGISTRATION`.`auth_permission`;

SELECT `auth_user`.`id`,
    `auth_user`.`password`,
    `auth_user`.`last_login`,
    `auth_user`.`is_superuser`,
    `auth_user`.`username`,
    `auth_user`.`first_name`,
    `auth_user`.`last_name`,
    `auth_user`.`email`,
    `auth_user`.`is_staff`,
    `auth_user`.`is_active`,
    `auth_user`.`date_joined`
FROM `REGISTRATION`.`auth_user`;

SELECT `auth_user_groups`.`id`,
    `auth_user_groups`.`user_id`,
    `auth_user_groups`.`group_id`
FROM `REGISTRATION`.`auth_user_groups`;

SELECT `auth_user_user_permissions`.`id`,
    `auth_user_user_permissions`.`user_id`,
    `auth_user_user_permissions`.`permission_id`
FROM `REGISTRATION`.`auth_user_user_permissions`;

SELECT `django_admin_log`.`id`,
    `django_admin_log`.`action_time`,
    `django_admin_log`.`object_id`,
    `django_admin_log`.`object_repr`,
    `django_admin_log`.`action_flag`,
    `django_admin_log`.`change_message`,
    `django_admin_log`.`content_type_id`,
    `django_admin_log`.`user_id`
FROM `REGISTRATION`.`django_admin_log`;

SELECT `django_content_type`.`id`,
    `django_content_type`.`app_label`,
    `django_content_type`.`model`
FROM `REGISTRATION`.`django_content_type`;

SELECT `django_migrations`.`id`,
    `django_migrations`.`app`,
    `django_migrations`.`name`,
    `django_migrations`.`applied`
FROM `REGISTRATION`.`django_migrations`;

SELECT `django_session`.`session_key`,
    `django_session`.`session_data`,
    `django_session`.`expire_date`
FROM `REGISTRATION`.`django_session`;

SELECT `social_auth_association`.`id`,
    `social_auth_association`.`server_url`,
    `social_auth_association`.`handle`,
    `social_auth_association`.`secret`,
    `social_auth_association`.`issued`,
    `social_auth_association`.`lifetime`,
    `social_auth_association`.`assoc_type`
FROM `REGISTRATION`.`social_auth_association`;

SELECT `social_auth_code`.`id`,
    `social_auth_code`.`email`,
    `social_auth_code`.`code`,
    `social_auth_code`.`verified`,
    `social_auth_code`.`timestamp`
FROM `REGISTRATION`.`social_auth_code`;

SELECT `social_auth_nonce`.`id`,
    `social_auth_nonce`.`server_url`,
    `social_auth_nonce`.`timestamp`,
    `social_auth_nonce`.`salt`
FROM `REGISTRATION`.`social_auth_nonce`;

SELECT `social_auth_partial`.`id`,
    `social_auth_partial`.`token`,
    `social_auth_partial`.`next_step`,
    `social_auth_partial`.`backend`,
    `social_auth_partial`.`data`,
    `social_auth_partial`.`timestamp`
FROM `REGISTRATION`.`social_auth_partial`;

SELECT `social_auth_usersocialauth`.`id`,
    `social_auth_usersocialauth`.`provider`,
    `social_auth_usersocialauth`.`uid`,
    `social_auth_usersocialauth`.`extra_data`,
    `social_auth_usersocialauth`.`user_id`,
    `social_auth_usersocialauth`.`created`,
    `social_auth_usersocialauth`.`modified`
FROM `REGISTRATION`.`social_auth_usersocialauth`;

SELECT `users_profile`.`id`,
    `users_profile`.`avatar`,
    `users_profile`.`user_id`,
    `users_profile`.`bio`
FROM `REGISTRATION`.`users_profile`;