#!/bin/bash
# entrypoint.sh

set -e

alembic upgrade head


exec "$@"
