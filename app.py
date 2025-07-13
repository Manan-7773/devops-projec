from flask import Flask
app = Flask(__name__)

@app.route('/')
def myapp():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Email Sender</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #f5f7fa;
      padding: 20px;
      margin: 0;
    }

    .container {
      max-width: 500px;
      margin: auto;
      background: #fff;
      padding: 25px 30px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    h2 {
      text-align: center;
      color: #333;
    }

    input, textarea, button {
      width: 100%;
      padding: 12px;
      margin: 10px 0;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      box-sizing: border-box;
      transition: border-color 0.3s ease;
    }

    input:focus, textarea:focus {
      border-color: #007BFF;
      outline: none;
    }

    button {
      background-color: #007BFF;
      color: white;
      border: none;
      cursor: pointer;
      font-weight: bold;
    }

    button:hover {
      background-color: #0056b3;
    }

    .success {
      background-color: #d4edda;
      color: #155724;
      padding: 10px;
      border-radius: 8px;
      margin-top: 10px;
    }

    .error {
      background-color: #f8d7da;
      color: #721c24;
      padding: 10px;
      border-radius: 8px;
      margin-top: 10px;
    }
  </style>
</head>
<body>

  <div class="container">
    <h2>📧 Send Email</h2>
    <input type="email" id="to" placeholder="Recipient Email" required />
    <input type="text" id="subject" placeholder="Email Subject" required />
    <textarea id="body" placeholder="Enter your message here..." rows="6" required></textarea>
    <button onclick="sendMail()">Send Email</button>
    <div id="responseMessage"></div>
  </div>

  <script>
    function sendMail() {
      const to = document.getElementById("to").value.trim();
      const subject = document.getElementById("subject").value.trim();
      const text = document.getElementById("body").value.trim();

      if (!to || !subject || !text) {
        showMessage("All fields are required.", true);
        return;
      }

      fetch('http://localhost:3000/send', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ to, subject, text })
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          showMessage("✅ Email sent successfully!");
          clearForm();
        } else {
          showMessage("❌ Failed to send email: " + data.message, true);
        }
      })
      .catch(err => showMessage("❌ Error: " + err.message, true));
    }

    function showMessage(msg, isError = false) {
      const div = document.getElementById("responseMessage");
      div.className = isError ? "error" : "success";
      div.innerText = msg;
    }

    function clearForm() {
      document.getElementById("to").value = '';
      document.getElementById("subject").value = '';
      document.getElementById("body").value = '';
    }
  </script>

</body>
</html>    """

if __name__=="__main__":
    app.run(host='0.0.0.0' , port=5000)
