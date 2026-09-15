// Starting page → Resume section
document.getElementById("startButton").addEventListener("click", function () {
    document.getElementById("resumeSection").scrollIntoView({
        behavior: "smooth"
    });
});


// Analyze Resume button → AI
document.getElementById("analyzeButton").addEventListener("click", async function () {

    const resume = document.getElementById("resume").value;
    const role = document.getElementById("role").value;
    const jobDescription = document.getElementById("jobDescription").value;
    const result = document.getElementById("result");

    if (resume.trim() === "") {
        result.innerHTML = "<p>Please enter your resume first.</p>";
        return;
    }

    result.innerHTML = "<p>🤖 AI is analyzing your resume...</p>";

    try {
        const response = await fetch("analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resume: resume,
                role: role,
                jobDescription: jobDescription
            })
        });

        const data = await response.json();

        result.innerHTML = `
            <div class="result-card">
                <h2>🤖 AI Resume Analysis</h2>
                <pre>${data.analysis}</pre>
            </div>
        `;

    } catch (error) {
        result.innerHTML = `
            <div class="result-card">
                <h2>❌ Error</h2>
                <p>Could not connect to the AI backend.</p>
            </div>
        `;
    }
});
