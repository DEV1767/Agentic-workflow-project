// AI Research Assistant - Frontend Logic

const API_URL = "http://127.0.0.1:8000/research";

const form = document.getElementById("research-form");
const topicInput = document.getElementById("topic-input");
const submitBtn = document.getElementById("submit-btn");
const btnText = submitBtn.querySelector(".btn-text");

const loadingIndicator = document.getElementById("loading-indicator");
const errorBox = document.getElementById("error-box");
const errorMessage = document.getElementById("error-message");

const reportSection = document.getElementById("report-section");
const reportTopic = document.getElementById("report-topic");
const reportContent = document.getElementById("report-content");
const copyBtn = document.getElementById("copy-btn");
const copyText = document.getElementById("copy-text");

let isSubmitting = false;

// 1. Manage button disabled state based on input
topicInput.addEventListener("input", () => {
  if (isSubmitting) return;
  const value = topicInput.value.trim();
  submitBtn.disabled = value.length === 0;
});

// 2. Form submission handler
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const topic = topicInput.value.trim();
  if (!topic || isSubmitting) return;

  // Set loading state
  setLoading(true);
  hideError();
  hideReport();

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ topic: topic }),
    });

    if (!response.ok) {
      let detailMsg = `Server responded with status ${response.status} (${response.statusText})`;
      try {
        const errorData = await response.json();
        if (errorData && errorData.detail) {
          detailMsg = typeof errorData.detail === "string" 
            ? errorData.detail 
            : JSON.stringify(errorData.detail);
        }
      } catch (_) {
        // Fallback to status message if not JSON
      }
      throw new Error(detailMsg);
    }

    const data = await response.json();

    displayReport(data.topic || topic, data.report || "No report generated.");
  } catch (err) {
    let message = err.message;
    if (err.name === "TypeError" && message.includes("Failed to fetch")) {
      message = "Could not connect to the backend server at http://127.0.0.1:8000. Please ensure your FastAPI app is running.";
    }
    showError(message);
  } finally {
    setLoading(false);
    // Refresh button disabled status depending on current input
    submitBtn.disabled = topicInput.value.trim().length === 0;
  }
});

function setLoading(isLoading) {
  isSubmitting = isLoading;
  topicInput.disabled = isLoading;
  submitBtn.disabled = isLoading;

  if (isLoading) {
    submitBtn.classList.add("loading");
    btnText.textContent = "Researching...";
    loadingIndicator.classList.remove("hidden");
  } else {
    submitBtn.classList.remove("loading");
    btnText.textContent = "Generate Research";
    loadingIndicator.classList.add("hidden");
  }
}

function showError(message) {
  errorMessage.textContent = message;
  errorBox.classList.remove("hidden");
}

function hideError() {
  errorBox.classList.add("hidden");
  errorMessage.textContent = "";
}

let rawReportText = "";

function displayReport(topic, report) {
  rawReportText = report;
  reportTopic.textContent = topic;

  // Render markdown if marked is loaded, otherwise fallback to textContent
  if (window.marked) {
    marked.setOptions({
      gfm: true,
      breaks: true,
    });
    const parsedHtml = marked.parse(report);
    reportContent.innerHTML = window.DOMPurify ? DOMPurify.sanitize(parsedHtml) : parsedHtml;
  } else {
    reportContent.textContent = report;
  }

  reportSection.classList.remove("hidden");
  // Scroll to report smoothly
  reportSection.scrollIntoView({ behavior: "smooth", block: "start" });
}

function hideReport() {
  rawReportText = "";
  reportSection.classList.add("hidden");
  reportTopic.textContent = "";
  reportContent.innerHTML = "";
}

// 3. Copy to clipboard functionality
copyBtn.addEventListener("click", async () => {
  const text = rawReportText || reportContent.innerText;
  if (!text) return;

  try {
    await navigator.clipboard.writeText(text);
    copyText.textContent = "Copied!";
    setTimeout(() => {
      copyText.textContent = "Copy";
    }, 2000);
  } catch (_) {
    copyText.textContent = "Failed";
    setTimeout(() => {
      copyText.textContent = "Copy";
    }, 2000);
  }
});
