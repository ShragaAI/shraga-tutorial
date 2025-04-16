import os

import uvicorn

from shraga_common.app import get_config, setup_app
from shraga_common.flows.demo import flows

config_path = os.getenv("CONFIG_PATH", "config.demo.yaml")
app = setup_app(config_path, flows)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=os.environ.get("PORT") or get_config("server.port") or 8000,
        reload=bool(os.environ.get("ENABLE_RELOAD", False)),
        log_config=None,
        server_header=False,
    )
