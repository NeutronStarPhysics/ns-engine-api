from pyctuator.pyctuator import Pyctuator

def setup_actuator(app):
  example_app_address = "localhost"
  example_sba_address = "localhost"
  registration_url = "http://localhost:8080/instances"

  pyctuator = Pyctuator(
      app,
      app.title,
      app_url=f"http://{example_app_address}:8000",
      pyctuator_endpoint_url=f"http://{example_app_address}:8000/pyctuator",
      registration_url=registration_url,
      app_description=app.description,
  )
