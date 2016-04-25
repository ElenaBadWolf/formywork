

def test_add_event_admin(app):
    app.add_event_admin.login_admin()
    app.add_event_admin.chose_event()
    app.add_event_admin.click_add_event()
    app.add_event_admin.fill_form_event()
    app.add_event_admin.have_alook_onsite()