async function evaluateModel() {
  const payload = {
    project_name: document.getElementById("projectName").value,
    true_positive: Number(document.getElementById("tp").value),
    false_positive: Number(document.getElementById("fp").value),
    false_negative: Number(document.getElementById("fn").value),
    true_negative: Number(document.getElementById("tn").value),
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/api/evaluate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok) {
      document.getElementById("metrics").innerHTML = `<p>${data.error}</p>`;
      return;
    }

    const metrics = data.metrics;

    document.getElementById("metrics").innerHTML = `
      <div class="metric">Precision: ${metrics.precision}</div>
      <div class="metric">Recall: ${metrics.recall}</div>
      <div class="metric">F1 Score: ${metrics.f1_score}</div>
      <div class="metric">Accuracy: ${metrics.accuracy}</div>
    `;

    document.getElementById("report").textContent = data.report;
  } catch (error) {
    document.getElementById("metrics").innerHTML =
      "<p>Failed to connect to backend. Make sure Flask is running.</p>";
  }
}