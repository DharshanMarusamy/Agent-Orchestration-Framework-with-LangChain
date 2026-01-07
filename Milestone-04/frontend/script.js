async function startWorkflow() {
    const topicInput = document.getElementById('topicInput');
    const topic = topicInput.value.trim();
    const runBtn = document.getElementById('runBtn');
    const statusMsg = document.getElementById('statusMessage');
    const errorBox = document.getElementById('errorBox');
    const resultsGrid = document.getElementById('resultsGrid');

    // Specific Output Areas
    const researchOut = document.getElementById('researchOutput');
    const analystOut = document.getElementById('summaryOutput');
    const emailOut = document.getElementById('emailOutput');

    if (!topic) {
        alert("Please enter a research topic!");
        return;
    }

    // 1. RESET UI
    errorBox.style.display = 'none';
    statusMsg.innerText = "🚀 Initializing AI Agents...";
    resultsGrid.classList.add('visible'); // Make grid fade in
    
    // Clear previous results with a loading animation placeholder
    researchOut.innerHTML = '<span class="loading-spinner"></span> Agent is thinking...';
    analystOut.innerText = 'Waiting for Researcher...';
    emailOut.innerText = 'Waiting for Analyst...';
    
    runBtn.disabled = true;

    try {
        // 2. CALL BACKEND
        const response = await fetch('http://127.0.0.1:5000/api/run-workflow', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: topic })
        });

        const data = await response.json();

        // 3. HANDLE ERRORS
        if (data.error) {
            throw new Error(data.error);
        }

        // 4. UPDATE UI WITH RESULTS
        // We map the logs to the specific card IDs
        const logs = data.logs || [];
        
        // Find Researcher Output
        const researchLog = logs.find(log => log.agent === "Researcher");
        if (researchLog) {
            researchOut.innerText = researchLog.output;
            statusMsg.innerText = "✅ Researcher finished. Analyst starting...";
        }

        // Find Analyst Output
        const analystLog = logs.find(log => log.agent === "Analyst");
        if (analystLog) {
            analystOut.innerText = analystLog.output;
            statusMsg.innerText = "✅ Analyst finished. Writing email...";
        }

        // Find Writer Output (Final Email)
        const writerLog = logs.find(log => log.agent === "Writer");
        if (writerLog) {
            emailOut.innerText = writerLog.output;
            statusMsg.innerText = "✨ Workflow Complete!";
        } else if (data.final_email) {
            // Fallback if logs structure is different
            emailOut.innerText = data.final_email;
            statusMsg.innerText = "✨ Workflow Complete!";
        }

    } catch (error) {
        console.error(error);
        errorBox.style.display = 'block';
        errorBox.innerText = "❌ Error: " + error.message;
        statusMsg.innerText = "Workflow Failed.";
        
        researchOut.innerText = "Failed.";
        analystOut.innerText = "Failed.";
        emailOut.innerText = "Failed.";
    } finally {
        runBtn.disabled = false;
    }
}

// Allow pressing "Enter" to search
function handleEnter(event) {
    if (event.key === "Enter") {
        startWorkflow();
    }
}