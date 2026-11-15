"""Build the Part 5 workflow files from the Part 4 workflow.
  workflow/weather-webhook-safe.json  : Part 4 + Advice fallback (On Error: Continue using error output) + an error workflow setting
  workflow/error-logger.json          : Error Trigger -> one CSV line per failure -> append to errors-log.csv
Usage:  python make_p5_workflows.py                      (writes the two sanitized files)
        python make_p5_workflows.py import [model] [url|-] [unsafe] [noerr] (writes runtime/_p5_*.json with the real credential id and path; for the CLI import)
"""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAFE_ID, LOGGER_ID = "Wthr05Safe000001", "Err05Logger000001"
CRED = {"ollamaApi": {"id": "JqDW9AG70jtrP5Lx", "name": "Ollama account"}}
PLACEHOLDER_PATH = "C:/Users/YOUR-NAME/.n8n-files/errors-log.csv"
REAL_PATH = "D:/MIT/n8n-ai-agent-tutorial/runtime/study-files/errors-log.csv"
FALLBACK_TEXT = "Advice is not available right now (the AI did not answer)."


def safe(model="llama3.2:3b", forecast_url=None, with_error_setting=True):
    d = json.load(open(ROOT / "workflow" / "weather-webhook.json", encoding="utf-8"))
    d["name"] = "Weather Webhook (safe)"
    for n in d["nodes"]:
        if n["name"] == "Webhook":
            n["parameters"]["path"] = "weather-safe"
            n["webhookId"] = "b7c1f0de-4a52-4c8e-9a10-0a5f4f3e7a05"
        if n["name"] == "Advice":
            n["onError"] = "continueErrorOutput"
            n["position"] = [1100, 100]
        if n["name"] == "Ollama Chat Model":
            n["parameters"]["model"] = model
        if n["name"] == "Get weather" and forecast_url:
            n["parameters"]["url"] = forecast_url
    d["nodes"].append({
        "parameters": {"assignments": {"assignments": [
            {"id": "e5000000-0000-4000-8000-000000000001", "name": "text", "value": FALLBACK_TEXT, "type": "string"}]}, "options": {}},
        "id": "a1000000-0000-4000-8000-000000000010", "name": "Fallback advice", "type": "n8n-nodes-base.set", "typeVersion": 3.4, "position": [1320, 300]})
    d["connections"]["Advice"] = {"main": [[{"node": "Reply", "type": "main", "index": 0}], [{"node": "Fallback advice", "type": "main", "index": 0}]]}
    d["connections"]["Fallback advice"] = {"main": [[{"node": "Reply", "type": "main", "index": 0}]]}
    d["settings"] = {"executionOrder": "v1"}
    if with_error_setting:
        d["settings"]["errorWorkflow"] = LOGGER_ID
    return d


def logger(path):
    line = ("={{ [$now.setZone('Asia/Manila').toFormat('yyyy-LL-dd HH:mm:ss'), $json.workflow.name, $json.execution.lastNodeExecuted, $json.execution.error.message]"
            ".map(v => '\"' + String(v).replaceAll('\"', '\"\"').replaceAll('\\n', ' ') + '\"').join(',') + '\\n' }}")
    return {
        "name": "Error logger",
        "nodes": [
            {"parameters": {}, "id": "b2000000-0000-4000-8000-000000000001", "name": "Error Trigger", "type": "n8n-nodes-base.errorTrigger", "typeVersion": 1, "position": [0, 200]},
            {"parameters": {"assignments": {"assignments": [{"id": "b2000000-0000-4000-8000-000000000002", "name": "line", "value": line, "type": "string"}]}, "options": {}},
             "id": "b2000000-0000-4000-8000-000000000003", "name": "Build line", "type": "n8n-nodes-base.set", "typeVersion": 3.5, "position": [220, 200]},
            {"parameters": {"operation": "toText", "sourceProperty": "line", "options": {}},
             "id": "b2000000-0000-4000-8000-000000000004", "name": "Convert to File", "type": "n8n-nodes-base.convertToFile", "typeVersion": 1.2, "position": [440, 200]},
            {"parameters": {"operation": "write", "fileName": path, "options": {"append": True}},
             "id": "b2000000-0000-4000-8000-000000000005", "name": "Write File to Disk", "type": "n8n-nodes-base.readWriteFile", "typeVersion": 1.1, "position": [660, 200]},
        ],
        "connections": {"Error Trigger": {"main": [[{"node": "Build line", "type": "main", "index": 0}]]},
                        "Build line": {"main": [[{"node": "Convert to File", "type": "main", "index": 0}]]},
                        "Convert to File": {"main": [[{"node": "Write File to Disk", "type": "main", "index": 0}]]}},
        "settings": {"executionOrder": "v1"},
    }


def dump(d, p):
    Path(p).write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "import":
        model = sys.argv[2] if len(sys.argv) > 2 else "llama3.2:3b"
        url = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] != "-" else None
        flags = sys.argv[4:]
        s = safe(model, url, with_error_setting="noerr" not in flags)
        if "unsafe" in flags:  # Part 4 behavior: no error output on Advice, no fallback
            for n in s["nodes"]:
                n.pop("onError", None)
            s["nodes"] = [n for n in s["nodes"] if n["name"] != "Fallback advice"]
            s["connections"].pop("Fallback advice", None)
            s["connections"]["Advice"] = {"main": [[{"node": "Reply", "type": "main", "index": 0}]]}
        for n in s["nodes"]:
            if n["type"].endswith("lmChatOllama"):
                n["credentials"] = CRED
        s["id"] = SAFE_ID
        lg = logger(REAL_PATH)
        lg["id"] = LOGGER_ID
        dump(s, ROOT / "runtime" / "_p5_safe.json")
        dump(lg, ROOT / "runtime" / "_p5_logger.json")
        print("import files written", model, url)
    else:
        dump(safe(), ROOT / "workflow" / "weather-webhook-safe.json")
        dump(logger(PLACEHOLDER_PATH), ROOT / "workflow" / "error-logger.json")
        print("sanitized workflow files written")
