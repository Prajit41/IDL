const enterBtn = document.getElementById('enterBtn');

enterBtn?.addEventListener('click', () => {
  const user = localStorage.getItem('debate_user');
  const logged = localStorage.getItem('debate_logged_in') === 'true';

  if (!user) {
    location.href = 'signup.html';
  } else if (!logged) {
    location.href = 'login.html';
  } else {
    location.href = 'index.html#dashboard';
  }
});
