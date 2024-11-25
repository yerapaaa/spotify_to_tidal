from typing import TypedDict, Literal, List, Optional


class SpotifyConfig(TypedDict):
    client_id: 02f543ba2d854feebfb3503e3e1f092f
    client_secret: f385474c380b4e078d4bb94a09623e7c
    username: Yerapaaa
    redirect_url: developer.spotify.com


class TidalConfig(TypedDict):
    access_token: str
    refresh_token: str
    session_id: str
    token_type: Literal["Bearer"]


class PlaylistConfig(TypedDict):
    spotify_id: str
    tidal_id: str


class SyncConfig(TypedDict):
    spotify: SpotifyConfig
    sync_playlists: Optional[List[PlaylistConfig]]
    excluded_playlists: Optional[List[str]]
