function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }

  const form = document.querySelector('form');
  const emailInput = document.querySelector('input[name="email"]');
  const submitButton = document.querySelector('button[type="submit"]');


    emailInput.addEventListener('input', () => {
      if (validateEmail(emailInput.value)) {
        emailInput.classList.remove('is-invalid');
        emailInput.classList.add('is-valid');
        submitButton.removeAttribute('disabled');
      } else {
        emailInput.classList.remove('is-valid');
        emailInput.classList.add('is-invalid');
        submitButton.setAttribute('disabled', '');
      }
    });
  
