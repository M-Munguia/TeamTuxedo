import Config

config :plausible, PlausibleWeb.Endpoint,
  url: [host: "localhost", port: 8000, scheme: "http"],
  check_origin: [
    "//localhost:8000",
    "//127.0.0.1:8000"
  ]