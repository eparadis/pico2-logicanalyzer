#!/usr/bin/env bash

set -euo pipefail

app_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
venv_dir="${app_dir}/.venv"
python_bin="${venv_dir}/bin/python"
pico_la_bin="${venv_dir}/bin/pico-la"
web_host="${PICO_LA_WEB_HOST:-127.0.0.1}"
web_port="${PICO_LA_WEB_PORT:-4173}"
ssh_user="${PICO_LA_SSH_USER:-$(id -un)}"

if [[ -n "${PICO_LA_SSH_HOST:-}" ]]; then
  ssh_host="${PICO_LA_SSH_HOST}"
elif command -v scutil >/dev/null 2>&1; then
  ssh_host="$(scutil --get LocalHostName 2>/dev/null || hostname)"
  ssh_host="${ssh_host}.local"
else
  ssh_host="$(hostname)"
fi

if [[ ! -x "${python_bin}" ]]; then
  python_source="$(command -v python3.12 || true)"
  if [[ -z "${python_source}" ]]; then
    echo "error: python3.12 is required but was not found" >&2
    exit 1
  fi

  echo "Creating Python environment..."
  "${python_source}" -m venv "${venv_dir}"
fi

if [[ ! -x "${pico_la_bin}" ]] || ! "${python_bin}" -c 'import aiohttp' 2>/dev/null; then
  echo "Installing the reviewed pico-la web environment..."
  "${python_bin}" -m pip install \
    --require-hashes \
    -r "${app_dir}/requirements-web.lock"
  "${python_bin}" -m pip install \
    --no-build-isolation \
    --no-deps \
    -e "${app_dir}[web]"
fi

device_port="$({ "${pico_la_bin}" devices --json; } | "${python_bin}" -c '
import json
import sys

devices = json.load(sys.stdin).get("devices", [])
if len(devices) != 1:
    print(
        f"error: expected exactly one Pico logic analyzer; found {len(devices)}",
        file=sys.stderr,
    )
    raise SystemExit(1)
print(devices[0]["device"])
')"

echo "Starting pico-la with the single discovered analyzer."
echo "On this Mac, open http://${web_host}:${web_port} in your browser."
echo
echo "From another computer, first open an SSH tunnel:"
echo "  ssh -N -L ${web_port}:${web_host}:${web_port} ${ssh_user}@${ssh_host}"
echo "Then open http://127.0.0.1:${web_port} on that computer."
echo "The Mac must have Remote Login enabled for SSH access."
echo
echo "Press Ctrl-C to stop the server."

exec "${pico_la_bin}" web \
  --host "${web_host}" \
  --port "${web_port}" \
  --device-port "${device_port}"
