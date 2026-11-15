"""Build the Part 6 workflow: a Schedule Trigger runs the weather report by itself and appends one CSV line per run.
  workflow/daily-weather-report.json : sanitized (daily 07:00, workflow timezone Asia/Manila, placeholder file path, no credentials)
  python make_p6_workflow.py import <minute|daily:H:M> <ny|manila>   writes runtime/_p6_daily.json (real credential id and path) for the CLI import; used by _p6_apply.sh
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WF_ID, LOGGER_ID = "Wthr06Daily00001", "Err05Logger000001"
CRED = {"ollamaApi": {"id": "JqDW9AG70jtrP5Lx", "name": "Ollama account"}}
PLACEHOLDER_PATH = "C:/Users/YOUR-NAME/.n8n-files/daily-weather.csv"
REAL_PATH = "D:/MIT/n8n-ai-agent-tutorial/runtime/study-files/daily-weather.csv"
FALLBACK_TEXT = "Advice is not available right now (the AI did not answer)."
PROMPT = ("=Weather today in {{ $json.city }}: high {{ $json.max }} degrees Celsius, low {{ $json.min }} degrees Celsius, chance of rain {{ $json.rain }} percent. "
          "Write ONE short sentence of advice for a student who is going out. Use simple English. Use only the numbers given here.")
LINE = ("={{ [$now.setZone('Asia/Manila').toFormat('yyyy-LL-dd HH:mm:ss'), $('Weather facts').item.json.city, $('Weather facts').item.json.max, $('Weather facts').item.json.min, $('Weather facts').item.json.rain, $json.text]"
        ".map(v => '\"' + String(v).replaceAll('\"', '\"\"').replaceAll('\\n', ' ') + '\"').join(',') + '\\n' }}")


def rule(spec):
    if spec == "minute":
        return {"interval": [{"field": "minutes", "minutesInterval": 1}]}
    _, h, m = spec.split(":")
    return {"interval": [{"field": "days", "daysInterval": 1, "triggerAtHour": int(h), "triggerAtMinute": int(m)}]}


def build(spec="daily:7:0", tz="manila", path=PLACEHOLDER_PATH):
    n = lambda i: f"c6000000-0000-4000-8000-{i:012d}"
    nodes = [
        {"parameters": {"rule": rule(spec)}, "id": n(1), "name": "Schedule Trigger", "type": "n8n-nodes-base.scheduleTrigger", "typeVersion": 1.2, "position": [0, 200]},
        {"parameters": {"url": "https://api.open-meteo.com/v1/forecast", "sendQuery": True, "queryParameters": {"parameters": [
            {"name": "latitude", "value": "14.6042"}, {"name": "longitude", "value": "120.9822"},
            {"name": "daily", "value": "temperature_2m_max,temperature_2m_min,precipitation_probability_max"},
            {"name": "forecast_days", "value": "1"}, {"name": "timezone", "value": "Asia/Manila"}]}, "options": {}},
         "id": n(2), "name": "Get weather", "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2, "position": [220, 200], "retryOnFail": True, "maxTries": 3, "waitBetweenTries": 1500},
        {"parameters": {"assignments": {"assignments": [
            {"id": n(11), "name": "city", "value": "Manila", "type": "string"},
            {"id": n(12), "name": "max", "value": "={{ $json.daily.temperature_2m_max[0] }}", "type": "number"},
            {"id": n(13), "name": "min", "value": "={{ $json.daily.temperature_2m_min[0] }}", "type": "number"},
            {"id": n(14), "name": "rain", "value": "={{ $json.daily.precipitation_probability_max[0] }}", "type": "number"}]}, "options": {}},
         "id": n(3), "name": "Weather facts", "type": "n8n-nodes-base.set", "typeVersion": 3.4, "position": [440, 200]},
        {"parameters": {"promptType": "define", "text": PROMPT, "batching": {}}, "id": n(4), "name": "Advice", "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.9,
         "position": [660, 200], "onError": "continueErrorOutput"},
        {"parameters": {"model": "llama3.2:3b", "options": {}}, "id": n(5), "name": "Ollama Chat Model", "type": "@n8n/n8n-nodes-langchain.lmChatOllama", "typeVersion": 1, "position": [680, 420]},
        {"parameters": {"assignments": {"assignments": [{"id": n(15), "name": "text", "value": FALLBACK_TEXT, "type": "string"}]}, "options": {}},
         "id": n(6), "name": "Fallback advice", "type": "n8n-nodes-base.set", "typeVersion": 3.4, "position": [880, 380]},
        {"parameters": {"assignments": {"assignments": [{"id": n(16), "name": "line", "value": LINE, "type": "string"}]}, "options": {}},
         "id": n(7), "name": "Build line", "type": "n8n-nodes-base.set", "typeVersion": 3.5, "position": [1100, 200]},
        {"parameters": {"operation": "toText", "sourceProperty": "line", "options": {}}, "id": n(8), "name": "Convert to File", "type": "n8n-nodes-base.convertToFile", "typeVersion": 1.2, "position": [1320, 200]},
        {"parameters": {"operation": "write", "fileName": path, "options": {"append": True}}, "id": n(9), "name": "Write File to Disk", "type": "n8n-nodes-base.readWriteFile", "typeVersion": 1.1, "position": [1540, 200]},
    ]
    c = lambda a, b, i=0: {"node": b, "type": "main", "index": i}
    conns = {
        "Schedule Trigger": {"main": [[c("", "Get weather")]]},
        "Get weather": {"main": [[c("", "Weather facts")]]},
        "Weather facts": {"main": [[c("", "Advice")]]},
        "Ollama Chat Model": {"ai_languageModel": [[{"node": "Advice", "type": "ai_languageModel", "index": 0}]]},
        "Advice": {"main": [[c("", "Build line")], [c("", "Fallback advice")]]},
        "Fallback advice": {"main": [[c("", "Build line")]]},
        "Build line": {"main": [[c("", "Convert to File")]]},
        "Convert to File": {"main": [[c("", "Write File to Disk")]]},
    }
    settings = {"executionOrder": "v1", "errorWorkflow": LOGGER_ID}
    if tz == "manila":
        settings["timezone"] = "Asia/Manila"
    return {"name": "Daily Weather Report", "nodes": nodes, "connections": conns, "settings": settings}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "import":
        spec, tz = sys.argv[2], sys.argv[3]
        d = build(spec, tz, REAL_PATH)
        for nd in d["nodes"]:
            if nd["type"].endswith("lmChatOllama"):
                nd["credentials"] = CRED
        d["id"] = WF_ID
        (ROOT / "runtime" / "_p6_daily.json").write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
        print("import file written", spec, tz)
    else:
        (ROOT / "workflow" / "daily-weather-report.json").write_text(json.dumps(build(), indent=2, ensure_ascii=False), encoding="utf-8")
        print("sanitized workflow written")
