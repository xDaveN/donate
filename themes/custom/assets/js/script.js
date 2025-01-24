console.log("scripts loaded");
const yearDate = new Date().getFullYear().toString();
document.querySelector(".year").innerText = yearDate;

document.querySelectorAll('.crypto-item').forEach(button => {
    button.addEventListener('click', async () => {
        try {
            const address = button.getAttribute('data-address');
            await navigator.clipboard.writeText(address);
            const originalText = button.querySelector('p').textContent;
            button.querySelector('p').textContent = "Address copied";
            setTimeout(() => {
                button.querySelector('p').textContent = originalText;
            }, 3000);
        } catch (err) {
            console.error('Failed to copy text: ', err);
        }
    });
});