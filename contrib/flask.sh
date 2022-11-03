#!/usr/bin/env bash
# vim:ts=4:sw=4:noet
#
# Launches automua as a Flask application. Execute this script from
# within the parent directory of your Python venv. Example usage:
#
# (1) flask.sh run --port=4243
# Launches application for http://127.0.0.1:4243/ . This is the typical
# production configuration when running behind a proxy server.
#
# (2) flask.sh run --host=somehost.example.com --port=80
# Launches application for http://somehost.example.com/ . This allows
# automua to run without a proxy server.

set -euo pipefail
source .venv/bin/activate

# User configurable section -- START

# If you want to override the paths where automua searches for configuration
# files, set the following environment variable to an absolute path.
#export AUTOMUA_CONF='/path/to/your/automua.conf'

# Set the following to either 'development' or 'production'.
export FLASK_CONFIG='production'

# User configurable section -- END

export FLASK_APP='automua.server:app'
flask "$@"
