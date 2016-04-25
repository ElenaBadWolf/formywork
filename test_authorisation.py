# -*- coding: utf-8 -*-
#use after registration

def test_authorisation_use_OK(app):
    app.authorisation.authorisation_use_OK()



def test_authorisation_use_twitter(app):
    app.authorisation.authorisation_use_twitter()


def test_authorisation_use_VK(app):
    app.authorisation.authorisation_use_VK()


def test_authorisation_use_FB(app):
    app.authorisation.authorisation_use_FB()


def test_authorisation_use_google(app):
    app.authorisation.authorisation_use_google()


def test_authorisation_use_email(app):
    app.authorisation.authorisation_use_email()