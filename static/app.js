fetch('/api/videos')
    .then(response => response.json())
    .then(videos => {
        const videoContainer = document.getElementById('video-container');

        videos.forEach(video => {
            const videoElement = document.createElement('div');
            videoElement.classList.add('video-wrapper');

            videoElement.innerHTML = `
                <h3>${video.title}</h3>
                <div class="rumble">
                    <iframe 
                        src="${video.url}" 
                        width="1920"
                        height="1080"
                        frameborder="0"
                        allowfullscreen
                        sandbox="allow-scripts allow-same-origin allow-popups">
                    </iframe>
                </div>
            `;

            videoContainer.appendChild(videoElement);
        });
    })
    .catch(error => {
        console.error("Error loading videos:", error);
        const videoContainer = document.getElementById('video-container');
        videoContainer.innerHTML = `<p class="error-message">Failed to load videos. Please try again later.</p>`;
    });