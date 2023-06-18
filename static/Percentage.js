const progressText = document.getElementById('progress-text');

function updateProgress() {
    let progress = 0;
    var percentageInput = document.getElementById('percentage');
    var value = percentageInput.value;
    const interval = setInterval(() => {
        progress += 1;
        progressText.textContent = `${progress}%`;
        if (progress == value) {
          clearInterval(interval);
        }
      }, 20); // Adjust this value to change the speed of the animation
  }