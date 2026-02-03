document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);

    const response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    // Store result temporarily
    localStorage.setItem("cropguard_result", JSON.stringify(data));

    // Redirect to result page
    window.location.href = "/result";
});
