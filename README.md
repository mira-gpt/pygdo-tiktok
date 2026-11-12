# PyGDO TikTok

Early skeleton for a TikTok LIVE connector. It does not connect, create users,
send messages, or start a stream yet. Installing the skeleton only provides a
creator-handle setting; it registers no connector or server.

## Planned incoming chat

- Use the third-party [TikTokLive Python library](https://github.com/isaackogan/TikTokLive)
  to receive LIVE comments. Its README describes an external Euler Stream
  signing service and community rate limits. Review what data is sent, the
  modified AGPL license, version compatibility and TikTok's terms before use.
- Map a stable platform user identifier to a server-scoped PyGDO user and the
  room to a channel; update display names separately. Treat comments as
  untrusted and do not grant permissions or assume platform authentication.
- Integrate reconnect and shutdown with Dog, handle duplicate events, and test
  using fixtures before connecting to a consenting live broadcast.

## Sending to LIVE chat: research

TikTokLive's documentation presents event reception, but does not document a
current supported Python method for sending LIVE comments. The third-party
[tiktok_live_connector](https://github.com/thebubble7/tiktok_live_connector)
describes sending with a session ID; this is unofficial, credential-sensitive,
and not verified here. An older [TikTokLive issue](https://github.com/isaackogan/TikTokLive/issues/88)
reports that sending did not work in some cases; it is not evidence of current
behavior. No official public LIVE-comment send endpoint was established in this
research. Check current official access, permissions, terms and alternatives
before selecting or implementing an outbound transport. Never log credentials.

## Video

Reuse the existing PyGDO virtual camera where supported; TikTok-specific LIVE
streaming requirements, platform support and account eligibility still need
verification. This module must not start a camera or broadcast automatically.
