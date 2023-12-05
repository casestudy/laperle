function submitForm(event) {
    event.preventDefault();
    const form = document.getElementById('contactForm');
    const formData = new FormData(form);
    const name = formData.get('name');
    const email = formData.get('email');
    const message = formData.get('message');
  
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Message:', message);
  }
  