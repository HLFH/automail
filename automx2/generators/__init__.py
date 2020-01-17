"""
Copyright © 2019-2020 Ralph Seichter

Graciously sponsored by sys4 AG <https://sys4.de/>

This file is part of automx2.

automx2 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

automx2 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with automx2. If not, see <https://www.gnu.org/licenses/>.
"""
from automx2 import IDENTIFIER
from automx2 import LdapLookupError
from automx2.ldap import LdapAccess
from automx2.ldap import LookupResult
from automx2.ldap import STATUS_ERROR
from automx2.model import Ldapserver


def branded_id(id_: str) -> str:
    return f'{IDENTIFIER}-{id_}'


class ConfigGenerator:
    def client_config(self, user_name, domain_name: str, realname: str, password: str) -> str:
        raise NotImplementedError

    @staticmethod
    def _ldap_lookup(email_address: str, server: Ldapserver) -> LookupResult:
        ldap = LdapAccess(server.name, port=server.port, use_ssl=server.use_ssl,
                          user=server.bind_user, password=server.bind_password)
        r = ldap.lookup(server.search_base, server.search_filter.format(email_address),
                        attr_cn=server.attr_cn, attr_uid=server.attr_uid)
        if r.status == STATUS_ERROR:  # pragma: no cover
            raise LdapLookupError('LDAP bind failed')
        return r
