const loginInput = document.querySelector("#login-form input");
const loginForm = document.querySelector("#login-form");
const greeting = document.querySelector("#greeting")

function onLoginSubmit(e){
    const username = loginInput.value;
    localStorage.setItem("username",username);
    loginForm.classList.add("hidden");
    paintGreeting(username);
}

function paintGreeting(username){
    greeting.innerText = `Hello ${username}`;
    greeting.classList.remove("hidden");
}

const savedUsername = localStorage.getItem("username");

if(savedUsername === null){
    loginForm.classList.remove("hidden");
    loginForm.addEventListener("submit", onLoginSubmit);
} 
else {
    paintGreeting(savedUsername);
}