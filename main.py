from app import App
from tests.tests import Tests

tests = Tests()
tests.run_all_tests()
app = App()
ui = app.start_app()
