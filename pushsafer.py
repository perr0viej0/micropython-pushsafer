"""
MicroPython Pushsafer implementation.
Forked from https://github.com/appzer/python-pushsafer
(Copyright (C) 2018  Kevin Siml <info@appzer.de>)

MicroPython port rewritted by APose (https://guthub/perr0viej0)
email: alexposer@gmail.com

USAGE: exactly the same way in python-pushsafer. Using pushsafer in
micropython is now painless.


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import urequests

__all__ = ["init", "Client", "MessageRequest", "InitError"]

MESSAGE_URL = "https://www.pushsafer.com/api"


class PushSaferError(Exception):
    pass


class MessageSendError(PushSaferError):
    pass


class Client:
    ENDPOINT = "https://www.pushsafer.com/api"

    def __init__(self, privatekey):
        self._key = privatekey

    def send_message(
        self,
        message,
        title=None,
        device=None,
        icon=None,
        sound=None,
        vibration=None,
        url=None,
        urltitle=None,
        time2live=None,
        priority=None,
        retry=None,
        expire=None,
        answer=None,
        picture1=None,
        picture2=None,
        picture3=None,
    ):
        payload = {
            "m": message,
            "d": device,
            "i": icon,
            "s": sound,
            "v": vibration,
            "t": title,
            "u": url,
            "ut": urltitle,
            "l": time2live,
            "pr": priority,
            "re": retry,
            "ex": expire,
            "a": answer,
            "p": picture1,
            "p2": picture2,
            "p3": picture3,
            "k": self._key,
        }
        return self._send(payload)

    def _send(self, payload: dict):
        payload = {k: v for k, v in payload.items() if v}
        payload['m'] = payload['m'].replace(" ", "+")
        payload['t'] = payload['t'].replace(" ", "+")
        st = "?"
        for cosas,valores in payload.items():
            st = st +"&" + cosas + "=" + valores
        r = urequests.post(f"{self.ENDPOINT}{st}")
        if r.status_code != 200:
            raise MessageSendError(f"Failed to send message, got {r.json()}")
        else:
            return r.json()
