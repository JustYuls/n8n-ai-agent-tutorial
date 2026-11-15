"""Scene list for Part 4: "n8n Webhook Tutorial for Beginners: Call Any API (Tagalog)".
Real captures: n8n 2.47.5 in Chrome (source/shots_part4 p01-p17, 1037x649) and real terminal outputs saved in source/shots_part4/t00-t06 (text copied from the real runs).
Highlight boxes are in screenshot pixel coordinates (x0, y0, x1, y1). Narration is Tagalog with English technical terms, one Filipino voice (synthetic).
Avoid dots inside words in say (the subtitle splitter cuts at dots): write "curl dot exe", not curl.exe; no file extensions.
"""
NAME = "04_n8n-webhook-api-tagalog"
SYSTEM_MESSAGE = ""
MIXED = False

T_GB = "Git Bash"
T_PS = "Windows PowerShell"

SCENES = [
    # ------------------------------------------------------------ 1. proof hook
    dict(kind="terminal", chapter="Demo: isang tawag, may sagot", step="RESULTA", title=T_PS, note="Totoong output",
         lines=[("cmd", "curl.exe -X POST http://localhost:5678/webhook/weather `"),
                ("out", '>>   -H "Content-Type: application/json" `'),
                ("out", ">>   -d '{\\\"city\\\":\\\"Manila\\\"}'"),
                ("out", '{"city":"Manila","temp":28.1,"humidity":68,"advice":'),
                ("out", '"\\"Stay in the shade and wear light clothes to beat the'),
                ("out", 'heat of 28.1 degrees.\\""}'),
                ("ok", "HTTP 200  5.858s")],
         say="Tingnan mo ito. Sa PowerShell, isang command lang ang tinype ko, at ang pangalan ng lungsod ay Manila. Pagkalipas ng halos anim na segundo, bumalik ang totoong temperatura, 28.1 degrees, ang humidity na 68 percent, at isang linya ng payo mula sa AI. "
             "Walang chat, at walang click. Isang tawag lang. Sa video na ito, gagawin natin ang workflow na iyan, at ipapakita ko rin ang mga totoong pagkakamali ko."),
    # ------------------------------------------------------------ 2. setup
    dict(kind="slide", chapter="Ano ang webhook at API", slide="p4_idea", step="SETUP",
         say="Ano ang webhook? Isa itong address na naghihintay ng tawag. Kapag may tumawag, tatakbo ang workflow mo. Parang doorbell: may pumindot, may sasagot. "
             "At ang API ay parang bintana ng ibang serbisyo. Tatawagin natin ang Open-Meteo, isang libreng weather API na walang account at walang API key."),
    dict(kind="slide", slide="p4_needs", step="SETUP",
         say="Ang kailangan mo ay n8n at Ollama na tumatakbo, galing sa Part 1. Ang PowerShell sa Windows 11, na may kasamang curl dot exe. At ang Open-Meteo, na libre. "
             "Nasa description ang workflow file, kaya pwede mo itong i-import."),
    dict(kind="slide", slide="p4_plan", step="SETUP",
         say="Ito ang plano. Una, ang Webhook, na tumatanggap ng pangalan ng lungsod. Pangalawa, ang HTTP Request na naghahanap sa lungsod. Pangatlo, isa pang HTTP Request para sa temperatura at humidity. "
             "Pang-apat, ang AI na susulat ng isang payo. At panghuli, ang Respond to Webhook, na magbabalik ng sagot. Mayroon ding isang daan para sa maling pangalan ng lungsod."),
    # ------------------------------------------------------------ 3. the workflow
    dict(kind="shot", chapter="Ang workflow at ang Webhook node", img="p01_canvas", step="ANG WORKFLOW", hl=[(125, 314, 177, 366), (903, 251, 955, 304), (483, 375, 535, 427)],
         note=["Webhook: dito nagsisimula", "Reply: dito nagtatapos", "City not found: maling pangalan"],
         say="Ito ang buong workflow. Sa kaliwa ang Webhook, at sa kanan ang Reply. Sa gitna ang Find city, City found, Get weather, Weather facts, at ang Advice na may Ollama Chat Model. "
             "Sa ibaba, ang City not found, para sa maling pangalan ng lungsod."),
    dict(kind="shot", img="p02_webhook-test-url", step="WEBHOOK NODE", hl=[(341, 150, 533, 182), (326, 270, 697, 302), (326, 340, 697, 370)], note=["Test URL", "Method: POST", "Path: weather"],
         say="Buksan natin ang Webhook node. Ang method ay POST, at ang path ay weather. May dalawang address ang webhook. Ang Test URL ay nagtatapos sa webhook dash test slash weather, at pang-test lang ito habang binubuo mo ang workflow."),
    dict(kind="shot", img="p03_webhook-prod-url", step="WEBHOOK NODE", hl=[(341, 193, 698, 221), (326, 478, 697, 506)], note=["Production URL: walang test", "Respond: Using Respond to Webhook Node"],
         say="Ang Production URL naman ay webhook slash weather, walang test. Tandaan ang pagkakaiba nila, dahil dito tayo magkakamali. Pansinin din ang Respond: naka-set ito sa Using Respond to Webhook Node, kaya ang huling node ang magbibigay ng sagot."),
    # ------------------------------------------------------------ 4. mistakes with the test URL
    dict(kind="shot", chapter="Pagkakamali: ang Test URL", img="p04_listening", step="COMMON MISTAKE #1", hl=[(78, 100, 256, 280), (40, 373, 292, 413)], note=["Listening for test event", "Make a POST request to"],
         say="Unang pagkakamali. Nag-click ako ng Listen for test event sa mismong Webhook node, at tumawag ako gamit ang curl."),
    dict(kind="terminal", step="COMMON MISTAKE #1", title=T_GB, note="Totoong output",
         lines=[("cmd", 'curl -s -w "\\nHTTP %{http_code}" -X POST \\'),
                ("out", "  http://localhost:5678/webhook-test/weather \\"),
                ("out", "  -H \"Content-Type: application/json\" -d '{\"city\":\"Manila\"}'"),
                ("note", "(walang laman ang sagot)"), ("ok", "HTTP 200  0.248s")],
         say="Walang laman ang sagot! HTTP 200 ang lumabas, pero walang resulta, at 0.25 segundo lang."),
    dict(kind="shot", img="p05_webhook-output", step="COMMON MISTAKE #1", hl=[(765, 425, 1000, 455), (765, 513, 1000, 535)], note=["body: city Manila", "executionMode: test"],
         say="Sa screen, dumating naman ang data: ang body ay may city na Manila. Pero isang node lang ang tumakbo, ang Webhook. Ang Listen sa loob ng node ay pang-test ng node na iyon lang."),
    dict(kind="terminal", step="COMMON MISTAKE #2", title=T_GB, note="Totoong output",
         lines=[("cmd", 'curl -s -w "\\nHTTP %{http_code}" -X POST \\'),
                ("out", "  http://localhost:5678/webhook-test/weather \\"),
                ("out", "  -H \"Content-Type: application/json\" -d '{\"city\":\"Manila\"}'"),
                ("out", '{"code":404,'),
                ("out", '"message":"The requested webhook \\"weather\\" is not registered.",'),
                ("out", '"hint":"Click the \'Execute workflow\' button on the canvas,'),
                ("out", "then try again. (In test mode, the webhook only works for"),
                ("out", 'one call after you click this button)", ...}'),
                ("ok", "HTTP 404")],
         say="Pangalawang pagkakamali: tinawag ko ulit ang Test URL. Error na: 404, the requested webhook weather is not registered. Sabi ng hint, i-click ang Execute workflow sa canvas, at subukan ulit. "
             "Sa test mode, isang tawag lang ang gumagana pagkatapos mong mag-click."),
    dict(kind="shot", chapter="Ang ayos: Execute workflow", img="p06_canvas-waiting", step="AYOS", hl=[(88, 294, 214, 310), (122, 309, 181, 369)], note=["Waiting for you to call the Test URL", "Ang buong workflow ang naghihintay"],
         say="Ang ayos: i-click ang Execute workflow sa canvas, hindi sa loob ng node. Naghihintay na ngayon ang buong workflow. Nakasulat pa nga: Waiting for you to call the Test URL."),
    dict(kind="shot", chapter="Retry On Fail: kapag nag-timeout ang API", img="p07_find-city-timeout", step="COMMON MISTAKE #3", hl=[(244, 312, 301, 369), (691, 480, 1021, 600)], note=["Pumula ang Find city", "The connection timed out"],
         say="Tumawag ako, at pumula ang Find city. The connection timed out. Totoong nangyari ito habang nire-record ko. Mabagal ang geocoding API noong oras na iyon, at nag-error ang buong workflow pagkalipas ng halos 22 segundo."),
    dict(kind="shot", img="p14_retry", step="AYOS", hl=[(325, 248, 441, 274), (326, 314, 697, 342), (326, 380, 697, 408)], note=["Retry On Fail: naka-on", "Max Tries: 3", "Maghihintay ng 1500 ms"],
         say="Ang ayos ay nasa Settings ng node: Retry On Fail. Ang Max Tries ay 3, at maghihintay ito ng 1500 milliseconds bago ulitin. Nilagay ko ito sa Find city at sa Get weather, ang dalawang tawag sa labas. Hindi nito ginagarantiya na laging gagana, pero mas malaki ang tsansa."),
    dict(kind="shot", img="p08_canvas-success", step="TEST 1", hl=[(125, 314, 177, 366), (903, 251, 955, 304), (691, 549, 1021, 602)], note=["Berde ang bawat node", "1 item sa bawat linya", "Workflow executed successfully"],
         say="Subukan ulit. Berde na ang lahat ng node, at may isang item sa bawat linya. Workflow executed successfully. Ang daan ng True ang tumakbo, hindi ang City not found."),
    dict(kind="pause", chapter="Pause and try", step="TRY IT", pause_q="Gawin sa sarili mong screen:", pause_a=["I-import ang weather webhook workflow", "I-click ang Execute workflow", "Tumawag sa Test URL gamit ang curl"], seconds=8,
         say="Pause and try. Sa sarili mong screen, i-import ang workflow file, i-click ang Execute workflow, at tumawag sa Test URL gamit ang curl. May walong segundo ka."),
    # ------------------------------------------------------------ 5. the nodes
    dict(kind="shot", chapter="Ang mga node: API, Edit Fields at AI", img="p09_find-city", step="FIND CITY", hl=[(325, 250, 697, 282), (326, 478, 697, 600), (812, 315, 1000, 372)], note=["GET sa geocoding API", "name at count", "Resulta: Manila, latitude, longitude"],
         say="Tingnan natin ang dalawang HTTP Request. Ang Find city ay GET sa geocoding API ng Open-Meteo. Ang query parameters ay name, na galing sa body ng webhook, at count na 1. Ang resulta sa kanan ay Manila, kasama ang latitude at longitude."),
    dict(kind="shot", img="p10_get-weather", step="GET WEATHER", hl=[(325, 250, 697, 282), (326, 478, 697, 600)], note=["GET sa forecast API", "latitude at longitude mula sa Find city"],
         say="Ang Get weather naman ay GET sa forecast API. Ipinapasa natin ang latitude at longitude mula sa Find city, at hinihingi natin ang temperature at relative humidity. Ang sagot ay may seksyong current, na may totoong halaga."),
    dict(kind="shot", img="p11_weather-facts", step="WEATHER FACTS", hl=[(350, 240, 693, 365), (740, 140, 1000, 230)], note=["Edit Fields: pinipili ang kailangan", "city, temp, humidity"],
         say="Ang Edit Fields na pinangalanang Weather facts ay pumipili lang ng kailangan: city, temp, at humidity. Ang temp dito ay 28.1, at ang humidity ay 68. Ito ang mga numerong ibibigay natin sa AI, para hindi ito mag-imbento."),
    dict(kind="shot", img="p12_advice", step="ADVICE", hl=[(325, 258, 697, 372), (740, 140, 1005, 175)], note=["Prompt: ang totoong numero", "Sagot ng model"],
         say="Sa Advice node, ang prompt ay ang panahon ngayon sa lungsod, ang temp at humidity, at isang maikling payo lang sa simpleng English. Kasama ang utos na gamitin lang ang mga numerong ibinigay. "
             "Ang sagot ng model: Bring an umbrella to cover you from the rain. Pero walang ulan sa datos natin! Totoo ang numero, pero opinyon lang ng maliit na model ang payo."),
    dict(kind="shot", img="p13_reply", step="REPLY", hl=[(325, 335, 712, 425)], note=["Response body: city, temp, humidity, advice"],
         say="Ang huling node ay ang Respond to Webhook. Ang response body ay isang object: city, temp, humidity, at advice. Ito ang babalik sa tumawag."),
    # ------------------------------------------------------------ 6. publish
    dict(kind="terminal", chapter="Publish: ang Production URL", step="COMMON MISTAKE #4", title=T_GB, note="Totoong output",
         lines=[("cmd", "curl -s -X POST http://localhost:5678/webhook/weather \\"),
                ("out", "  -H \"Content-Type: application/json\" -d '{\"city\":\"Manila\"}'"),
                ("out", '{"code":404,'),
                ("out", '"message":"The requested webhook \\"POST weather\\" is not registered.",'),
                ("out", '"hint":"The workflow must be active for a production URL to run'),
                ("out", "successfully. You can activate the workflow using the toggle in"),
                ("out", 'the top-right of the editor. ..."}'),
                ("ok", "HTTP 404")],
         say="Ngayon, ang Production URL. Bago ako nag-Publish, sinubukan ko ito, at 404 ang sagot: the requested webhook POST weather is not registered. Sabi ng hint, i-activate ang workflow gamit ang toggle sa taas. "
             "Pero sa bersyong ito ng n8n, ang button ay Publish na."),
    dict(kind="shot", img="p15_publish-dialog", step="AYOS", hl=[(293, 228, 744, 266), (671, 458, 744, 490)], note=["Pangalan ng version", "I-click ang Publish"],
         say="Binigyan ng pangalan ang version, at nag-click ako ng Publish."),
    dict(kind="shot", img="p16_published", step="AYOS", hl=[(879, 16, 1017, 48), (289, 210, 748, 440)], note=["Published", "Pwede nang tumawag sa production URL"],
         say="Workflow published. Pwede ka nang tumawag sa production webhook URL. Pansinin na hindi na lumalabas sa canvas ang mga tawag na ito. Nasa Executions list na sila."),
    # ------------------------------------------------------------ 7. PowerShell
    dict(kind="terminal", chapter="Pagkakamali sa PowerShell", step="COMMON MISTAKE #5", title=T_PS, note="Totoong output",
         lines=[("cmd", "curl.exe -X POST http://localhost:5678/webhook/weather `"),
                ("out", '>>   -H "Content-Type: application/json" `'),
                ("out", ">>   -d '{\"city\":\"Manila\"}'"),
                ("out", '{"code":422,'),
                ("out", '"message":"Failed to parse request body",'),
                ("out", '"hint":"Expected property name or \'}\' in JSON at position 1'),
                ("out", '(line 1 column 2)", ...}'),
                ("ok", "HTTP 422")],
         say="Sa PowerShell, may isa pang problema. Tinype ko ang JSON na may mga quotes, at 422 ang sagot: Failed to parse request body. Expected property name or curly bracket at position 1. Nawala ang mga quotes sa loob ng JSON."),
    dict(kind="terminal", step="AYOS", title=T_PS, note="Totoong output",
         lines=[("cmd", "curl.exe -X POST http://localhost:5678/webhook/weather `"),
                ("out", '>>   -H "Content-Type: application/json" `'),
                ("out", ">>   -d '{\\\"city\\\":\\\"Manila\\\"}'"),
                ("note", "Backslash bago ang bawat quote sa loob ng JSON"),
                ("out", '{"city":"Manila","temp":28.1,"humidity":68,"advice": ...}'),
                ("ok", "HTTP 200  5.858s")],
         say="Ang ayos: lagyan ng backslash ang bawat quote sa loob ng JSON. Ngayon, 200 na ang sagot, at kumpleto ang resulta."),
    # ------------------------------------------------------------ 8. verification
    dict(kind="terminal", chapter="Verification: Manila, Cebu at maling lungsod", step="TEST 2", title=T_GB, note="Production URL",
         lines=[("out", "== Manila =="),
                ("out", '{"city":"Manila","temp":28.1,"humidity":68,'),
                ("out", ' "advice":"Bring a hat and wear light clothes to stay cool outside."}'),
                ("ok", "HTTP 200  19.199s"),
                ("out", "== Cebu =="),
                ("out", '{"city":"Cebu","temp":23.5,"humidity":90,'),
                ("out", ' "advice":"Wear light clothes and bring a hat to protect you ..."}'),
                ("ok", "HTTP 200  7.884s")],
         say="Verification. Pagkatapos mag-Publish, tumawag ako sa Production URL. Manila: 28.1 degrees at 68 percent. Cebu: 23.5 at 90 percent. Ang una ay inabot ng 19 segundo, at ang Cebu ay 7.9 segundo. Magkakaiba ang oras, depende sa API at sa model."),
    dict(kind="terminal", step="TEST 3", title=T_GB, note="Maling pangalan",
         lines=[("cmd", "curl -s -X POST http://localhost:5678/webhook/weather \\"),
                ("out", "  -H \"Content-Type: application/json\" -d '{\"city\":\"Zzqxyw\"}'"),
                ("out", '{"error":"City not found",'),
                ("out", ' "tip":"Check the spelling of the city."}'),
                ("ok", "HTTP 404  1.160s")],
         say="Ngayon, ang maling pangalan ng lungsod: Zzqxyw. Bumalik ang 404 na may City not found, sa loob ng 1.2 segundo. Hindi nag-crash ang workflow. Ang daan ng False ang tumakbo."),
    dict(kind="terminal", step="TEST 4", title=T_GB, note="Tama ba ang numero?",
         lines=[("out", "== webhook =="),
                ("out", '{"city":"Manila","temp":28.1,"humidity":68,'),
                ("out", ' "advice":"Be careful when going out because it\'s very hot ..."}'),
                ("out", "== Open-Meteo, diretso =="),
                ("out", '"current":{"time":"2026-11-15T21:30","interval":900,'),
                ("out", '  "temperature_2m":28.1,"relative_humidity_2m":68}'),
                ("note", "Pareho: 28.1 at 68")],
         say="Tama ba ang numero? Tinawag ko ang Open-Meteo nang diretso. Ang temperature ay 28.1, at ang humidity ay 68, parehong-pareho sa sagot ng webhook."),
    dict(kind="shot", img="p17_executions", step="EXECUTIONS", hl=[(66, 458, 312, 516), (66, 162, 312, 222), (372, 88, 720, 130)], note=["Error: 21.721 segundo", "Pinakabago: City not found, 1.136 s", "Ang detalye ng takbo"],
         say="Sa Executions tab, makikita ang lahat ng takbo. Nandito ang error na inabot ng 21.7 segundo, at ang pinakabagong takbo na City not found, na 1.136 segundo lang, sa daan ng False."),
    dict(kind="slide", slide="p4_rules", step="BAGO MO GAMITIN",
         say="Tatlong paalala. Una, ang Test URL ay isang tawag lang, at ang Production URL ay kailangang i-Publish. Pangalawa, pwedeng mabagal o mag-timeout ang mga API, kaya gamitin ang Retry On Fail, at maglagay ng daan para sa maling pangalan. "
             "Pangatlo, ibigay sa AI ang totoong numero, at i-check ang payo, dahil nag-iimbento pa rin ang maliit na model."),
    dict(kind="slide", slide="p4_results", step="BUOD NG TEST",
         say="Ito ang buod ng mga totoong resulta. Walang laman ang sagot kapag sa mismong node nag-Listen. Isang tawag lang ang Test URL. Nag-timeout ang geocoding API. Hindi gumana ang Production URL bago mag-Publish. At nasira ang JSON sa PowerShell. "
             "Pagkatapos ng lahat ng ayos, tama ang Manila: 28.1 degrees at 68 percent."),
    dict(kind="comment", step="COMMENT", comment_q="Anong API ang gusto mong ikonekta sa n8n mo?", comment_sub="I-comment mo sa ibaba!", seconds=5,
         say="Tanong ko sa iyo: anong API ang gusto mong ikonekta sa n8n mo? I-comment mo sa ibaba."),
    # ------------------------------------------------------------ 9. exit ramp
    dict(kind="slide", chapter="Susunod: Part 5, error handling", slide="p4_next", step="SUSUNOD",
         say="Hindi pa tapos ang serye. Sa Part 5, aayusin natin nang tama ang mga error, para hindi basta pumalya ang workflow mo. I-click ang playlist sa screen para panoorin ang buong serye. Nasa description ang workflow file."),
]
