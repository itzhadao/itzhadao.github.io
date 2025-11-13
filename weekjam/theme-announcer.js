function announceTheme(targetDateISO, themeName) {
    const themeHeader = document.getElementById('theme-header');
    if (!themeHeader) {
        console.error("Element with ID 'theme-header' not found.");
        return;
    }
    
    const targetDate = new Date(targetDateISO);
    const currentDate = new Date();
    
    const contentParagraph = document.createElement('p');

    if (currentDate.getTime() >= targetDate.getTime()) {
        contentParagraph.innerHTML = `Theme: **${themeName}**`;
    } else {
        const targetDateUTC = targetDate.toLocaleDateString('en-US', { 
            year: 'numeric', month: '2-digit', day: '2-digit', timeZone: 'UTC' 
        }) + ' ' + targetDate.toLocaleTimeString('en-US', { 
            hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false, timeZone: 'UTC' 
        }) + ' UTC';
        
        contentParagraph.innerHTML = `Theme will be revealed on **${targetDateUTC}**!`;
    }
    
    themeHeader.parentNode.insertBefore(contentParagraph, themeHeader.nextSibling);
}
