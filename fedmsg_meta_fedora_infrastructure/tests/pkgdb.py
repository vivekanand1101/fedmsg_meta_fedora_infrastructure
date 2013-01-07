# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>
#
""" Tests for pkgdb messages """

import unittest

from fedmsg.tests.test_meta import Base

"""
Done:

    - acl.update
    - acl.request.toggle
    - owner.update
    - package.retire

Need these, still:

    - acl.user.remove
    - branch.clone
    - package.new
    - package.update
    - critpath.update
"""


class TestPkgdbACLUpdate(Base):
    expected_title = "pkgdb.acl.update (unsigned)"
    expected_subti = "ralph changed ralph's 'watchbugzilla' permission on " + \
        "python-sh (EL-6) to 'Awaiting Review'"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/python-sh"
    expected_icon = "https://apps.fedoraproject.org/packages/images/icons/" + \
        "package_128x128.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set(['python-sh'])
    expected_usernames = set(['ralph', 'grover'])
    expected_objects = set(['python-sh/acls/EL-6/watchbugzilla/ralph'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357576703.125622,
        "topic": "org.fedoraproject.stg.pkgdb.acl.update",
        "msg": {
            "status": "Awaiting Review",
            "username": "ralph",
            "package_listing": {
                "owner": "grover",
                "package": {
                    "upstreamurl": None,
                    "name": "python-sh",
                    "description": None,
                    "reviewurl": None,
                    "summary": "Python module to simplify calling "
                    "shell commands"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            },
            "agent": "ralph",
            "acl": "watchbugzilla"
        }
    }


class TestPkgdbOwnerUpdate(Base):
    expected_title = "pkgdb.owner.update (unsigned)"
    expected_subti = "ralph changed owner of php-zmq (EL-6) to 'orphan'"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = "https://apps.fedoraproject.org/packages/images/icons/" + \
        "package_128x128.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/owner/EL-6'])
    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1357580533.5999,
        "topic": "org.fedoraproject.stg.pkgdb.owner.update",
        "msg": {
            "package_listing": {
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            },
            "agent": "ralph"
        }
    }


class TestPkgdbACLRequestToggle(Base):
    expected_title = "pkgdb.acl.request.toggle (unsigned)"
    expected_subti = "ralph has requested 'commit' on php-zmq (EL-6)"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = "https://apps.fedoraproject.org/packages/images/icons/" + \
        "package_128x128.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/acls/EL-6/commit/ralph'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357581512.006664,
        "topic": "org.fedoraproject.stg.pkgdb.acl.request.toggle",
        "msg": {
            "acl_action": "requested",
            "package_listing": {
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            },
            "acl_status": "Awaiting Review",
            "agent": "ralph",
            "acl": "commit"
        }
    }


class TestPkgdbPackageRetire(Base):
    expected_title = "pkgdb.package.retire (unsigned)"
    expected_subti = "ralph retired php-zmq (EL-6)!"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = "https://apps.fedoraproject.org/packages/images/icons/" + \
        "package_128x128.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/retire'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357583297.886945,
        "topic": "org.fedoraproject.stg.pkgdb.package.retire",
        "msg": {
            "package_listing": {
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            },
            "retirement": "retired",
            "agent": "ralph"
        }
    }



"""
        # Emit an event to the fedmsg bus.
        fedmsg.publish(topic="acl.user.remove", msg=dict(
            package=pkg.api_repr(version=1),
            package_listings=[pl.api_repr(version=1) for pl in package_listings],
            username=username,
            collections=collectn_list,
            agent=identity.current.user_name,
        ))
"""
class TestPkgdbUserRemove(Base):
    expected_title = "pkgdb.acl.user.remove (unsigned)"
    expected_subti = "ralph removed ralph from php-zmq (EL-6, F18)"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = "https://apps.fedoraproject.org/packages/images/icons/" + \
        "package_128x128.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/remove/ralph'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357583297.886945,
        "topic": "org.fedoraproject.stg.pkgdb.acl.user.remove",
        "msg": {
            "package_listings": [{
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            }, {
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora",
                    "publishurltemplate": None,
                    "version": "18",
                    "disttag": ".f18",
                    "branchname": "F18"
                },
                "specfile": None
            }],
            "collections": [
                # This actually has stuff in it in prod.
            ],
            "username": "ralph",
            "agent": "ralph",
        }
    }



if __name__ == '__main__':
    unittest.main()