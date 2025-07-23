
function signIn() {
  const username = document.getElementById('username').value;
  if (username.trim() !== '') {
    localStorage.setItem('username', username);
    localStorage.setItem('quizzesAttempted', 0); // Init
    window.location.href = "dashboard.html";
  } else {
    alert("Please enter a username");
  }
}
