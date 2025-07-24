function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Dummy login — use real backend in production
  if (username === "admin" && password === "1234") {
    localStorage.setItem("isLoggedIn", "true");
    window.location.href = "dashboard.html";
  } else {
    document.getElementById("error").innerText = "Invalid credentials!";
  }
}

function checkLogin() {
  if (localStorage.getItem("isLoggedIn") !== "true") {
    window.location.href = "indexx.html";
  }
}

function logout() {
  localStorage.removeItem("isLoggedIn");
  window.location.href = "indexx.html";
}
