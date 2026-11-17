
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>HIHU! 🌸</title>
<style>
* { box-sizing: border-box; }
body {
    background: #080810;
    color: #00ff99;
    font-family: monospace;
    text-align: center;
    padding: 25px 12px;
    min-height: 100vh;
    overflow-x: hidden;
}
.container { margin: 65px auto; max-width: 600px; }
h1 { color: #ff3399; font-size: 65px; }
#log { line-height: 2; font-size: 17px; }
button {
    background: #a000ff;
    color: white;
    border: 0;
    padding: 15px 25px;
    border-radius: 12px;
    font-size: 17px;
    margin-top: 25px;
}
#loading {
    width: 100%;
    background: #333;
    height: 15px;
    border-radius: 20px;
    margin-top: 20px;
    display: none;
}
#bar {
    width: 0%;
    height: 100%;
    background: #00ff99;
    border-radius: 20px;
}
#scare { display: none; }
.big {
    font-size: clamp(65px, 18vw, 115px);
    font-weight: bold;
    color: #ff168b;
    text-shadow: 0 0 25px #ff168b;
    animation: pop .5s infinite alternate;
}
.flowers {
    font-size: 30px;
    line-height: 1.8;
    animation: appear .4s ease;
}
@keyframes pop {
    from { transform: scale(.9); }
    to { transform: scale(1.1); }
}
@keyframes appear {
    from { opacity: 0; transform: scale(.3); }
    to { opacity: 1; transform: scale(1); }
}
#scare p { font-size: 20px; }
</style>
</head>

<body>
<div class="container">

<div id="start">
<h2>⚠ SYSTEM SECURITY CENTER ⚠</h2>
<p>Simulasi pemeriksaan sistem</p>
<button onclick="startScan()">TEKAN UNTUK MEMULAI</button>
</div>

<div id="log"></div>

<div id="loading">
<div id="bar"></div>
</div>

<div id="scare">
<div class="big">HIHU!</div>
<div id="flowers"></div>
<p style="color:#ffdd00">WKWKWKWK 😭💗</p>
<p>LU KENA PRANK CUY!</p>
<p style="color:#00ffcc">HP LU AMAN ❤️</p>
<p style="color:#ff69b4">🌸 HAVE A NICE DAY 🌸</p>
</div>

</div>

<script>
const log = document.getElementById("log");

function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function show(text, delay=1800) {
    log.innerHTML += "<div>" + text + "</div>";
    await wait(delay);
}

async function startScan() {
    document.getElementById("start").style.display = "none";

    await show("[+] Menghubungkan ke sistem...");
    document.getElementById("loading").style.display = "block";

    for(let i=0; i<=100; i+=5) {
        document.getElementById("bar").style.width = i+"%";
        log.innerHTML = log.innerHTML.split("<div>[+] Scanning")[0]
            + "<div>[+] Scanning perangkat " + i + "%</div>";
        await wait(200);
    }

    await show("[+] Menganalisis data...");
    await show("⚠ AKTIVITAS MENCURIGAKAN TERDETEKSI!", 2500);
    await show("BERHASIL DIRETAS!", 2500);

    log.innerHTML += "<div style='color:#ff66cc;font-size:23px'>Coba lihat pojok kiri...</div>";

    // Jeda prank
    await wait(10000);

    log.style.display = "none";
    document.getElementById("loading").style.display = "none";

    document.getElementById("scare").style.display = "block";

    const flowers = ["🌸","🌺","🌷","🌼","💮","🌻","🌹"];

    for(let i=0; i<8; i++) {
        let line = "";
        for(let j=0; j<7; j++) {
            line += flowers[Math.floor(Math.random()*flowers.length)] + " ";
        }

        let row = document.createElement("div");
        row.className = "flowers";
        row.innerHTML = line;

        document.getElementById("flowers").appendChild(row);
        await wait(350);
    }
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
