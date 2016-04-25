

def test_add_event_of_theday(app):
    app.add_event_admin.login_admin()
    app.add_event_of_theday.add_event_of_theday()
