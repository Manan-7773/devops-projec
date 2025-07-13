from flask import Flask
app = Flask(__name__)

@app.route('/')
def myapp():
    return """
   <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>📍 My Location Finder</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    * { box-sizing: border-box; }

    body {
      margin: 0;
      padding: 0;
      background: #eef1f6;
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }

    .app-container {
      background: #fff;
      padding: 24px;
      border-radius: 16px;
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.08);
      width: 100%;
      max-width: 420px;
    }

    h2, h3 {
      margin-top: 0;
      color: #222;
      text-align: center;
    }

    p {
      margin: 8px 0;
      color: #444;
    }

    input, button {
      width: 100%;
      padding: 12px 14px;
      margin-top: 12px;
      border-radius: 10px;
      border: 1px solid #ccc;
      font-size: 1rem;
    }

    input:focus {
      border-color: #007bff;
      outline: none;
    }

    button {
      background-color: #007bff;
      color: white;
      font-weight: bold;
      cursor: pointer;
      border: none;
      transition: 0.2s ease;
    }

    button:hover {
      background-color: #0056b3;
    }

    a {
      display: block;
      margin-top: 10px;
      text-align: center;
      color: #007bff;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    hr {
      border: none;
      border-top: 1px solid #ddd;
      margin: 30px 0 20px;
    }

    .section {
      margin-bottom: 20px;
    }

    .location-box {
      background: #f8f9fa;
      padding: 12px;
      border-radius: 10px;
      text-align: center;
    }

    .error-msg {
      color: red;
      text-align: center;
      font-size: 0.9rem;
    }
  </style>
</head>
<body>

  <div class="app-container">
    <h2>📍 My Location Finder</h2>

    <div class="section">
      <h3>🧭 Your Current Location</h3>
      <div class="location-box">
        <p><strong>Latitude:</strong> <span id="lat">--</span></p>
        <p><strong>Longitude:</strong> <span id="lon">--</span></p>
        <a id="map-link" href="#" target="_blank">View on Google Maps</a>
      </div>
      <button onclick="getLocation()">📡 Get My Location</button>
      <p id="error" class="error-msg"></p>
    </div>

    <hr />

    <div class="section">
      <h3>🔍 Search a Location</h3>
      <input type="text" id="search-input" placeholder="e.g. Arya College Jaipur" />
      <button onclick="searchLocation()">🔎 Search on Map</button>
      <a id="search-link" href="#" target="_blank"></a>
    </div>
  </div>

  <script>
    function getLocation() {
      const errorBox = document.getElementById("error");
      errorBox.textContent = "";

      if (!navigator.geolocation) {
        errorBox.textContent = "Geolocation is not supported by your browser.";
        return;
      }

      navigator.geolocation.getCurrentPosition(success, error);

      function success(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        document.getElementById("lat").textContent = lat.toFixed(6);
        document.getElementById("lon").textContent = lon.toFixed(6);

        const mapUrl = `https://www.google.com/maps?q=${lat},${lon}`;
        const link = document.getElementById("map-link");
        link.href = mapUrl;
        link.textContent = "📍 View on Google Maps";
      }

      function error(err) {
        errorBox.textContent = "❌ Location error: " + err.message +
          ". Make sure you're running on localhost or HTTPS.";
      }
    }

    function searchLocation() {
      const query = document.getElementById("search-input").value.trim();
      if (!query) return alert("Please enter a place to search.");

      const encoded = encodeURIComponent(query);
      const url = `https://www.google.com/maps/search/?api=1&query=${encoded}`;

      const link = document.getElementById("search-link");
      link.href = url;
      link.textContent = `📍 View "${query}" on Google Maps`;

      window.open(url, "_blank");
    }
  </script>

</body>
</html>
  """

if __name__=="__main__":
    app.run(host='0.0.0.0' , port=5000)
