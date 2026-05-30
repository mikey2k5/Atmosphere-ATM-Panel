document.addEventListener('DOMContentLoaded', () => {
    // 1. Alert Toasts Automatic Fade-Out
    const toasts = document.querySelectorAll('.premium-toast');
    toasts.forEach(toast => {
        setTimeout(() => {
            toast.style.transform = 'translateX(120%)';
            toast.style.opacity = '0';
            toast.style.transition = 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
            setTimeout(() => toast.remove(), 600);
        }, 5000);
    });

    // 2. Preset Withdraw Amount Injector
    const presetBtns = document.querySelectorAll('.preset-btn');
    const amountInput = document.querySelector('input[name="amount"]');
    if (presetBtns.length > 0 && amountInput) {
        presetBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const value = btn.getAttribute('data-value');
                amountInput.value = value;
                // Add focus and light glow
                amountInput.focus();
            });
        });
    }

    // 3. Card Reflect Hover Mechanics
    const premiumCard = document.querySelector('.premium-card');
    if (premiumCard) {
        premiumCard.addEventListener('mousemove', (e) => {
            const rect = premiumCard.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const px = (x / rect.width) * 100;
            const py = (y / rect.height) * 100;
            
            premiumCard.style.setProperty('--x', `${px}%`);
            premiumCard.style.setProperty('--y', `${py}%`);
            
            // Subtle rotation reflection
            const rx = -(py - 50) / 4;
            const ry = (px - 50) / 4;
            premiumCard.style.transform = `perspective(1000px) rotateX(${rx}deg) rotateY(${ry}deg) scale(1.01)`;
        });
        
        premiumCard.addEventListener('mouseleave', () => {
            premiumCard.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)';
        });
    }

    // 4. Submit Spinner Loading State
    const actionForm = document.querySelector('form');
    const submitBtn = actionForm ? actionForm.querySelector('button[type="submit"]') : null;
    if (actionForm && submitBtn) {
        actionForm.addEventListener('submit', (e) => {
            // Check HTML5 validation first
            if (!actionForm.checkValidity()) return;
            
            const originalHtml = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.85';
            submitBtn.innerHTML = `
                <svg class="spinner-icon" viewBox="0 0 50 50" style="animation: spin 1s linear infinite; width: 20px; height: 20px; fill: none; stroke: currentColor; stroke-width: 5; stroke-linecap: round;">
                    <circle cx="25" cy="25" r="20" stroke-dasharray="80 150" stroke-dashoffset="0"></circle>
                </svg>
                Processing Transaction...
            `;
            
            // Allow form submission to continue
        });
    }
});

// Adding styles for spinner dynamically to avoid CSS clutter
const style = document.createElement('style');
style.textContent = `
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .spinner-icon circle {
        stroke: #ffffff;
    }
`;
document.head.appendChild(style);
