document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('auth-modal');
    const openBtn = document.getElementById('open-login-btn');
    const closeBtn = document.getElementById('close-modal-btn');
    const toggleBtn = document.getElementById('toggle-auth-btn');
    
    const registerForm = document.getElementById('register-form');
    const loginForm = document.getElementById('login-form');
    const modalTitle = document.getElementById('modal-title');
    const modalSubtitle = document.getElementById('modal-subtitle');
    const toggleText = document.getElementById('toggle-text');
    
    let isLoginView = false; // Start with registration view by default or login, let's say login.
    // Wait, the prompt asked to generate registration option and login option. Let's make the button "Iniciar Sesión" open the login view.
    
    // Open Modal
    openBtn.addEventListener('click', (e) => {
        e.preventDefault();
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
        
        // Since the button says "Iniciar Sesión", let's open the Login view by default
        switchToLogin();
    });
    
    // Close Modal
    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    };
    
    closeBtn.addEventListener('click', closeModal);
    
    // Close on clicking outside the container
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });
    
    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
    
    // Toggle Views
    const switchToLogin = () => {
        registerForm.classList.add('hidden');
        loginForm.classList.remove('hidden');
        modalTitle.textContent = 'Iniciar Sesión';
        modalSubtitle.textContent = 'Bienvenido de nuevo a RutaPremium.';
        toggleText.textContent = '¿No tienes cuenta?';
        toggleBtn.textContent = 'Regístrate';
        isLoginView = true;
    };
    
    const switchToRegister = () => {
        loginForm.classList.add('hidden');
        registerForm.classList.remove('hidden');
        modalTitle.textContent = 'Registro';
        modalSubtitle.textContent = 'Introduce tus datos para crear tu perfil profesional.';
        toggleText.textContent = '¿Ya tienes cuenta?';
        toggleBtn.textContent = 'Iniciar Sesión';
        isLoginView = false;
    };
    
    toggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
        if (isLoginView) {
            switchToRegister();
        } else {
            switchToLogin();
        }
    });
});
