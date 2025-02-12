USER_DATA = {
"email": "test-user-kovalev-a@yandex.ru",
"password": "password",
"name": "Testname"
}

DATA_WITH_1_EMPTY_PARAM = [{
"email": "test-user-kovalev-artem1@yandex.ru",
"password": "password"
}, {
"email": "test-user-kovalev-artem1@yandex.ru",
"name": "Testname"
}, {
"password": "password",
"name": "Testname"
}]

WRONG_LOGIN_DATA = [{"email": "test-user-kovalev-artem1@yandex.ru", "password": "password1111"}, {"email": "test-wronguser-kovalev@yandex.ru", "password": "password1111"}]
PATCH_DATA = [{"email": "test-user-kovalev-artem1234@yandex.ru"},{"name": "Toni Kark"}]