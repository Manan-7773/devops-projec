from flask import Flask
app = Flask(__name__)

@app.route('/')
def myapp():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Capture Photo</title>
  <style>
    video, canvas {
      display: block;
      margin: 10px auto;
      border: 2px solid #333;
    }
    button {
      display: block;
      margin: 20px auto;
      padding: 10px 20px;
      font-size: 18px;
    }
  </style>
</head>
<body>

  <video id="video" width="400" height="300" autoplay></video>
  <canvas id="canvas" width="400" height="300" style="display: none;"></canvas>
  <button id="capture">Capture & Download Photo</button>

  <script>
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const button = document.getElementById('capture');

    // Access webcam
    navigator.mediaDevices.getUserMedia({ video: true })
      .then((stream) => {
        video.srcObject = stream;
      })
      .catch((err) => {
        alert('Error accessing webcam: ' + err);
      });

    // Capture and download photo
    button.addEventListener('click', () => {
      const context = canvas.getContext('2d');
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      // Convert canvas to image
      const imageURL = canvas.toDataURL('image/png');

      // Create download link
      const link = document.createElement('a');
      link.href = imageURL;
      link.download = 'photo.png';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    });
  </script>

</body>
</html>

    """

if __name__=="__main__":
    app.run(host='0.0.0.0' , port=5000)
