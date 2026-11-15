#!/bin/bash
# usage: _p5_apply.sh <model> <url|-> [flags...]   imports + publishes the Part 5 workflows and waits for n8n
cd /d/MIT/n8n-ai-agent-tutorial/source && python make_p5_workflows.py import "$@" >/dev/null || exit 1
cd ../runtime && export N8N_USER_FOLDER="D:/MIT/n8n-ai-agent-tutorial/runtime/n8n-data"
npx n8n import:workflow --input=_p5_logger.json 2>&1 | tail -1
npx n8n import:workflow --input=_p5_safe.json 2>&1 | tail -1
npx n8n publish:workflow --id=Err05Logger000001 2>&1 | tail -1 >/dev/null
npx n8n publish:workflow --id=Wthr05Safe000001 2>&1 | tail -1 >/dev/null
sleep 5
for i in $(seq 1 30); do c=$(curl -s -m 3 -o /dev/null -w "%{http_code}" http://localhost:5678/healthz); [ "$c" = "200" ] && break; sleep 3; done
sleep 10
echo applied "$@"
