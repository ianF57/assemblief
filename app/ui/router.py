from __future__ import annotations

from datetime import datetime, UTC

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/ui/templates")


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request) -> HTMLResponse:
    """Render the default institutional dashboard page."""
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "title": "Assemblief | Dashboard",
            "generated_at": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%SZ"),
        },
    )
