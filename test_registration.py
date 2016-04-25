# -*- coding: utf-8 -*-



def test_registr_ok(app):
    app.registration.open_home_page()
    app.registration.push_login_button()
    app.registration.chose_socialbutton_OK()
    app.registration.authorization_OK( email_ok="nervios@mail.ru", password_ok="magaioliveira19")
    app.registration.fill_registration_form(email="jgfjghfk@jgfhgjf1.gf")


def test_registr_twitter(app):
    app.registration.open_home_page()
    app.registration.push_login_button()
    app.registration.chose_socialbutton_twitter()
    app.registration.authorization_twitter(username_twitter="plastmassovaya", password_twitter="magaioliveira19")
    app.registration.fill_registration_form(email="jgfjghfk@jgfhgjf2.gf")

def test_registr_vk(app):
    app.registration.open_home_page()
    app.registration.push_login_button()
    app.registration.chose_socialbutton_vk()
    app.registration.authorization_vk(mailvk="plastmassovaya@gmail.com", passwordvk="dostoevskyfm19")
    app.registration.fill_registration_form(email="jgfjghnnnfk@jgfhgjf3.gf")


def test_registr_fb(app):
    app.registration.open_home_page()
    app.registration.push_login_button()
    app.registration.chose_socialbutton_fb()
    app.registration.authorization_fb(mailfb="nervios_heart@mail.ru", password_fb="magaioliveira19")
    app.registration.fill_registration_form(email="jgfjghfk@jgfhgjf4.gf")


def test_registr_google_plus(app):
    app.registration.open_home_page()
    app.registration.push_login_button()
    app.registration.chose_socialbutton_google_plus()
    app.registration.authorization_google_plus( mailgoogle="plastmassovaya@gmail.com", passwordgoogle="magaioliveira19")
    app.registration.fill_registration_form(email="jgfjghfk@jgfhgjf5.gf")

def test_registr_email(app):
    app.registration.open_home_page()
    app.registration.push_login_button()
    app.registration.chose_emailreg()
    app.registration.fill_regform_email(displayname="test", email="test@test.testtest", password="fkmnfdbcnf",
                                password2="fkmnfdbcnf")
