#!/usr/bin/env python3
"""
Fetches the "comets visible today" list from the COBS Comet Observation
Database (https://cobs.si) Planner API and writes a small, clean JSON
snapshot to data/comets.json for the static site to read.

COBS data is licensed CC BY-NC-SA 4.0 - see https://cobs.si/help/data_policy/
Attribution is required and preserved in the output "source" field.

Run by .github/workflows/update-comets.yml on a schedule. Safe to run
locally too: `python3 scripts/update_comets.py`
"""

import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

# loc=106 is the MPC observatory code for Crni Vrh Observatory (COBS's
# home observatory) - this matches the "Comets visible today at Crni Vrh
# Observatory" table shown on the COBS homepage.
API_URL = "https://cobs.si/api/planner.api?loc=106"
OUTPUT_PATH = "data/comets.json"
USER_AGENT = "kavosh-space.github.io (astronomy club site; contact: kavosh.space@gmail.com)"


def fetch_planner_data():
    req = urllib.request.Request(API_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8")
    return json.loads(raw)


def build_snapshot(payload):
    comet_list = payload.get("comet_list", [])
    cleaned = []
    for c in comet_list:
        cleaned.append({
            "type": c.get("comet_type"),
            "name": c.get("comet_name"),
            "fullname": c.get("comet_fullname"),
            "mpc_name": c.get("mpc_name"),
            "magnitude": c.get("magnitude"),
            "constellation": c.get("constelation"),
            "best_time": c.get("best_time"),
            "best_alt": c.get("best_alt"),
            "rise_time": c.get("rise_time"),
            "set_time": c.get("set_time"),
            "sun_elongation": c.get("sun_elongation"),
            "moon_elongation": c.get("moon_elongation"),
            "trend": c.get("trend"),
        })

    # Sort brightest (lowest magnitude number) first.
    cleaned.sort(key=lambda c: (c["magnitude"] is None, c["magnitude"]))

    return {
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "location": payload.get("location", {}),
        "moon_events": payload.get("moon events", {}),
        "comets": cleaned,
        "source": {
            "name": "COBS Comet Observation Database",
            "url": "https://cobs.si/",
            "license": "CC BY-NC-SA 4.0",
            "license_url": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
            "data_policy_url": "https://cobs.si/help/data_policy/",
        },
    }


def main():
    try:
        payload = fetch_planner_data()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        # Don't clobber a good previous snapshot if the API is temporarily down.
        print(f"COBS API request failed: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"COBS API returned invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    snapshot = build_snapshot(payload)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Wrote {len(snapshot['comets'])} comets to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
