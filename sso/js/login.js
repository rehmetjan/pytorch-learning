const username = 'admin'
const password = 'MyPassword'

// read from url parameter
var urlParams = new URLSearchParams(window.location.search)
var getUserName = urlParams.get('username')
var getPassword = urlParams.get('password')

console.log(getUserName)
// get the value from the input field and check if it is equals to username and password
if (getUserName === username && getPassword === password) {
  // if the value is correct, redirect to the index.html
  window.location.href = 'index.html'
} else {
  // if the value is wrong, show an alert
  console.log('Wrong username or password')
  console.log(getUserName, getPassword)
}
