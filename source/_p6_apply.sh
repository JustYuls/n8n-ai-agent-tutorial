#!/bin/bash
# usage: _p6_apply.sh <minute|daily:H:M> <ny|manila> <pub|nopub>   imports the Part 6 workflow, publishes or unpublishes it, and waits for n8n
cd /d/MIT/n8n-ai-agent-tutorial/source && python make_p6_workflow.py import "$1" "$2" >/dev/null || exit 1
cd ../runtime && export N8N_USER_FOLDER="D:/MIT/n8n-ai-agent-tutorial/runtime/n8n-data"
npx n8n import:workflow --input=_p6_daily.json 2>&1 | tail -1
if [ "$3" = "pub" ]; then npx n8n publish:workflow --id=Wthr06Daily00001 2>&1 | tail -1 >/dev/null; else npx n8n unpublish:workflow --id=Wthr06Daily00001 2>&1 | tail -1 >/dev/null; fi
sleep 5
for i in $(seq 1 30); do c=$(curl -s -m 3 -o /dev/null -w "%{http_code}" http://localhost:5678/healthz); [ "$c" = "200" ] && break; sleep 3; done
sleep 8
echo "applied $* at $(date +%H:%M:%S)"
