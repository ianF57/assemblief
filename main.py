from __future__ import annotations

import logging
import socket
import threading
import webbrowser

import uvicorn

from app.app_factory import create_app
from app.data.database import initialize_database
from app.logging_setup import configure_logging
from config import settings

logger = logging.getLogger(__name__)
app = create_app()


def find_available_port(start_port: int) -> int:
    """Find the next available TCP port starting at start_port."""
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((settings.app_host, port))
                return port
            except OSError:
                port += 1


def _open_browser(port: int) -> None:
    """Open browser after startup in local runtime."""
    browser_host = settings.app_host if settings.app_host != "0.0.0.0" else "127.0.0.1"
    url = f"http://{browser_host}:{port}/"
    opened = webbrowser.open(url)
    if opened:
        logger.info("Opened browser at %s", url)
    else:
        logger.warning("Could not auto-open browser. Visit %s manually.", url)


if __name__ == "__main__":
    configure_logging(settings.log_level)

    logger.info("Initializing database at %s", settings.db_path)
    initialize_database()

    selected_port = find_available_port(settings.app_port)
    if selected_port != settings.app_port:
        logger.warning("Port %s unavailable, using %s instead.", settings.app_port, selected_port)

    threading.Timer(1.0, _open_browser, args=(selected_port,)).start()
    logger.info("Starting %s on %s:%s", settings.app_name, settings.app_host, selected_port)
    uvicorn.run(app, host=settings.app_host, port=selected_port, log_level=settings.log_level.lower())
