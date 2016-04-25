


def test_add_places_calculator(app):
    app.calculator.open_home_page()
    app.calculator.authorisation()
    app.calculator.chose_calculator()
    app.calculator.add_places()
    app.calculator.send_form()


def test_add_events_calculator(app):
    app.calculator.open_home_page()
    app.calculator.authorisation()
    app.calculator.chose_calculator()
    app.calculator.add_events()
    app.calculator.send_form()


def test_add_topovoe_tematichesky(app):
    app.calculator.open_home_page()
    app.calculator.authorisation()
    app.calculator.chose_calculator()
    app.calculator.add_topovoe_tematichesky()
    app.calculator.send_form()

def test_add_topovoe_glavnaya(app):
    app.calculator.open_home_page()
    app.calculator.authorisation()
    app.calculator.chose_calculator()
    app.calculator.add_topovoe_glavnaya()
    app.calculator.send_form()


def test_add_banners(app):
    app.calculator.open_home_page()
    app.calculator.authorisation()
    app.calculator.chose_calculator()
    app.calculator.add_banners()
    app.calculator.send_form()


def test_add_branding(app):
    app.calculator.open_home_page()
    app.calculator.authorisation()
    app.calculator.chose_calculator()
    app.calculator.add_branding()
    app.calculator.send_form()



def test_add_spec_project(app):
    app.calculator.open_home_page()
    app.calculator.authorisation()
    app.calculator.chose_calculator()
    app.calculator.add_spec_project()
    app.calculator.send_form()
