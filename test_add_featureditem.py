

def test_add_featureditem_place(app):
    app.add_event_admin.login_admin()
    app.add_featureditem.add_featureditem_place()
    app.add_event_admin.have_alook_onsite()


def test_add_featureditem_event(app):
    app.add_event_admin.login_admin()
    app.add_featureditem.add_featureditem_event()
    app.add_event_admin.have_alook_onsite()


def test_add_featureditem_news(app) :
    app.add_event_admin.login_admin()
    app.add_featureditem.add_featureditem_news()
    app.add_event_admin.have_alook_onsite()



def test_add_featureditem_list(app):
    app.add_event_admin.login_admin()
    app.add_featureditem.add_featureditem_list()
    app.add_event_admin.have_alook_onsite()


def test_add_featureditem_movie(app):
    app.add_event_admin.login_admin()
    app.add_featureditem.add_featureditem_movie()
    app.add_event_admin.have_alook_onsite()


def test_add_featureditem_incontent(app):
    app.add_event_admin.login_admin()
    app.add_featureditem.add_featureditem_incontent()
    app.add_event_admin.have_alook_onsite()
