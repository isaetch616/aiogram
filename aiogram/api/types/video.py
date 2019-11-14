from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .base import TelegramObject

if TYPE_CHECKING:
    from .photo_size import PhotoSize


class Video(TelegramObject):
    """
    This object represents a video file.

    Source: https://core.telegram.org/bots/api#video
    """

    file_id: str
    """Identifier for this file"""
    width: int
    """Video width as defined by sender"""
    height: int
    """Video height as defined by sender"""
    duration: int
    """Duration of the video in seconds as defined by sender"""
    thumb: Optional[PhotoSize] = None
    """Video thumbnail"""
    mime_type: Optional[str] = None
    """Mime type of a file as defined by sender"""
    file_size: Optional[int] = None
    """File size"""